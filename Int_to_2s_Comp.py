" Instructions to two's Complements"""

# Variable Declaration
num_bit = 32


def flip_binary(d):
    if d == '0':
        return '1'
    else:
        return '0'


def One_And_Twos_Complement(Binary_Value):
    Length_of_Binary_Value = len(Binary_Value)
    Ones_Complement = ""

    for i in range(Length_of_Binary_Value):
        Ones_Complement += flip_binary(Binary_Value[i])

    Ones_Complement = list(Ones_Complement.strip(""))
    Twos_Complement = list(Ones_Complement)
    for i in range(Length_of_Binary_Value - 1, -1, -1):

        if Ones_Complement[i] == '1':
            Twos_Complement[i] = '0'
        else:
            Twos_Complement[i] = '1'
            break

    i -= 1
    if i == -1:
        Twos_Complement.insert(0, '1')

    Twos_Complement_string = ''
    # print("1's complement: ", *Ones_Complement, sep="")
    # print("2's complement: ", *Twos_Complement, sep="")
    # print(type(Twos_Complement))
    Twos_Complement_string = ("".join(Twos_Complement))
    # print(type(Twos_Complement_string))
    return Twos_Complement_string


def integerToBinary(c, num_bit):
    z = ''
    if c >= 0:  # Positive
        z = bin(c).replace('0b', '').zfill(num_bit)

    if c < 0:  # Negative
        c = bin(-c)
        x = c.replace('0b', '').zfill(num_bit)
        z = (One_And_Twos_Complement(x))

    return z
