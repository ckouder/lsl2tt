def ttc_and(a, b):
    """
    proceed and operand on two equal-length columns
    return the result column
    """
    r = []
    for i in range(len(a)):
        r.append(a[i] and b[i])
    return r


def ttc_or(a, b):
    """
    proceed or operand on two equal-length columns
    return the result column
    """
    r = []
    for i in range(len(a)):
        r.append(a[i] or b[i])
    return r


def ttc_not(a):
    """
    proceed not operand on one column
    return the result column
    """
    return [not i for i in a]


def ttc_if(a, c):
    """
    proceed if operand on two equal-length columns
    return the result column
    """
    r = []
    for i in range(len(a)):
        if (a[i] and not c[i]):
            r.append(False)
        else:
            r.append(True)
    return r


def ttc_iff(a, b):
    """
    proceed iff operand on two equal-length columns
    return the result column
    """
    r = []
    for i in range(len(a)):
        if (a[i] != b[i]):
            r.append(False)
        else:
            r.append(True)
    return r
