###############################################################################
##
##      A qubit which is defined by connections from the FPGA to actual
##      hardware.
##      Author: Aaron Vontell
##
###############################################################################


class Qubit:
    """
    Properties of our qubits:
        name - a unique identifier
        T1 - a T1 time, or None if not available
        T2 - a T2 time, or None if not available
        temp - a temperatue, or None if not available
        channels - a dictionary of sources to the ports that we use
        static_field - information regarding any static magnetic field (just for information purposes)
        last_characterized - a dictionary of properties to timestamps
    """

    def __init__(self, name, channels, readout_method, properties=None):
        """
        Creates a definition of a qubit given a name, dictionary of channels, and readout method
        :param name: A name for this qubit
        :param channels: A dictionary as a mapping of ports to channel usages
        :param readout_method: A function(self) which is used to readout the qubit state
        :param properties: A list of properties you would like to keep track of. Defaults to all.
        """
        self.name = name
        self.channels = channels
        self.readout_method = readout_method

        if properties is None:
            self.properties = ['T1', 'T2', 'TEMP']
        else:
            self.properties = properties

    def get_channels(self):
        pass

    def get_readout(self):
        pass
