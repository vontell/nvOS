###############################################################################
##
##      A collection of device configurations for ARTIQ
##      Author: Aaron Vontell
##
###############################################################################

from qubit import Qubit


def get_pipistrello_default(setup):
    """
    Given an FPGA setup, sets the qubits to be used in our default Pipistrello lab setup
    :param setup: The FPGA object that will be using these qubits
    :return: None
    """
    
    # First, create the qubits
    q0 = Qubit("Q0", {"mw": "ttl0", "green": "ttl1", "apd": "pmt0"}, None)
    setup.qubits = [q0]
    # Sometimes we will set a driver here, but this is done previously for the pip
