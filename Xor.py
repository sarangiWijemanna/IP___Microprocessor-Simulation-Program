"XOR instructions"""


# Define XOR function
def xorF(a, b):
    n = max(len(a), len(b))
    ans = ""

    # Loop to iterate over the
    # Binary Strings
    for i in range(n):

        # If the Character matches
        if a[i] == b[i]:
            ans += "0"
        else:
            ans += "1"

    return ans
