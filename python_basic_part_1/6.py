# numbersInput = input().split(', ')
#
# print(list(numbersInput))
# print(tuple(numbersInput))


values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ', list)
print('Tuple : ', tuple)

"""
Write a Python program which accepts a sequence of comma-separated 
numbers from user and generate a list and a tuple with those numbers. Go to the editor
Sample data : 3, 5, 7, 23
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""
