date, name, price = ['december, 18','tejas',50]

print(date)
print(name)
print(price)


def drop_f_l(grades):
    first, *middle, last = grades

    avg = sum(middle)/len(middle)
    print(avg)


drop_f_l([65,6,7,8,3,2,90])