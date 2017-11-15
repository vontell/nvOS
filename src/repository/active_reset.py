from artiq.experiment import *
from pipistrello import Board

class ActiveReset(EnvExperiment):
    '''
    Does an active reset of a given qubit.
    '''

    def build(self):
        self.board = Board(self)

    @kernel
    def run(self):

#		self.board.reset()
#		self.board.get_core().break_realtime()
#		delay(2*s)
#		START = now_mu()
#		print("Start time: ", START)
#		print("Starting pulse")
#		self.board.pulse(0, .6 * ns, 1)
#		delay(10 * ns)
#		self.board.pulse(0, .6 * ns, 1)
#		print("Pulses placed. Done!")


        # Example for running 
        self.board.characterize()   # Run experiments to characterize qubit properties
        q0 = self.board.getQubit(0) # Obtain a reference to the equipment used to talk to a qubit
        q0.reset()                  # The goal is that this will be an active reset, but this is for later
        q0.PI()                     # Apply a simple PI pulse
        q0.readout()                # Readout the state of the qubit