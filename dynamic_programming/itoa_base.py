def itoa_base(integer, base):
    DIGITS = '0123456789ABCDEF'

    if integer < base:
        return DIGITS[integer]

    # Delaying concatenation until after recursive call returns avoids needing to reverse string
    # reminds of stacks
    return itoa_base(integer // base, base) + DIGITS[integer % base]

print(itoa_base(10, 2))
