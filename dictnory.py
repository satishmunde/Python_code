dict={
    "satish": "This is a coder",
    "DOB": "26 jan 2002",
    "dict1": {"passion": "Being a hacker",
           "marks": 98
           }
 
 }
print(dict['satish'])
print(dict.get('DOB'))
print(dict['dict1']['passion']) #nested dictonary acess
print(dict.get('marks'))
dict['marks']=[10,20,30,40,50]
print(dict.get('marks'))
print(type(dict.keys()))
print(dict.keys())
print(dict.values())
print(dict.items())
newdict={
    "Satish": "Munde",
    "satish": "He is a Cracker"
}
dict.update(newdict) #it will update already existing value
print(dict)

print(dict.get('Sattu0'))
print(dict['Sattu0'])