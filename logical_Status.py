" logical Status"""


def logicalStatus(c, Status):
    # Sign Function flag Function
    if c[0] == '1':
        Status["SF"] = 1
    if c[0] == '0':
        Status["SF"] = 0

    # Zero Function flag Function
    decimalResult = int(c, base=2)
    if decimalResult == 0:
        Status["ZF"] = 1
    if decimalResult != 0:
        Status["ZF"] = 0

    # Overflow Flag
    Status["OF"] = 0

    # Carry Flag
    Status["OF"] = 0

    return Status
