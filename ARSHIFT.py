" Arithmetic-Right-Shift instruction"""


# Input RSp is in binary string
def ARshiftF(a, cnt, num_bit):
    y = a.zfill(num_bit)
    aa = int(a, 2)
    # print(f'\n\nInput RSp value  : {y}')

    if y[0] == '0':
        ans = (aa >> cnt)
        ans = (bin(ans).replace('0b', ''))
        ans = ans.rjust(num_bit, '0')

    if y[0] == '1':
        ans = (aa >> cnt)
        ans = (bin(ans).replace('0b', ''))
        ans = ans.rjust(num_bit, '1')

    return ans  # In binary string Out
