###############################################################################
##
##      A representation of our FPGA board, which holds a sequence to be
##      executed
##      Author: Aaron Vontell
##
###############################################################################

from src.devices import *
from src.sandbox.pipistrello import Board
from library import *
from artiq.experiment import kernel


class FPGA:

    def __init__(self, address, verbosity=0):
        """
        Creates an FPGA board, defined by the given address.
        :param address: The address to connect to
        :param verbosity: Logging verbosity level (default 0, or no logs)
        """
        self.address = address
        self.characterization_results = {}
        self.driver = None
        self.verbosity = verbosity

    def load(self, identifier):
        """
        Loads setup configurations into this blank setup, which configures where each
        qubit is and which interfaces talk to it. Setups can be found in devices.py
        :param identifier: The identifier for the desired setup.
        """
        if identifier == "PIPISTRELLO_DEFAULT":
            get_pipistrello_default(self)
            self.print_log(1, "LOADED DEFAULT PIPISTRELLO")
        else:
            raise NameError("Desired setup not found in load() or devices.py: " + identifier)

    def connect(self, kern):
        """
        Connects to the given driver, by creating a board and pinging the setup.
        :param kern: The kernelized experiment that is using this setup.
        """
        self.driver = Board(kern)
        self.print_log(1, "CONNECTION SUCCESSFUL")
            
    def characterize(self, name=None):
        """
        Characterizes each qubit through a series of experiments, such as Rabi oscillations.
        Results are stored by timestamp or by a given name.
        :param name: An optional name for this characterization experiment
        """

        # As an initial test, we will simply attempt to pulse the LEDs
        self.driver.led_test()
        
        # # First, characterize each qubit, if we have any
        # for qubit in self.qubits:
        #     rabi(qubit, self.driver) # Run a Rabi experiment on a qubit given a driver
        #     # Save the results in self.characterization_results
            
    def available_characterizations(self):
        """
        Returns a list of all characterization records that are available, in order of
        time executed. Records can be read using get_characterization().
        """
        return self.characterization_results.keys()
    
    def get_characterization(self, key):
        """
        Returns the characterization record mapped from 'key'
        :param key: The key to a given record, as found from available_characterizations()
        """
        return self.characterization_results[key]

    def print_log(self, verbosity, message):
        if verbosity >= self.verbosity:
            print(format("FPGA LOG: %s", message))
