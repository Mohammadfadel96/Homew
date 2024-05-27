# Write a Python program that converts a Binary number into its equivalent Decimal number.
# The program should start reading the binary number from the user. Then the decimal equivalent number must be
# calculated. Finally, the program must display the equivalent decimal number on the screen.
# Tips: solve input errors.
def B_2_D_Converter(bi_num):
    dec_num = 0
    for digit in bi_num:
        if digit != '0' and digit != '1':
            return None
        dec_num = dec_num * 2 + int(digit)
    return dec_num
bi_num = input("Enter a Binary number to know it's Decimal equivalent\n")
dec_num = B_2_D_Converter(bi_num)
if dec_num is not None:
    print(f"the decimal equivalent for '{bi_num}' is {dec_num}")
else:
    print("invalid input")

