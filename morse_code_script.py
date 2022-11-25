from morse_dict import morse_dict


def translate_to_morse(message):
    output = ''
    raw_msg = message.split(' ')
    try:
        for word in raw_msg:
            for ch in word:
                letter = morse_dict[ch]
                output += letter + ' '
            if word == raw_msg[-1]:
                continue
            else:
             output += '/' + ' '
    except KeyError:
        print('\nPlease enter valid Characters, only letters and numbers!')
        get_user_message()   
    return user_feedback(output)


def translate_from_morse(message):
    output = ''
    splited_words = message.split('/')
    raw_msg = []
    for word in splited_words:
        letters = word.split(' ')
        raw_msg.append(letters)
    for word in raw_msg:
        for letter in word:
            morse_letter = get_morse_ch(letter)
            if morse_letter == None:
                continue
            else:
                output += morse_letter
        output += " "
    return user_feedback(output)

def get_morse_ch(val):
    for key, value in morse_dict.items():
        if val == value:
            return key
    return None


def get_user_message():
    encode_or_decode = input('Would you like to encode or decode? [enc / dec] >: ').lower()
    if encode_or_decode not in ['enc', 'dec']:
        print('\nPlease enter a valid option: ("enc" or "dec")')
        return get_user_message()
    elif encode_or_decode == 'dec':
        message = input('\nType the morse code you want to decrypt (words separated by "/" and letters by space) >: ').lower()
        return translate_from_morse(message)
    else:
        message = input('\nType the message you want to encode in Morse code >: ').lower()
        return translate_to_morse(message)


def user_feedback(output):
    return print(f'\nYour output >: {output} \n')


get_user_message()
