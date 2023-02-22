" Subtraction Instruction"""


def twos_complement(val, nbits):
    """Compute the 2's complement of int value val"""
    val = int(val,2)
    if val < 0:
        val = (1 << nbits) + val
    else:
        if (val & (1 << (nbits - 1))) != 0:
            # If sign bit is set.
            # compute negative value.
            val = val - (1 << nbits)
    return val


def Subtraction(a, b, N, Status):
    c1 = 0
    c2 = 0
    Result = ""

    for num in range(N-1, -1, -1) :
        ax = int(a[num],2)
        bx = int(b[num],2)
        
        S = str(c1 ^ (ax ^ bx))
        Result = Result + S

        c2 = c1 & (~(ax ^ bx)) | (~ax) & bx

        Status["CF"] = c2
        Status["OF"] = c1 ^ c2
        c1 = c2  
    Result = Result[::-1]

    # Sign Function flag Function
    if Result[0] == '1':
        Status["SF"] = 1
    if Result[0] == '0':
        Status["SF"] = 0

    # Zero Function flag Function
    decimalResult = int(Result, base=2)
    if decimalResult == 0:
        Status["ZF"] = 1
    if decimalResult != 0:
        Status["ZF"] = 0

    return  Result, Status

        

