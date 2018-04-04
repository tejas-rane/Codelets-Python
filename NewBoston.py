def unpack(age,apples_ate,cigs):
    total = age+apples_ate+cigs
    print(total)

unpack(2,3,4)

list = [2,3,7]
unpack(list[0],list[1],list[2])
unpack(*list)  #unpacks automatically
