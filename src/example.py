###############################################################################
##
##      A simple example for characterizing a setup
##      Author: Aaron Vontell
##
###############################################################################

from src.fpga import FPGA
from artiq.experiment import *


class SimpleExample(EnvExperiment):
    """
    Initializes an experiment and setup, and does a characterization on a single
    qubit.
    """

    def __init__(self):
        self.pip = None
        super()

    def build(self):
        address = '0.0.0.0:2452'
        self.pip = FPGA(address, verbosity=1)   # Initializes an FPGA object to use as the base of our setup
        self.pip.load("PIPISTRELLO_DEFAULT")    # Defines the ports and methods for acting on this setup

    @kernel
    def run(self):

        # We connect the kernel to the FPGA
        self.pip.connect(self)

        # Now we run a blocking experiment which characterizes the setup,
        # and then displays the results
        pip.characterize()

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
