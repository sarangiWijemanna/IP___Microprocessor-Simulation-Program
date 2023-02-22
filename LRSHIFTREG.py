" Logical-Right-Register-Shift instruction"""


# RTp and RSp is in Binary String Format
def LRSHIFTREG_F(a, b, num_bit):

    y = a.zfill(num_bit)
    # print(f'\nInput RSp value   : {y}')
    aa = int(a, 2)

    # Con_REG Creation
    # print(f'\n Input RTp value : {b}')
    y = b[-5:]
    cnt_REG = int(y, 2)
    # print(f'Counter RTp value : {cnt_REG}\n')

    # Process
    if y[0] == '0':
        ans = (aa >> cnt_REG)
        ans = bin(ans).replace('0b', '').zfill(num_bit)

    if y[0] == '1':
        ans = (aa >> cnt_REG)
        ans = (bin(ans).replace('0b', '').zfill(num_bit))

    return ans  # Return Binary String




