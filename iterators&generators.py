class Reverse:
    def __init__(self,data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        
        if self.index == 0:
            raise StopIteration
        self.index = self.index -1
        return self.data[self.index]

def reverse(data):
    print("from method using yeild")
    for index in range(len(data)-1,-1,-1):
        yield data[index]
    
    
def Main():
   
    #print(rev.data)
    print("from reverseString method")
    rev1 = Reverse("ABCDEFGH")
    for char in rev1:
        print(char )
        
    rev = Reverse("ABCDEFGH")
    print("from __next__ ")
    for char in rev:
        print(char )
    
    data = "ABCDEFGH"
    print("from inline generator")
    print(list(data[i] for i in range(len(data)-1,-1,-1)))
        
if __name__=='__main__':
    Main()   