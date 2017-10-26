###############################################################################
##
##      A representation of our FPGA board, which holds a sequence to be
##      executed
##      Author: Aaron Vontell
##
###############################################################################

from devices import *
from pipistrello import Board
from library import *

class FGPA:
    
    def __init__(self, address):
        '''
        Creates an FPGA board, defined by the given address.
        :param address: The address to connect to
        '''
        self.address = address
        
    def connect(self, kern):
        self.kern = kern
        self.driver = Board(kern)
        print("CONNECTION SUCCESSFUL")
    
    def load(self, identifier):
        
        if identifier == "PIPISTRELLO_DEFAULT":
            get_pipistrello_default(self)
            print("LOADED DEFAULT PIPISTRELLO")
            
            # At this point, we have the board (kernelized) and a qubit spec
            
        else:
            print("ERROR: DESIRED SETUP NOT FOUND")
            
    def characterize(self):
        
        # First, characterize each qubit, if we have any
        for qubit in self.qubits:
            rabi(qubit, board) # Run a Rabi experiment on a qubit given a driver