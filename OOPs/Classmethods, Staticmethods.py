class Stack:
    
    retirementAge = 60
    
    def __init__(self,name,surname, age):
        # These are the parameters of the object created
        self.name = name
        self.surname = surname
        self.age = age
    
    def fullName(self):
        print(f"{self.name} {self.surname} is your full name.")
    
    def vote(self):
        if self.age>=18:
            print("You can vote you are "+str(self.age))
        else:
            print("You can't vote sorry")
    
    def retirement(self):
        print(f"{self.retirementAge-self.age} years till retirement!")


#---------------------------------------------

me = Stack("Abhishek", "Kumar", 24)
friend = Stack("Satyam", "Raj", 24)