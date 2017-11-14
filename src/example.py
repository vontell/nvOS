###############################################################################
##
##      A simple example for characterizing a setup
##      Author: Aaron Vontell
##
###############################################################################

from fpga import FPGA
from artiq.experiment import *


class SimpleExample(EnvExperiment):
    """
    Initializes an experiment and setup, and does a characterization on a single
    qubit.
    """

    def build(self):
        address = '0.0.0.0:2452'
        self.pip = FPGA(address, verbosity=1)   # Initializes an FPGA object to use as the base of our setup
        self.pip.load("PIPISTRELLO_DEFAULT")    # Defines the ports and methods for acting on this setup
        self.pip.connect(self)                  # We connect the experiment to the FPGA

    @kernel
    def run(self):

        # Now we run a blocking experiment which characterizes the setup,
        # and then displays the results
        self.pip.characterize()

        # pip.display_characterization()
        #
        # # Now we construct a pulse sequence
        # pip.X(Math.PI, "Q0")
        # pip.Y(Math.PI / 2, "Q0")
        #
        # # Finally, we compile and execute the sequence
        # def experiment_callback(results):
        #     results.show()
        #
        # pip.execute(experiment_callback)
