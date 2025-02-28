import json

class Person(object):
    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email

class Student(Person):
    def __init__(self,name,age,email,studentid):
        super().__init__(name, age, email)
        self.studentid = studentid

    def to_dict(self): 
        return {       
            'name' : self.name,
            'age' : self.age,
            'email' : self.email,
            'studentid' : self.studentid
        }
    
class Saver(object):
    def save(data, filename = 'studentnew.json'):
        with open(filename, 'w') as f:  
            json.dump(data,f, indent=4) 

student = Student('Jayvee', 25,'jmbonus@cpp.edu', 305983)

filename = 'student.json'
with open('student.json', 'w') as f:
    json.dump(student.to_dict(), f, indent=4)

with open('student.json') as f:
    data_classes = json.load(f)
    print (json.dumps(data_classes, indent=2))