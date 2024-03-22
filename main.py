import math


def main():
    # Main function
    stop = 0
    while stop != 1:
        user_input = float(input("Input a decimal number: "))
        base_number = int(input("Input the base number: "))
        user_input = list(str(user_input))
        signBit = sign_bit(user_input[0])  # Gets the sign bit


        if user_input[0] == '-':
            user_input.remove('-')

        user_input = normalize(user_input, base_number)
        if user_input[-1] == "True":
            user_input.pop()
            base_number = int(user_input[-1])
            user_input.pop()

        elif user_input[-1] == "False":
            user_input.pop()

        output = [int(num) for num in user_input]
        # -------------------------------------------

        msb = most_significant_bit(output[0])
        exponentPrime = exponent_prime_hexadecimal(base_number)
        combination_field = find_combination_field(output[0], msb, exponentPrime)

        exponent_continuation = get_exponent_continuation(exponentPrime)

        coefficient_continuation = get_coefficient_field(output[1:])

        output_binary(signBit, combination_field, exponent_continuation, coefficient_continuation)
        output_hex(signBit, combination_field, exponent_continuation, coefficient_continuation)

        # print("Sign bit: ", signBit)
        # print("Combination field: ", combination_field)
        # print("Exponent Continuation: ", exponent_continuation)
        # print("Coefficient Continuation: ", coefficient_continuation)
        # Use the above prints to test
        stop = int(input("Do you want to quit?: "))  # Input 1 to end the loop. This is for test purposes
def sign_bit(index):
    if index == '-':
        return 1
    else:
        return 0


def most_significant_bit(decimal):
    stop = 1
    num = 8
    binary = []
    while stop <= 4:
        if decimal >= num:
            decimal = decimal - num
            num = num / 2
            binary.append(1)
            stop += 1
        else:
            binary.append(0)
            num = num / 2
            stop += 1
    return binary


def exponent_prime_hexadecimal(base):
    base = base + 101
    stop = 1
    num = 128
    binary = []
    while stop <= 8:
        if base >= num:
            base = base - num
            num = num / 2
            binary.append(1)
            stop += 1
        else:
            binary.append(0)
            num = num / 2
            stop += 1
    return binary


def find_combination_field(msb_decimal, msb_hexadecimal, exponent_prime):
    combination_field = []
    if 0 <= msb_decimal <= 7:
        combination_field.append(exponent_prime[0])
        combination_field.append(exponent_prime[1])
        combination_field.append(msb_hexadecimal[1])
        combination_field.append(msb_hexadecimal[2])
        combination_field.append(msb_hexadecimal[3])
    else:
        combination_field.append(1)
        combination_field.append(1)
        combination_field.append(exponent_prime[0])
        combination_field.append(exponent_prime[1])
        combination_field.append(msb_hexadecimal[3])
    return combination_field


def get_exponent_continuation(exponent_prime):
    exponent_prime = exponent_prime[2:]
    return exponent_prime


def get_coefficient_field(nums):
    # print(nums)
    section1 = merge_num_list(nums[0:3])
    section2 = merge_num_list(nums[3:])
    updated_section1 = []
    updated_section2 = []
    final_section = []

    if section1[0] == 0 and section1[4] == 0 and section1[8] == 0:
        updated_section1.append(section1[1])  # b
        updated_section1.append(section1[2])  # c
        updated_section1.append(section1[3])  # d
        updated_section1.append(section1[5])  # f
        updated_section1.append(section1[6])  # g
        updated_section1.append(section1[7])  # h
        updated_section1.append(0)  # v
        updated_section1.append(section1[9])  # j
        updated_section1.append(section1[10])  # k
        updated_section1.append(section1[11])  # m
    elif section1[0] == 0 and section1[4] == 0 and section1[8] == 1:
        updated_section1.append(section1[1])  # b
        updated_section1.append(section1[2])  # c
        updated_section1.append(section1[3])  # d
        updated_section1.append(section1[5])  # f
        updated_section1.append(section1[6])  # g
        updated_section1.append(section1[7])  # h
        updated_section1.append(1)  # v
        updated_section1.append(0)
        updated_section1.append(0)
        updated_section1.append(section1[11])  # m

    elif section1[0] == 0 and section1[4] == 1 and section1[8] == 0:
        updated_section1.append(section1[1])  # b
        updated_section1.append(section1[2])  # c
        updated_section1.append(section1[3])  # d
        updated_section1.append(section1[5])  # f
        updated_section1.append(section1[6])  # g
        updated_section1.append(section1[7])  # h
        updated_section1.append(1)  # v
        updated_section1.append(0)
        updated_section1.append(1)
        updated_section1.append(section1[11])  # m

    elif section1[0] == 0 and section1[4] == 1 and section1[8] == 1:
        updated_section1.append(section1[1])  # b
        updated_section1.append(section1[2])  # c
        updated_section1.append(section1[3])  # d
        updated_section1.append(1)
        updated_section1.append(0)
        updated_section1.append(section1[7])  # h
        updated_section1.append(1)  # v
        updated_section1.append(1)
        updated_section1.append(1)
        updated_section1.append(section1[11])  # m

    elif section1[0] == 1 and section1[4] == 0 and section1[8] == 0:
        updated_section1.append(section1[9])  # j
        updated_section1.append(section1[10])  # k
        updated_section1.append(section1[3])  # d
        updated_section1.append(section1[5])  # f
        updated_section1.append(section1[6])  # g
        updated_section1.append(section1[7])  # h
        updated_section1.append(1)  # v
        updated_section1.append(1)
        updated_section1.append(0)
        updated_section1.append(section1[11])  # m

    elif section1[0] == 1 and section1[4] == 0 and section1[8] == 1:
        updated_section1.append(section1[5])  # f
        updated_section1.append(section1[6])  # g
        updated_section1.append(section1[3])  # d
        updated_section1.append(0)
        updated_section1.append(1)
        updated_section1.append(section1[7])  # h
        updated_section1.append(1)  # v
        updated_section1.append(1)
        updated_section1.append(1)
        updated_section1.append(section1[11])  # m

    elif section1[0] == 1 and section1[4] == 1 and section1[8] == 0:
        updated_section1.append(section1[9])  # j
        updated_section1.append(section1[10])  # k
        updated_section1.append(section1[3])  # d
        updated_section1.append(0)
        updated_section1.append(0)
        updated_section1.append(section1[7])  # h
        updated_section1.append(1)  # v
        updated_section1.append(1)
        updated_section1.append(1)
        updated_section1.append(section1[11])  # m

    elif section1[0] == 1 and section1[4] == 1 and section1[8] == 1:
        updated_section1.append(0)
        updated_section1.append(0)
        updated_section1.append(section1[3])  # d
        updated_section1.append(1)
        updated_section1.append(1)
        updated_section1.append(section1[7])  # h
        updated_section1.append(1)  # v
        updated_section1.append(1)
        updated_section1.append(1)
        updated_section1.append(section1[11])  # m

    if section2[0] == 0 and section2[4] == 0 and section2[8] == 0:
        updated_section2.append(section2[1])  # b
        updated_section2.append(section2[2])  # c
        updated_section2.append(section2[3])  # d
        updated_section2.append(section2[5])  # f
        updated_section2.append(section2[6])  # g
        updated_section2.append(section2[7])  # h
        updated_section2.append(0)  # v
        updated_section2.append(section2[9])  # j
        updated_section2.append(section2[10])  # k
        updated_section2.append(section2[11])  # m

    elif section2[0] == 0 and section2[4] == 0 and section2[8] == 1:
        updated_section2.append(section2[1])  # b
        updated_section2.append(section2[2])  # c
        updated_section2.append(section2[3])  # d
        updated_section2.append(section2[5])  # f
        updated_section2.append(section2[6])  # g
        updated_section2.append(section2[7])  # h
        updated_section2.append(1)  # v
        updated_section2.append(0)
        updated_section2.append(0)
        updated_section2.append(section2[11])  # m

    elif section2[0] == 0 and section2[4] == 1 and section2[8] == 0:
        updated_section2.append(section2[1])  # b
        updated_section2.append(section2[2])  # c
        updated_section2.append(section2[3])  # d
        updated_section2.append(section2[9])  # j
        updated_section2.append(section2[10])  # k
        updated_section2.append(section2[7])  # h
        updated_section2.append(1)  # v
        updated_section2.append(0)
        updated_section2.append(1)
        updated_section2.append(section2[11])  # m

    elif section2[0] == 0 and section2[4] == 1 and section2[8] == 1:
        updated_section2.append(section2[1])  # b
        updated_section2.append(section2[2])  # c
        updated_section2.append(section2[3])  # d
        updated_section2.append(1)
        updated_section2.append(0)
        updated_section2.append(section2[7])  # h
        updated_section2.append(1)  # v
        updated_section2.append(1)
        updated_section2.append(1)
        updated_section2.append(section2[11])  # m

    elif section2[0] == 1 and section2[4] == 0 and section2[8] == 0:
        updated_section2.append(section2[9])  # j
        updated_section2.append(section2[10])  # k
        updated_section2.append(section2[3])  # d
        updated_section2.append(section2[5])  # f
        updated_section2.append(section2[6])  # g
        updated_section2.append(section2[7])  # h
        updated_section2.append(1)  # v
        updated_section2.append(1)
        updated_section2.append(0)
        updated_section2.append(section2[11])  # m

    elif section2[0] == 1 and section2[4] == 0 and section2[8] == 1:
        updated_section2.append(section2[5])  # f
        updated_section2.append(section2[6])  # g
        updated_section2.append(section2[3])  # d
        updated_section2.append(0)
        updated_section2.append(1)
        updated_section2.append(section2[7])  # h
        updated_section2.append(1)  # v
        updated_section2.append(1)
        updated_section2.append(1)
        updated_section2.append(section2[11])  # m

    elif section2[0] == 1 and section2[4] == 1 and section2[8] == 0:
        updated_section2.append(section2[9])  # j
        updated_section2.append(section2[10])  # k
        updated_section2.append(section2[3])  # d
        updated_section2.append(0)
        updated_section2.append(0)
        updated_section2.append(section2[7])  # h
        updated_section2.append(1)  # v
        updated_section2.append(1)
        updated_section2.append(1)
        updated_section2.append(section2[11])  # m

    elif section2[0] == 1 and section2[4] == 1 and section2[8] == 1:
        updated_section2.append(0)
        updated_section2.append(0)
        updated_section2.append(section2[3])  # d
        updated_section2.append(1)
        updated_section2.append(1)
        updated_section2.append(section2[7])  # h
        updated_section2.append(1)  # v
        updated_section2.append(1)
        updated_section2.append(1)
        updated_section2.append(section2[11])  # m

    final_section.extend(updated_section1)
    final_section.extend(updated_section2)
    return final_section


def merge_num_list(nums):
    # print(nums)
    decimal1 = most_significant_bit(nums[0])
    decimal2 = most_significant_bit(nums[1])
    decimal3 = most_significant_bit(nums[2])
    mergedlist = []
    mergedlist.extend(decimal1)
    mergedlist.extend(decimal2)
    mergedlist.extend(decimal3)
    return mergedlist


def normalize(decimalnumbers, basenumber):
    isBaseNumberUpdated = "False"
    if decimalnumbers[-2] == '.' and decimalnumbers[-1] == '0':
        decimalnumbers.pop()
        decimalnumbers.pop()
    else: # move decimal dot to the right
        temp = decimalnumbers
        decimalnumbers = move_decimal_dot(decimalnumbers)
        basenumber = update_base_number(temp, basenumber)
        isBaseNumberUpdated = "True"
        decimalnumbers.pop()

    count_digits = len(decimalnumbers)
    if count_digits < 7:  # if there are less than 7 digits, pad zeros on the left
        max = 7
        while count_digits < max:
            decimalnumbers.insert(0, '0')
            count_digits += 1

    elif count_digits > 7:  # if there are less than 7 digits, move decimal dot to the right and round off
        decimalnumbers.append('.')
        while True:
            if count_digits > 7:
                indexM = decimalnumbers.index('.') - 1
                indexN = decimalnumbers.index('.')
                decimalnumbers[indexM], decimalnumbers[indexN] = decimalnumbers[indexN], decimalnumbers[indexM]
                count_digits -= 1
                basenumber += 1
            else:
                isBaseNumberUpdated = "True"
                break

        float_digits = list_to_float(decimalnumbers)
        float_digits = round(float_digits)
        # float_digits = which_rounding_method(float_digits) #lets the user decide which rounding method
        decimalnumbers = list(str(float_digits))

    if isBaseNumberUpdated == "True":
        decimalnumbers.append(str(basenumber))
        decimalnumbers.append(isBaseNumberUpdated)
        return decimalnumbers
    else:
        decimalnumbers.append(isBaseNumberUpdated)
        return decimalnumbers


def move_decimal_dot(decimalnumbers):
    while True:
        if decimalnumbers[-1] != '.':
            indexM = decimalnumbers.index('.')
            indexN = decimalnumbers.index('.') + 1
            decimalnumbers[indexM], decimalnumbers[indexN] = decimalnumbers[indexN], decimalnumbers[indexM]
        else:
            break
    return decimalnumbers


def update_base_number(decimalnumbers, basenumber):
    while True:
        if decimalnumbers[-1] != '.':
            indexM = decimalnumbers.index('.')
            indexN = decimalnumbers.index('.') + 1
            decimalnumbers[indexM], decimalnumbers[indexN] = decimalnumbers[indexN], decimalnumbers[indexM]
            basenumber -= 1
        else:
            break
    return basenumber


def list_to_float(digits):
    # Join the list elements into a single string
    number_str = ''.join(digits)

    # If there is no decimal point in the string, add one at the end
    if '.' not in number_str:
        number_str += '.'

    # Convert the string to a float
    return float(number_str)


def output_binary(signbit, combinationfield, exponentcont, coefficientcont):
    combinedstring1 = str(signbit)
    combinedstring2 = ''.join(map(str, combinationfield))
    combinedstring3 = ''.join(map(str, exponentcont))
    combinedstring4 = ''.join(map(str, coefficientcont))

    print(combinedstring1, combinedstring2, combinedstring3, combinedstring4)


def output_hex(signbit, combinationfield, exponentcont, coefficientcont):
    combined_list = [signbit]
    combined_list.extend(combinationfield)
    combined_list.extend(exponentcont)
    combined_list.extend(coefficientcont)
    hex_output = [hex_converter(combined_list[0:4]), hex_converter(combined_list[4:8]),
                  hex_converter(combined_list[8:12]), hex_converter(combined_list[12:16]),
                  hex_converter(combined_list[16:20]), hex_converter(combined_list[20:24]),
                  hex_converter(combined_list[24:28]), hex_converter(combined_list[28:])]
    final_output = ''.join(map(str, hex_output))
    print(final_output)


def hex_converter(decimaldigits):
    if decimaldigits[0] == 0 and decimaldigits[1] == 0 and decimaldigits[2] == 0 and decimaldigits[3] == 0:
        return '0'
    elif decimaldigits[0] == 0 and decimaldigits[1] == 0 and decimaldigits[2] == 0 and decimaldigits[3] == 1:
        return '1'
    elif decimaldigits[0] == 0 and decimaldigits[1] == 0 and decimaldigits[2] == 1 and decimaldigits[3] == 0:
        return '2'
    elif decimaldigits[0] == 0 and decimaldigits[1] == 0 and decimaldigits[2] == 1 and decimaldigits[3] == 1:
        return '3'
    elif decimaldigits[0] == 0 and decimaldigits[1] == 1 and decimaldigits[2] == 0 and decimaldigits[3] == 0:
        return '4'
    elif decimaldigits[0] == 0 and decimaldigits[1] == 1 and decimaldigits[2] == 0 and decimaldigits[3] == 1:
        return '5'
    elif decimaldigits[0] == 0 and decimaldigits[1] == 1 and decimaldigits[2] == 1 and decimaldigits[3] == 0:
        return '6'
    elif decimaldigits[0] == 0 and decimaldigits[1] == 1 and decimaldigits[2] == 1 and decimaldigits[3] == 1:
        return '7'
    elif decimaldigits[0] == 1 and decimaldigits[1] == 0 and decimaldigits[2] == 0 and decimaldigits[3] == 0:
        return '8'
    elif decimaldigits[0] == 1 and decimaldigits[1] == 0 and decimaldigits[2] == 0 and decimaldigits[3] == 1:
        return '9'
    elif decimaldigits[0] == 1 and decimaldigits[1] == 0 and decimaldigits[2] == 1 and decimaldigits[3] == 0:
        return 'A'
    elif decimaldigits[0] == 1 and decimaldigits[1] == 0 and decimaldigits[2] == 1 and decimaldigits[3] == 0:
        return 'B'
    elif decimaldigits[0] == 1 and decimaldigits[1] == 0 and decimaldigits[2] == 1 and decimaldigits[3] == 1:
        return 'C'
    elif decimaldigits[0] == 1 and decimaldigits[1] == 1 and decimaldigits[2] == 0 and decimaldigits[3] == 1:
        return 'D'
    elif decimaldigits[0] == 1 and decimaldigits[1] == 1 and decimaldigits[2] == 1 and decimaldigits[3] == 0:
        return 'E'
    elif decimaldigits[0] == 1 and decimaldigits[1] == 1 and decimaldigits[2] == 1 and decimaldigits[3] == 1:
        return 'F'


def which_rounding_method(number):
    if input == 0:  # nearest zero
        if number >= 0:
            return int(number)
        else:
            return -int(-number)
    elif input == 1:  # floor
        return math.floor(number)
    elif input == 2:  # ceiling
        return math.ceil(number)
    elif input == 3:  # ties to nearest even
        number = round(number)
        return number


if __name__ == '__main__':
    main()
