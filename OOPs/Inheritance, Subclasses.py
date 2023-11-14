class Employee:
    
    retirementAge = 60
    
    def __init__(self,name,surname, age):
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


# Put the Parent class in parenthesis to specify which class to inherit from
# This is inherits all the class methods and class variables as well.
class Developer(Employee):
    def __init__(self, name, surname, age, lang):
        super().__init__(name, surname, age) 
        # This will inherit all the attributes from the parent class by super().__init__
        self.lang = lang
        # As usual get the extra attribute like usual
        
    
    def job(self):
        print(f"{self.name} is a {self.lang} developer")

me = Developer('Abhishek', 'Kumar', 24, 'python')

me.retirement()

me.job()

