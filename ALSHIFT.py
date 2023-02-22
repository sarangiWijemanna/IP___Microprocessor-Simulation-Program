"Arithmetic-Left-Shift instruction """

# Import integer two's complement function
from Int_to_2s_Comp import *


def ALshiftF(a, cnt):
    alshift_Int = a << cnt
    ans = integerToBinary(alshift_Int)

    return ans


