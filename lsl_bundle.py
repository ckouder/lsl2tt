import regex
from config import LSL_SYMBOL

GLOBAL_RULE = '({}?[A-z]|{}?\((?R)\))(?: ?([{}{}]|{}|{}) ?({}?[A-z]|{}?\((?R)\)))*'\
.format(
    LSL_SYMBOL['NOT'],
    LSL_SYMBOL['NOT'],
    LSL_SYMBOL['AND'],
    LSL_SYMBOL['OR'],
    LSL_SYMBOL['IF'],
    LSL_SYMBOL['IFF'],
    LSL_SYMBOL['NOT'],
    LSL_SYMBOL['NOT'],
)

# (\~)*(\()*(\w)(\|)*(\(|\))*(\|)*

SIMPLE_RULE = '\(?({}?)([a-zA-Z]) ?([{}{}]|{}|{}) ?({}?)([a-zA-Z])\)?'\
.format(
    LSL_SYMBOL['NOT'],
    LSL_SYMBOL['AND'],
    LSL_SYMBOL['OR'],
    LSL_SYMBOL['IF'],
    LSL_SYMBOL['IFF'],
    LSL_SYMBOL['NOT'],
)

def ruleGenerator(num_of_parenthese):
    SINGLETON_OPERATOR = LSL_SYMBOL['NOT']
    BINARY_OPERATORS = '()'

def LSLGrammarIsOk(lsl_string):
    return regex.match(GLOBAL_RULE, lsl_string)[0] == lsl_string
