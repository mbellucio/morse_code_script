from morse_dict import morse_dict

morse_code = morse_dict

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

def get_user_message():
    message = input('\nType the message you want to encode in Morse code >: ').lower()
    return translate_to_morse(message)

def user_feedback(output):
    print(f'\nYour translation message in to morse code >: \n {output} \n')
    print('Paste the Morse message on this website to check the result: \n https://morsecode.world/international/translator.html\n')

get_user_message()
    