from artiq.experiment import *


class PulseKernel(EnvExperiment):
    """Simple simulation"""

    def build(self):
        self.setattr_device("core")
        for wo in "abcd":
            self.setattr_device(wo)
            
    def sequence(self, seq):
        this.sequence = seq

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