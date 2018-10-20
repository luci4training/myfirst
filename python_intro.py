print('Hello, Django girls!')

print("Ola" * 3)

a="Ola"

print(a.upper())

mylist=[1,2,3]


print(mylist)
print(len(mylist))

mylist.pop(0)
print(mylist)
mylist.append(1)
print(mylist)


participant = {'name': 'Ola', 'country': 'Poland', 'favorite_numbers': [7, 42, 92]}

print(participant['name'])

participant['favorite_language'] = 'Python'

print(participant)

print(6>7 or 6<7)
print(6>7 and 6<7)
# only True is correct.

if 3 > 2:
    print('It works!')
else:
    print('bla')

name = 'Sonja'
if name == 'Ola':
    print('Hey Ola!')
elif name == 'Sonja':
    print('Hey Sonja!')
else:
    print('Hey anonymous!')


def hi():
    print('Hi there!')
    print('How are you?')
hi()

def sayhello(name):
    if name == 'Ola':
        print('Hey Ola!')
    elif name == 'Sonja':
        print('Hey Sonja!')
    else:
        print('Hey ' + name)

sayhello("Ola")
sayhello("Luciana")

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Me']

for name in girls:
    #print(name)
    sayhello(name)

for i in range(1, 6):
    print(i)
# "range" is half-open, and by that we mean it includes the first value, but not the last.


#myvenv\Scripts\activate
