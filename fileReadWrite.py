fw=open("test.txt",'w')
fw.write("this is from newboston\n")
fw.write("hi, i am tejas")
fw.close()

fr=open("test.txt",'r')
text= fr.read()
print(text)
fr.close()