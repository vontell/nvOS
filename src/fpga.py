###############################################################################
##
##      A representation of our FPGA board, which holds a sequence to be
##      executed
##      Author: Aaron Vontell
##
###############################################################################

class FGPA:
    
    def __init__(self, address):
        '''
        Creates an FPGA board, defined by the given address.
        :param address: The address to connect to
        '''
        self.address = address