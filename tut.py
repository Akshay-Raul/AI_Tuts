name = input("Enter your name:")
age = input("Enter your age:")
isTut = True

'''
 a 
 multiline
 comment
'''

print("Name:"+name+"\n Age:"+age)

aList = ["Aki", True, 25]

print(aList.index("Aki"))


def hello(name="Max"):
	print("Hello " + name)

def add(num1, num2):
	return num1+num2

shape= (32,32,1)
dicti = {"brand":"bmw", "price" : 25000}

hello()

hello("Thomas")
hello("Mesut")


if isTut:
	print("isTut is True")
else:
	print("isTut is not True")



num = 10
while(num > 0):
	print(num)
	num -= 1
print("End of the loop")


rangeList = ["Aki", True, 25]


for i in rangeList:
	print(i)


twoDim = [[1,2,3],[5,7,8]]

for i in twoDim:
	print(i[0])



selectedList = [1,3,4,6,7,8,4,3]

newList= []
newList.extend(range (1,20))
newList.extend(range (0,20))

print(newList)

'''
w3schools
'''

'''
try:
	x=10
	print(x)
except NameError:
	print("Variable x is not defined")
except:
	print("Something else went wrong")

# Own
try:
	print("This is a number: " + 15)
except:
	raise Exception("Number is not a string")
finally:
	print("Cleanup")
'''


f = open("Hello.txt", "a")
f.write("Now the file has more content!")
f.close()

f = open("Hello.txt", mode = "r")
text = f.readlines()
print(text)





