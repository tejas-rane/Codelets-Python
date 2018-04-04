class Mario:
    def move(self):
        print("moving")
class Shroom():
    def eatShroom(self):
        print("shroom")

class BigMario(Mario,Shroom):
    pass #nothing to write

bm = BigMario()
bm.move()
bm.eatShroom()