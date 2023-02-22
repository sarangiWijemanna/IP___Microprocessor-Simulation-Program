" Logical-Right-Shift instruction"""


# Input RSp is in binary string
def LRSHIFTF(a, cnt, num_bit):
    y = a
    aa = int(a, 2)
    # print(f'\nInput RSp value   : {y}')

    if y[0] == '0':
        ans = (aa >> cnt)
        ans = bin(ans).replace('0b', '').zfill(num_bit)

    if y[0] == '1':
        ans = (aa >> cnt)
        ans = (bin(ans).replace('0b', '').zfill(num_bit))

    return ans  # In binary string Out
