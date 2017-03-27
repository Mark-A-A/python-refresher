age = 27

name = "Mark"

sentence = "I am " + str(age)

nameSentence = "My name  is {}".format(name)
ageSentence ="I am {} years old.".format(age)

sentence4 = "My name  is {} and I am {} years old.".format(name,age)
# print(nameSentence)
# print(ageSentence)
print(sentence4)

year = 1830 # When you check your solution, don't change this number'

if year < 2100 and year > 2000:
    print('Welcome to the 21st century!')
else:
    print('You are before or after the 21st century')



def sayHello(name="Python"):
    # print("Hello World")
    return "Hello {}".format(name)

sentence6 = sayHello()
print(sentence6)

sentence7 = sayHello(name)
print(sentence7)

sentence8 = sayHello("Matthew")
print(sentence8)



def trippleprint (str):

    string="{}{}{}".format(str, str, str)
    print(string)

trippleprint("hello")
    # print(string)
    # print(string)
    # print(string)
