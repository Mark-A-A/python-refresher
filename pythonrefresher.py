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

# Arrays are Python Lists
shoes = ["Spizikes", "Air Force 1","Curry 2","Melo 5"]
print(shoes)
shoes.insert(0, "Jordan 11")

print(shoes)
del(shoes[1])
print(shoes)


dogs = ["Fido","Sonny", "Cloud", "Maggie", "Ralph"]
print(dogs)
for dog in dogs:
    print(dog)

while len(dogs) > 0:
    print(dogs)
    del(dogs[0])

numbers = [76, 83, 16, 69, 52, 78, 10, 77, 45, 52, 32, 17, 58, 54, 79, 72, 55, 50, 81, 74, 45, 33, 38, 10, 40, 44, 70, 81, 79, 28, 83, 41,
14, 16, 27, 38, 20, 84, 24, 50, 59, 71, 1, 13, 56, 91, 29, 54, 65, 23, 60, 57, 13, 39, 58, 94, 94, 42, 46, 58, 59, 29, 69, 60, 83, 9, 83, 5, 64, 70, 55, 89, 67, 89, 70, 8, 90, 17, 48, 17, 94, 18,
98, 72, 96, 26, 13, 7, 58, 67, 38, 48, 43, 98, 65, 8, 74, 44, 92]

for num in numbers:
    if num > 90:
        print(num)
