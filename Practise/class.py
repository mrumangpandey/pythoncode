class Person:
     def __init__(self, name):
         self.name = name 
     
     def talk(self):
         print(f"Hi I'm {self.name}")  
         
         
         
john = Person('Umang pandey')       
john.talk()


bob = Person('Bob sing')
bob.talk()