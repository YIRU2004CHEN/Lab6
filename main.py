print('Menu')
print('-------------')
print('1. Encode')
print('2. Decode')
print('3. Quit')



program = True

# Yiru Chen
def encode_password(password):
    # Initialize an empty string to store the encoded password.
    encoded_password = ""
    # Iterate through each digit in the input password.
    for digit in password:
        # Apply the encoding logic: shift the digit by 3 positions in a circular manner.
        encoded_digit = str((int(digit) + 3) % 10)
        # Append the encoded digit to the result.
        encoded_password += encoded_digit
    # Return the encoded password.
    return encoded_password

#Jess Barnes
def decoding_password(password):
    decoded_password = ''
    for i in password:
        decode_digit = (str(int(i) - 3))
        decoded_password += decode_digit
    return decoded_password

if program:

    option = input('Please enter an option: ')

    if option == '1':
        password = input('Please enter your password to encode: ')
        encoded_password = encode_password(password)
        print('Your password has been encoded and stored!')
    elif option == '2':
        password = input('Please enter your password to encode: ')
        decoded_password = decoding_password(password)
        print('Your password has been encoded and stored!')
    elif option == '3':

        program = False

