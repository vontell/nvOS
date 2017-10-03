###############################################################################
##
##      A simple example of an X gate on a qubit
##      Author: Aaron Vontell
##
###############################################################################

import Qubit
import Sequence
import FPGA


# First we connect to the board
address = '0.0.0.0:2452'
kc707 = FPGA(address)
kc707.connect()
ck707.load("KC707_DEFAULT")

# Now we construct a pulse sequence
kc707.X("Q0")

# Finally, we compile and execute the sequence
def experiment_callback(results):
    #plot results here
    result.show()

kc707.execute(experiment_callback)