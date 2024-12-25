# customer = {
#     'name': 'Umang',
#     'age': 27,
#     'is_verified': True
#     }




# customer['birthdate'] = '04 oct 1997'
# print(customer.get('phone','No phone number available'))

# print(customer['birthdate'])



phone = input('Enter the phone number : ')
digits_mapping = {
    "1" : 'one',
    "2" : 'two',
    "3" : 'three',
    "4" :  'four',
    "5" : 'five',
    "6" : 'six',
    "7" : 'seven',
    "8" : 'eight',
    "9" : 'nine',
    "0" : 'zero'
}

output = ""
for i in phone:
    output += digits_mapping.get(i, "!") + ' '
     
print(output)    
