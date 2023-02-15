# Python program to check if all digits of a number divide it

def check_if_all_digit_divide_num(num):
    temp = num

    while temp > 0:
        if temp % 10 == 0:
            return 'No'
        else:
            last_digit = temp % 10
            if num % last_digit == 0:
                temp //= 10
                continue
            else:
                return 'No'
    return 'Yes'

num = int(input('Enter number : '))
print(f'All digits of a number {num} divides it ? : {check_if_all_digit_divide_num(num)}')


"""
o/p
Enter number : 7879
All digits of a number 7879 divides it ? : No
----------
Enter number : 66
All digits of a number 66 divides it ? : Yes
"""