# name = input("Enter name:")
# age = int(input("Enter age:"))
# location = input("Enter location:")
# print("hello there my name is",name,"am",age,"of age and i stay at",location)


# input_string = input('Enter elements of a list separated by space ')
# user_list = input_string.split()
# for i in range(len(user_list)):
#     user_list[i] = int(user_list[i])
# print("Sum = ", sum(user_list))

# x = (input('some text : '))
# x = {a for a in x.split(",")}
# print(x)


# number = input("Enter 1st set")#takes input from users
# number2 = input("Enter 2nd set")

# number = {a for a in number.split()} #converts the input into a set and sets the slipt function
# number2 = {b for b in number2.split()}
# print(number)
# print(number2) 

# print(number.intersection(number2))

# words=["table","food","bus","airplane","school","queen"]
# output=[word for word in words if len(word)%2==1]
# print(output)

#words=["table","food","bus","airplane","school","queen"]
# for word in words: 
# print(len(word[0:]))#print length number of each element


# Write a function called convert_add that takes a list of strings as an 
# argument and converts it to integers and sums the list. For example 
# [‘1’, ‘3’, ‘5’] should be converted to [1, 3, 5] and summed to 9.

def convert_add():
    numbers = ["1","2","3","4","5"]
    output =[]
    for i in numbers:
        output.append(int(i))
    print(numbers)
    print(output)
    print(sum(output))
convert_add()