###############################################################################
##
##      A collection of device configurations for ARTIQ
##      Author: Aaron Vontell
##
###############################################################################

from artiq.experiment import *
from artiq.sim import devices

def get_simulator():
    '''
    Creates an FPGA that is a simulation of a device / ARTIQ-enabled FPGA.
    '''
    dmgr = dict()
    dmgr["core"] = devices.Core(dmgr)
    dmgr["pmt"] = devices.Input(dmgr, "pmt")
    dmgr["ttl"] = devices.Output(dmgr, "ttl")
    for wo in "abcd":
        dmgr[wo] = devices.WaveOutput(dmgr, wo)
    

def get_kc707_default()


class SimpleSimulation(EnvExperiment):
    """Simple simulation"""

    def build(self):
        self.setattr_device("core")
        for wo in "abcd":
            self.setattr_device(wo)

    @kernel
    def run(self):
        with parallel:
            with sequential:
                self.a.pulse(100*MHz, 20*us)
                self.b.pulse(200*MHz, 20*us)
            with sequential:
                self.c.pulse(300*MHz, 10*us)
                self.d.pulse(400*MHz, 20*us)

    
    exp = SimpleSimulation(dmgr)
    exp.run()