try:
    age = int(input('Enter the age : '))
    income = 2000
    risk = income/age 
    print(age)
    
    
except ValueError:
    print('Please enter the valid numbers')
except ZeroDivisionError:
    print("Age can't be zero")    
    