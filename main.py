print('Menu')
print('-------------')
print('1. Encode')
print('2. Decode')
print('3. Quit')

def encode_password(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password

program = True

if program:

    option = input('Please enter an option: ')

    if option == '1':
        password = input('Please enter your password to encode: ')
        encoded_password = encode_password(password)
        print('Your password has been encoded and stored!')
    elif option == '2':
        print('000')

    elif option == '3':

        program = False




