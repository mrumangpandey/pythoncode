message = input('Enter your message : ')
emojis = {
    ':)' : '😊',
    ':(' : '😒'
}

word = message.split(' ')
output =""
for i in word:
    output += emojis.get(i, i) + ' '
    
print(output)    

##ADDING SOMETHING
