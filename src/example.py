###############################################################################
##
##      A simple example for characterizing a setup
##      Author: Aaron Vontell
##
###############################################################################

import Qubit
import Sequence
import FPGA
from artiq.experiment import *


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

        # Now we run a blocking experiment which characterizes the setup,
        # and then displays the results
        pip.characterize()
        pip.display_characterization()

        # Now we construct a pulse sequence
        pip.X(Math.PI, "Q0")
        pip.Y(Math.PI/2, "Q0")

        # Finally, we compile and execute the sequence
        def experiment_callback(results):
            results.show()

        pip.execute(experiment_callback)