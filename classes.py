class MyClass:
    number = 0
    name = "NoName"
    
def Main():
    me = MyClass()
    me.number=1020
    me.name="tejas"
    
    friend = MyClass()
    friend.name="Roy"
    friend.number=12234
    
    empty = MyClass()
    print("name: " + me.name + ", Fav No: "+str(me.number))
    print("name: " + friend.name + ", Fav No: "+str(friend.number))
    print("name: " + empty.name + ", Fav No: "+str(empty.number))
    
if __name__=='__main__':
    Main()