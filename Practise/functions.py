def emoji_converter(message):
    emojis = {
        ':)' : '😊',
        ':(' : '😒'
    }

    word = message.split(' ')
    output =""
    for i in word:
        output += emojis.get(i, i) + ' '
    return output


message = input('Enter the message : ')
result = emoji_converter(message)

print(result)