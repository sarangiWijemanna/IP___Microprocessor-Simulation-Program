" Define AND function"""


def AndF(a, b):
    n = max(len(a), len(b))
    ans = ""

    # Loop to iterate over the
    # Binary Strings
    for i in range(n):

        # If the Character matches
        if a[i] == b[i] == '1':
            ans += '1'
        else:
            ans += '0'

    return ans