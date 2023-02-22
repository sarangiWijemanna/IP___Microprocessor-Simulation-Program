# Defined OR Function
def OrF(a, b, n):
    ans = ""

    # Loop to iterate over the
    # Binary Strings
    for i in range(n):

        # If the Character matches
        if a[i] == b[i] == '0':
            ans += '0'
        else:
            ans += '1'

    return ans
