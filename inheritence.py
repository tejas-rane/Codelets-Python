
class Pet:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def talk(self):
        raise NotImplementedError("subclass must implement absrtact method")
class Cat(Pet):
    def __init__(self,name,age):
        super().__init__(name, age)
        
    def talk(self):
        return "Meowww"
class Dog(Pet):
    def __init__(self,name,age):
        super().__init__(name,age)
    def talk(self):
        return "woofff"
        
def Main():
    thepet=Pet("Pet",1)
    jess = Cat("jess",3)
    
    print("is jess a cat? " + str(isinstance(jess, Cat)))
    print("is jess a pet? " + str(isinstance(jess, Pet)))
    print("is thepet a Cat? " + str(isinstance(thepet, Cat)))
    print("is thepet a Pet? " + str(isinstance(thepet, Pet)))
    
    pets = [Cat("jess",3), Dog("jack", 5), Cat("fred", 4),Pet("thepet",9)]
    
    for pet in pets:
        print("Name: "+pet.name +" age "+str(pet.age) + " says "+pet.talk())
    
if __name__=='__main__':
    Main()