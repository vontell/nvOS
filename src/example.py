###############################################################################
##
##      A simple example for characterizing a setup
##      Author: Aaron Vontell
##
###############################################################################

import Qubit
import Sequence
import FPGA


class SimpleExample(EnvExperiment):
	'''
	Does a characterization of available qubits
	'''
	
	def build(self):
		address = '0.0.0.0:2452'
        self.pip = FPGA(address)
		
	@kernel
	def run(self):

        # First we connect to the board
        pip.connect(self)
        pip.load("PIPISTRELLO_DEFAULT")

        # Now we run a blocking experiment which characterizes the setup
        pip.characterize()

        # Now we construct a pulse sequence
        pip.X("Q0")

        # Finally, we compile and execute the sequence
        def experiment_callback(results):
            #plot results here
            result.show()

        pip.execute(experiment_callback)