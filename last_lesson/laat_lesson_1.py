"""
 class = сложны тип данных





"""


class User:
     amount = 0

     def __init__(self, firs_name, last_name, age):
         User.amount += 1
         self.first_name = firs_name
         self.last_name = last_name
         self.age = age

jack = User("jakc", "barbaro", 15)
print(jack)
