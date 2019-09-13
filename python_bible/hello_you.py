#Ask user for name
name = input("Please enter your name : ")
#Ask user for their age
age = input("Please enter your age : ")
#Ask user for their city
city = input("Please enter your city : ")
#Ask user what they enjoy
love = input("Please enter your hobby : ")
#create output text
string = "Your name is {} and you are {} years old. You live in {} and you love {}"
output = string.format(name,age, city, love)
#print output on screen
print(output)
