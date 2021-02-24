import string

field = string.ascii_lowercase

cipher = "ljfv xdpl"
a, b = 7, 9


def affine_de(aVal, bVal, ci):
    # field = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # inverse modulo value
    x = 0
    for i in range(26):
        if (aVal * i) % 26 == 1:
            x = i

    # affine decrypt formula
    decrpyt = []
    for letter in ci:
        index = field.find(letter)
        if index != -1:
            index = (x * (index - bVal) % 26)
            decrpyt.append(field[index])
        else:
            decrpyt.append(letter)

    return "".join(decrpyt)


print(affine_de(a, b, cipher))
