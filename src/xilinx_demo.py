###############################################################################
##
##      A simple and quick demo to confirm that the Xilinx is connected
##      and working
##      Author: Aaron Vontell
##
###############################################################################

from artiq.experiment import *

class SimpleXilinxExample(EnvExperiment):
    '''
    Does a characterization of available qubits
    '''

    def build(self):

        self.setattr_device('core')
        self.setattr_device('pmt0')
        self.setattr_device('ttl0')
        self.setattr_device('ttl1')

    @kernel
    def run(self):

        # Reset the core, delay for 1 second, and pulse for 250 ms
        self.get_core().reset()
        delay(1000*ms)
        self.pulse(250*ms)