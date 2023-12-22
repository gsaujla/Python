x=[]
y=4
for i in range(1,int(y)):
   x.append(i)

print(x)
def sayhi():
    return ("Hello World")

def myname(name):
    print(name + " says " + sayhi())
myname("Gurmehar")

def cuber(x):
    return (pow(x,3))
print(cuber(2))

is_hero = False
if is_hero:
    print(True)
else:
 print(False)

i=1
while (i < 11):
    print(i)
    i += 1

secret_word = "aujla"
guess = ""
i = 0
while guess != secret_word :
    if i < 4:
     guess = input("Guess My last name : ")
     i += 1
    else:
        break
if guess == secret_word:
    print("Wallah")
else:
    print("Sorry You Ran outta tries")











