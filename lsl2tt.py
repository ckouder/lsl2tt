from ttc_operator import *
from lsl_bundle import *
from config import *
import regex

compond_var_num = 0
NAMES = "abcdefghijklmnopqrstuvwxyz"
CELL_SEPARATOR = "|"
ROW_SEPARATOR = "=="

def substitueAtomicLSLWithLetter(lsl_string):
    '''
    substitue atomic lsl string with single letter in a complex lsl string

    @param lsl_string: a grammarical lsl string
    @return list: (reduced lsl string, matched object, letter)
    '''
    global compond_var_num
    simple_lsl_match = regex.search(SIMPLE_RULE, lsl_string)
    # print(simple_lsl_match)
    name = NAMES[compond_var_num]
    compond_var_num += 1

    return (lsl_string.replace(simple_lsl_match[0], name), simple_lsl_match, name)

def findSymbols(lsl_string):
    '''
    find symbols of a lsl string.
    @param lsl_string: a grammarical lsl string
    @return list: list of strings
    '''
    l = [x for x in set(regex.findall(r'[A-Z]', lsl_string))]
    l.sort()
    return l

def generateAtomicTruthTable(symbols):
    '''
    generate atomic truth table for symbols
    @param symbols: symbols
    @return list: list of symbols and their corresponding truth values
    '''
    atomic_truth_table = {}
    for i in symbols:
        c = 2 ** symbols.index(i)
        atomic_truth_table[i] = \
        ([True for x in range(0, c)] + \
        [False for y in range(0, c)]) * int((2 ** len(symbols)) / (c * 2))

    return atomic_truth_table

def getTruthColumnForAtomicLSL(atomic_lsl, truth_table):
    '''
    Get truth column for atomic LSL
    '''
    # the result components would be like (~, a, |, ~, b)
    components = regex.search(SIMPLE_RULE, atomic_lsl)
    col_a = truth_table[components.group(2)]
    col_b = truth_table[components.group(5)]

    if components.group(1) == LSL_SYMBOL['NOT']:
        col_a = OPERATOR_REFERENCE[LSL_SYMBOL['NOT']](col_b)

    if components.group(4) == LSL_SYMBOL['NOT']:
        col_b = OPERATOR_REFERENCE[LSL_SYMBOL['NOT']](col_b)

    result_col = OPERATOR_REFERENCE[components.group(3)](col_a, col_b)

    # print(result_col)
    return result_col

def reformat(truth_table, reference_table):
    '''
    Reformat the truth table to make it understandable
    '''
    truth_table_keys = sorted(truth_table.keys(), reverse=True)
    reference_table_keys = sorted(reference_table.keys(), reverse=True)
    reformat_table = [[] for x in range(len(truth_table_keys))]
    key = 0
    for ttk in truth_table_keys:
        truth_col = truth_table[ttk]
        negator = ""
        if len(ttk) == 2 and ttk[1] in reference_table:
            true_key = reference_table[ttk[1]]
            negator = ttk[0]

        elif len(ttk) == 1 and ttk in reference_table:
            true_key = reference_table[ttk]

        else:
            true_key = ttk

        while regex.search(r'[a-z]', true_key) != None:
            symbol = regex.search(r'[a-z]', true_key)[0]
            true_key = regex.sub(symbol, reference_table[symbol], true_key)

        reformat_table[key].append(negator + true_key)
        reformat_table[key].extend(truth_table[ttk])
        key += 1
    return reversed(reformat_table)

def fantasticPrint(truth_table):
    '''
    Make the output as fantastic as possible
    '''
    printed_format = list(map(list, zip(*truth_table)))
    print("The result truth table of {} is ... \n\n\n".format(text_input))
    for m in range(len(printed_format)):
        r = ""
        for n in range(len(printed_format[m])):
            r = r + str(printed_format[m][n]) + '\t'
            if n < len(printed_format[m]) - 1:
                r += CELL_SEPARATOR
        print(r)
        if m == 0:
            print(ROW_SEPARATOR * len(r))
    print("\n\n\n")


######################################################
######### Main Program Starts Below Here #############
######################################################

print(
    '''
    Welcome to truth table convertor(TTC) ver.0.1
    Please follow instructions to input your LSL expressions.

        and => &
        or  => |
        not => ~
        if  => ->
        iff => <->

    Only single English character is considered as a legal sentential variable.
    Please use () to separate triary LSL expressions. e.g
    A & B & C will throw en error, while (A & B) & C is all fine.
    Have fun and enjoy!

    Copyright (c) 2019-2100 Copyright All Rights Not Reserved.
    '''
)

while True:
    text_input = input("please input a lsl expression: ").upper()
    lsl_string = text_input

    if (LSLGrammarIsOk(lsl_string)):
        # generate atomic truth table for symbols in the lsl string
        truth_table = generateAtomicTruthTable(findSymbols(lsl_string))
        reference_table = {}

        # extract atomic lsl expression and compute its truth column
        while len(lsl_string) > 2:
            (lsl_string, matched, symbol) = substitueAtomicLSLWithLetter(lsl_string)
            reference_table[symbol] = matched[0]
            truth_table[symbol] = getTruthColumnForAtomicLSL(matched[0], truth_table)

        if len(lsl_string) == 2:
            truth_table[lsl_string] = OPERATOR_REFERENCE[LSL_SYMBOL['NOT']](truth_table[lsl_string[-1]])
            del truth_table[lsl_string[-1]]

        printable = reformat(truth_table, reference_table)
        fantasticPrint(printable)

    else:
        print("Illegal input detected, please check your grammar.")
