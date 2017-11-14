# Abstraction of the Pipistrello board to be used for easily creating
# experiments that use the board
# Author: Aaron Vontell
# Date: October 21, 2016

from artiq.experiment import Experiment, kernel, us, ms, parallel
import numpy as np


class Board:

    def __init__(self, experiment):

        self.experiment = experiment
        experiment.setattr_device('core')

        # Set the attributes for each TTL output (0-14), PMT input, and LED

        experiment.setattr_device('pmt0')
        experiment.setattr_device('pmt1')
        experiment.setattr_device('ttl0')
        experiment.setattr_device('ttl1')
        experiment.setattr_device('ttl2')
        experiment.setattr_device('ttl3')
        experiment.setattr_device('ttl4')
        experiment.setattr_device('ttl5')
        experiment.setattr_device('ttl6')
        experiment.setattr_device('ttl7')
        experiment.setattr_device('ttl8')
        experiment.setattr_device('ttl9')
        experiment.setattr_device('ttl10')
        experiment.setattr_device('ttl11')
        experiment.setattr_device('ttl12')
        experiment.setattr_device('ttl13')
        experiment.setattr_device('ttl14')
        experiment.setattr_device('ttl15')
        experiment.setattr_device("led1")
        experiment.setattr_device("led2")
        experiment.setattr_device("led3")
        experiment.setattr_device("led4")

        self.ttls = [
            experiment.ttl0,
            experiment.ttl1,
            experiment.ttl2,
            experiment.ttl3,
            experiment.ttl4,
            experiment.ttl5,
            experiment.ttl6,
            experiment.ttl7,
            experiment.ttl8,
            experiment.ttl9,
            experiment.ttl10,
            experiment.ttl11,
            experiment.ttl12,
            experiment.ttl13,
            experiment.ttl14,
            experiment.ttl15
        ]

        self.pmt = [
            experiment.pmt0,
            experiment.pmt1
        ]
        
        self.leds = [
            experiment.led1,
            experiment.led2,
            experiment.led3,
            experiment.led4
        ]

        # The minimum latency that we have determined for this board for
        # reliable placement of events into the timeline
        # Set to a default of 2 microseconds
        self.LATENCY = 2 * us

    @kernel
    def reset(self):
        """
        Resets the board This should be called at the start of every 'run'
        command in your experiment
        """
        self.get_core().reset()

    @kernel
    def find_latency(self, max_value, tries, timeout, ttl):
        """
        Finds the latency associated with placing events into the
        timeline for this board. Takes as parameters a `max_value` latency
        which is a starting value for the binary search procedure upper bound,
        a 'tries' count for the number of tests the board should use
        for each latency guess, a `timeout` which is the total
        number of guesses that should be made before the binary search
        halts, and a `ttl` which is an output that is safe to test on

        SAVES THIS LATENCY IN CLASS VARIABLE `self.LATENCY`
        """
        
        total_count = 0
        min_value = 0.0
        
        # Now find the correct value
        while total_count < timeout:

            #print("Total count: ", total_count)
            self.reset() # Reset any timeline configurations
            delay(1*s)
            guess = (max_value - min_value)/ 2.0 + min_value
            #print("Trying with guess: ", guess)
            test_count = 0
            #print("[" , min_value , ",", max_value, "]")
            while test_count < tries:
                test_count += 1
                try:
                    delay(guess)
                    self.ttls[ttl].pulse(guess)
                except RTIOUnderflow:
                    #print("Failed with guess: ", guess)
                    min_value = guess
                    break
                except RTIOCollision:
                    #print("Failed with guess: ", guess)
                    min_value = guess
                    break
            else:
                #print("Succeeded with guess below")
                #print(guess)
                max_value = guess
            
            total_count += 1

        self.LATENCY = max_value
        return max_value

    
    @kernel
    def led_test(self):
        '''Flashes LEDs on the board to test the connection'''

        self.leds[0].pulse(250*ms)
        self.leds[1].pulse(250*ms)
        self.leds[2].pulse(250*ms)
        self.leds[3].pulse(250*ms)
        with parallel:
            self.leds[0].pulse(500*ms)
            self.leds[1].pulse(500*ms)
            self.leds[2].pulse(500*ms)
            self.leds[3].pulse(500*ms)

    @kernel
    def pulse(self, ttl, period, length):
        '''
        Pulses the FPGA on ttl with a period of period. If no length is given,
        then the pulse will be continuous. Otherwise, the pulse will occur for
        length iterations
        '''
        
        half_period = period / float(2)
        count = 0
        while count < length:
            self.ttls[ttl].pulse(half_period)
            delay(half_period)
            count += 1

    @kernel
    def pulseDC(self, ttl, length):
        '''
        Turns on the given ttl for a length of length
        '''
        self.ttls[ttl].pulse(length)

    @kernel
    def rotate(self, array):
        '''Rotates an array, deleting the oldest value'''
        neg_one = np.int64(-1)
        array = array[neg_one:] + array[:neg_one]
        array[0] = 0
        return array

    @kernel
    def register_rising(self, detector, results, start, index, begin, threshold=0, tolerance=0*us):
        '''
        Fires a method (handler) when the count of rising edges on a given
        input detector reaches a certain threshold (which defaults to 0). Returns this board for chaining capabilities. Optionally allows for defining
        the start time to begin listening (defaults to now), and the amount of
        time to listen for (defaults to forever)
        
        NOTE: Make sure to call unregister_rising() to reset the detector once done
                This method will call unregister_rising() when the threshold is
                reached, but this event may never occur
        '''

        timestamps = [-1 for i in range(threshold)]
        neg_one = np.int32(-1)

        # Set the timeline pointer to start
        at_mu(start)

        # Starting now, begin detecting rising edges
        self.pmt[detector]._set_sensitivity(1)

        while True:
            last = self.pmt[detector].timestamp_mu()
            if last > 0:

                # Rotate the timestamp list
                timestamps = timestamps[neg_one:] + timestamps[:neg_one]
                timestamps[0] = last
                difference = timestamps[0] - timestamps[-1]
                if difference > 0 and timestamps[neg_one] > 0:# and difference < window + tolerance:
                    at_mu(last)
                    # Record results
                    results[index] = (threshold, timestamps[-1] - begin, timestamps[0] - begin)
                    break

        return results

    @kernel
    def record_rising(self, detector, start, timeout, timestamps):
        '''
        Records the rising edges on a given detector for the given amount of
        time (timeout). Unlike `register_rising`, this method simply returns
        a list of timestamps for rising edges that were recorded for a certain
        period of time. `start` is the starting time to begin recording.
        buffer_size is the size of the pre allocated array used to hold
        timestamps
        '''

        # Set the timeline pointer to start
        at_mu(start)

        # Starting now, begin detecting rising edges for the desired amount of
        # time
        self.pmt[detector].gate_rising(timeout)

        end = now_mu()

        # Now begin listening for edges and record timestamps
        head = 0
        while True:

            # Get the timestamp
            last = self.pmt[detector].timestamp_mu()

            # Add it to a list
            if last > 0 and last < end:
                timestamps[head] = last
                head = head + 1

            # If time is past timeout, stop
            if last > end or self.get_core().get_rtio_counter_mu() > end:
                break

        timestamps = timestamps[0 : head + 1]
        return timestamps


    @kernel
    def get_echo(self, detector, handler, start, end):
        '''
        Grabs timestamps of falling and rising edges on an input channel,
        and returns them as a list such that an output can echo the input
        sequence. Note that due to the list operations, this method will finish
        executing long after the input signal has finished.
        
        Takes as parameters the input detector, the method to call once threshold is
        reached (this handler should take two parameters, this board and a list of timestamps),
        and the start and end time (in machine units) to listen for events.
        '''

        # Set the timeline pointer to start
        at_mu(start)

        # Starting now, begin detecting all edges
        self.pmt[detector]._set_sensitivity(3)

        # End the listening
        at_mu(end)
        self.pmt[detector]._set_sensitivity(0)

        # List of timestamps
        timestamps = []

        while True:
            # If we are past the end listening time, then exit
            if self.experiment.core.get_rtio_counter_mu() > end:
                at_mu(end)
                delay(1 * s) #TODO: Not a good delay!
                handler(self, timestamps)
                break

            # Otherwise, check if there is a new timestamp
            last = self.pmt[detector].timestamp_mu()
            if last > 0:
                timestamps.append(last)

    
    @kernel
    def unregister_rising(self, detector, start):
        '''
        Unregisters the given detector from listening for rising edges by turning
        the input off at an unspecified later date. Must be provided a time
        for when it should turn off this pmt
        '''
        
        self.pmt[detector]._set_sensitivity(0)

    
    @kernel
    def get_core(self):
        '''
        Returns the core device, in situations where granular control is
        necessary
        '''
        
        return self.experiment.core
        
        
    def print_underflow(self):
        '''
        Returns a string that can be printed when an UnderflowError occurs
        These errors occur when you run the board at a speed that is too fast
        for instruction timing to keep up.
        '''
        
        print("UnderflowError on Pipistrello Board (your instructions are beginning to overlap)")