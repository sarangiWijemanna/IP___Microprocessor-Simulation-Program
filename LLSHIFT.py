" Logical-Left-Shift instruction"""

from Int_to_2s_Comp import *


def LLshiftF(a, cnt):
    llshift_Int = a << cnt
    ans = integerToBinary(llshift_Int,num_bit)

    return ans



