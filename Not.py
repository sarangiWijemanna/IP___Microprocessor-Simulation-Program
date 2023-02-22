# NOT Function
def Not(a):
    n = len(a)
    ans = ""

    # Loop to iterate over the
    # Binary Strings
    for i in range(n):

        # If the Character matches
        if a[i] == '1':
            ans += '0'
        else:
            ans += '1'

    return ans
