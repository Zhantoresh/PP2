a = 5
print(type(a))
#object of class "int"

b = 3.14
print(type(b))
#objext of class "float"

c = "hello"
print(type(c))
#class of object "str"

class Person:
    name = "Linux"
    age = 18
Person.age = 35
person = Person()
person2 = Person()
print(person.name)
print(person.age)
person2.name = "Sasha"
person2.age = 20
print(person2.age)
