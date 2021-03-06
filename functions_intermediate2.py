# 1.  Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ]. *DONE
# Change the last_name of the first student from 'Jordan' to 'Bryant' *DONE
# In the sports_directory, change 'Messi' to 'Andres' *DONE
# Change the value 20 in z to 30 *DONE
x[1][0] = 15
print(x)
students[0] ['last_name']='Bryant'
print(students)
sports_directory['soccer'][0]='Andres'
print(sports_directory)
z[0]['y']=30
print(z)


# 2.  Iterate Through a List of Dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
def iterateDictionary(name_list):
    for student in name_list:
        output = ""
        for key, value in student.items():
            output+= f"{key} - {value}, "
        print(output)
print(iterateDictionary(students)) 




# 3. Get Values From a List of Dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# Create a function iterateDictionary2(key_name, some_list)
# that, given a list of dictionaries and a key name,
# the function prints the value stored in that key for each dictionary.
# For example, iterateDictionary2('first_name', students) should output:
# Michael
# John
# Mark
# KB
def iterateDictionary2(key_name, name_list):
    for student in name_list:
        print(student['first_name'])
print(iterateDictionary2('first_name',students))
# And iterateDictionary2('last_name', students) should output:
# Jordan
# Rosales
# Guillen
# Tonel
def iterateDictionary2(key_name, name_list):
    for student in name_list:
        print(student['last_name'])
print(iterateDictionary2('last_name',students))


# 4.  Iterate Through a Dictionary with List Values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo_list):
    for key, value in dojo_list.items():
        print(f"{len(value)} {key.upper()}")
        for x in value:
            print(x)
print(printInfo(dojo))

# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon


