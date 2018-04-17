# import urllib2
# url = 'http://www.sap.com/belgique/index.html'
# response = urllib2.urlopen(url)
# page = response.read()
# page = page.replace('SAP', 'Odoo')
# f = open("test.html", "wb")
# f.write(str(page))
# f.close()
# print page
#
# class Solution:
#     def rec_sum(self,res,arr,index):
#         if index == len(arr):
#             return res
#         else:
#             if arr[index].isdigit():
#                 res += int(arr[index])
#             return self.rec_sum(res,arr, index+1)
#
# res = 0
# arr = ["hghgsdh", "100", "hhc", "1", "wee", "19"]
# index = 0
# print Solution().rec_sum(res,arr,index)
# def onCondition():
#     for i in range(1,99):
#         if i %3 ==0 and i % 7 == 0:
#             print "OpenSource"
#         elif i%7 == 0:
#             print "Source"
#         elif i %3 ==0 :
#             print "Open"
#         else:
#             print i
# onCondition
# import re
# p = re.compile('\bjack\b.*\bjames\b|\bjames\b.*\bjack\b')
# line = "this is james and jack goiing asmhqdqn"
# print p.match(line)
fo = open("in.txt", "rb+")
line = fo.readline()
print line
line = fo.readline()
print line
line = fo.readline()
print line
fo.close()

