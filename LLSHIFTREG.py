" Logical-Left-Register-Shift instruction"""

from Int_to_2s_Comp import *

# RSp is in Integer Input
# RTP is in Binary String Format


def LLshiftRegF(a, b):
    # print(f'\nInput RSp value   : {a}')

    # Con_REG Creation
    # print(f'\n Input RTp value : {b}')
    y = b[-5:]
    cnt_REG = int(y, 2)
    # print(f'Counter RTp value : {cnt_REG}\n')

    # Process
    llshiftREG_Int = a << cnt_REG
    # print(llshiftREG_Int)
    ans = integerToBinary(llshiftREG_Int)

    return ans  # Return Binary String








    llshift_Int = a >> cnt
    ans = integerToBinary(llshift_Int)

    return ans


