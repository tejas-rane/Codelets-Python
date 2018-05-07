def Solution(ax,ay,bx,by):
    xd=bx-ax
    yd=by-ay
    cor=""


    if xd==0: #travellign vert
        if yd>0:
            cor=str(bx+1)+","
            cor = cor+str(by)
        elif yd<0:
            cor = str(bx - 1) + ","
            cor = cor + str(by)
        return cor

    if yd==0:
        if xd>0:
            cor=str(bx)+","
            cor = cor+str(by-1)
        elif xd<0:
            cor = str(bx) + ","
            cor = cor + str(by+1)
        return cor

    slope = (by - ay) / (bx - ax)
    print "slope:", slope
    if slope >0:
        cor = str(bx+1) + ","
        cor = cor + str(by - 1)

    else:
        cor = str(bx - 1) + ","
        cor = cor + str(by - 2)
    return cor


print Solution(2,2,2,-3)
print Solution(-1,3,3,1)
# print Solution(2,2,2,-3)
# print Solution(2,2,2,-3)