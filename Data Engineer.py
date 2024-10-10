#Spliting text
text = 'You cannot end a sentence with because because because is a conjunction'
print(text.split(' '))
#Slicing out the phrase 'because because because'
text =  'You', 'cannot', 'end', 'a', 'sentence', 'with', 'because', 'because', 'because', 'is', 'a', 'conjunction'
first_six = text[0:6]
last_eight = text[9:11]
print(text[6:8])
#Finding if''Coding For All' start with a substring Coding?
text = 'Coding For All'
if text.startswith('Coding'):
    print(True)
else:
    print(False)
#Finding if 'Coding For All' end with a substring coding?
text = 'Coding For All'
if text.endswith('Coding'):
    print(True)
else:
    print(False)

#Removing the left and right trailing spaces from '   Coding For All      ' 
text = '   Coding For All      '
print(text.strip(' '))

#Using new line escape sequence to separate
sentence = "I am enjoying this challenge.\nI just wonder what is next."
print(sentence)

#Declaring a list
cars = ('BMW', 'Audi', 'Benz')

#Find length of list
cars = ['BMW', 'Audi', 'Benz']
print(len(cars))

#Declaring list
mixed_data_types = ['name, age, height, marital status']
name = 'Brian'
age = 21
height = 162
marital_status = 'single'
print(mixed_data_types)

#New code
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[0])
print(it_companies[3])
it_companies.insert(0,'Azure') #Insert Azure
if 'Google' in it_companies:
    print (True)
else:
    print(False)
    
#Slicing out the first 3 companies from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies[0:3])

#Slicing last digits
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies[3:6])

#Removing the first IT company from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies.remove('Facebook'))

#Removing all IT companies from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies.clear())

#Joining lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
my_list = front_end + back_end
print(my_list)

#New code
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort() #sorting a list
print(ages)

#Tuples
bros = ('Brian' 'John' 'Dan')
siz = ('Nora' 'Shar' 'Nao')
siblings = (bros) + (siz)
space = (' ')
print(siblings)

#New Code, converting to a list
bros = ('Brian' 'John' 'Dan')
print(list(bros))

#Sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))
#Adding to a set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it_companies.add('Twitter')
print(it_companies)

#Removing item from set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it_companies.remove('IBM')
print(it_companies)

#Joining sets
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.union(B))

#New code
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
if (A.issubset(B)):
    print(True)
else:
    print(False)
    
#Dictionaries
#New code, length of dictionary
student = {'first_name':'Brian', 'gender':21,'marital status':'single','skils':'smart'}
print(len(student))

#Accesing dictionary
#you call out the key of the value you want to access
student = {'first_name':'Brian', 'gender':21,'marital status':'single','skils':'smart'}
print(student['skils'])

#converting to list, use (keys()) or values()
#Get the dictionary keys as a list
student = {'first_name':'Brian', 'gender':21,'marital status':'single','skils':'smart'}
keys = student.keys()
print(keys)