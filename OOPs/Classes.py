# This is how you define a class, 
class Stack:
    # self, is the instance itself, it is default there
    # Because whenever you call a class, an instance (object) is always created , that is 'self'
    # Apart from that all the others are arguments
    
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



# Create an instance by calling the class and passing in the arguments
me = Stack("Abhishek", "Kumar", 24)
friend = Stack("Satyam", "Raj", 24)


print(me) # This prints the location of the object itself
print(friend)

# Print the individual attributes

# print(me.name)
# print(me.surname)
# print(me.age)
# print()
# print(friend.name)
# print(friend.surname)
# print(friend.age)

print(me.__dict__) # This prints all the attributes available in the instance
print(me.__class__) # Prints which class is this instance is made of

# It inherits the variable from the class
print(me.retirementAge)

me.retirementAge = 70

print(me.__dict__)

me.fullName()

me.vote()

me.retirement()

