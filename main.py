# python_instructors = ["skinny","Mutemi","John","Ali","Maureen","Grey"]
# count = 0
# while count < len(python_instructors):
#   print("instructor=",python_instructors[count])
#   count += 1

#A = [[1, 4, 5, 12],[-5, 8, 9, 0],[-6, 7, 11, 19]]
# print("A=",A)
#print("A[1]=",A[1])
# print("A[1][2]=",A[1][2])
# print("A=",A[0][3])

# column = []; # empty list
# for row in A:
#   column.append(row[2])
# print("3rd column=",column)


#transposing using nested loop comprehesion
# X = [[12,7],
#    [4 ,5],
#        [7 ,8]]

# Result = [[X[i][j] for i in range(len(X))] for j in range(len(X[0]))]   
# for r in Result:
#   print(r)

#transposing
# X = [[12,7],
#     [4 ,5],
#     [3 ,8]]

# result = [[0,0,0],
#          [0,0,0]]

# # iterate through rows
# for i in range(len(X)):
#    # iterate through columns
#    for j in range(len(X[0])):
#        result[j][i] = X[i][j]

# for r in result:
#    print(r)
# iterate through rows
#for i in range(len(X)):
#    # iterate through columns
   #for j in range(len(X)):
#        result[i][j] = X[i][j] + Y[i][j]

# for r in result:
#    print(r)


#numpy practice

# import numpy as np

# a = np.array([1, 2, 3])

# print(a)

# vowels = ["a", "e", "i", "o", "u"]

# def vowel_counter(str):
#   return len([char for char in str if char in vowels])

# print(vowel_counter("enthusiasm"))

#classes and objects
# class Person:
#   def __init__(self):
#     self.name = "kamash"
#     self.age = 25
# details = Person()
# details.name = "Giddy"
# details.age = 21
# print(details.name)
# print(details.age)

# class Person:
#   def displayinfo(self):
#     print('personal information')
# p1 = Person()
# p1.displayinfo()


# class Person:
#   def __init__(self,age,name):
#     self.name = name
#     self.age = age
    
#   def displayinfo(self):
#     print("person name:",self.name,",person age:",self.age)
# p1=Person("kamash",25)
# p1.displayinfo()

