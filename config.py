from ttc_operator import *

LSL_SYMBOL = {
    'AND' : '&',
    'OR'  : '|',
    'NOT' : '~',
    'IF'  : '->',
    'IFF' : '<->',
}

OPERATOR_REFERENCE = {
    LSL_SYMBOL['NOT']: ttc_not,
    LSL_SYMBOL['AND']: ttc_and,
    LSL_SYMBOL['OR'] : ttc_or,
    LSL_SYMBOL['IF'] : ttc_if,
    LSL_SYMBOL['IFF']: ttc_iff,
}
