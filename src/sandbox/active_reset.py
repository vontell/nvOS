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
        
        START = now_mu()
		print("Start time: ", START)
		print("Starting pulse")
		self.board.pulse(0, 0.6 * ns, 1)
		print("Pulses placed. Done!")