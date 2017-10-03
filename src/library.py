###############################################################################
##
##      A collection of useful, common pulse sequences
##      Author: Aaron Vontell
##
###############################################################################

def active_reset(qubit, params, callback):
    '''
    Actively resets the QUBIT to the 0 state with 99.5% probability.
    :param qubit: The qubit which we are resetting
    :param params: Experiment parameters, if needed.
    :param callback: A function to call with either an error or a result.
    '''

def pi_over_2(qubit, params, callback):
    '''
    Applies a PI/2 pulse to the given QUBIT, given PARAMs. Calls a CALLBACK
    when the experiment is finished.
    :param qubit: The qubit which we are applying this pulse to.
    :param params: Experiment parameters, if needed.
    :param callback: A function to call with either an error or result.
    '''
    pass

def pi(qubit, params, callback):
    '''
    Applies a PI pulse to the given QUBIT, given PARAMs. Calls a CALLBACK
    when the experiment is finished.
    :param qubit: The qubit which we are applying this pulse to.
    :param params: Experiment parameters, if needed.
    :param callback: A function to call with either an error or result.
    '''
    pass

def ramsey(qubit, params, callback):
    '''
    Applies a Ramsey to the given QUBIT, given PARAMs. Calls a CALLBACK
    when the experiment is finished.
    :param qubit: The qubit which we are applying this pulse to.
    :param params: Experiment parameters, if needed.
    :param callback: A function to call with either an error or result.
    '''
    pass

def hahn_echo(qubit, params, callback):
    '''
    Applies a Hahn echo to the given QUBIT, given PARAMs. Calls a CALLBACK
    when the experiment is finished.
    :param qubit: The qubit which we are applying this pulse to.
    :param params: Experiment parameters, if needed.
    :param callback: A function to call with either an error or result.
    '''
    pass

###############################################################################
##
##  REFERENCES
##
##  [1] https://www.qudev.phys.ethz.ch/sites/default/files/users/abdu/QSITHS2012/StandardMeasurementsInQIP.pdf
##
###############################################################################