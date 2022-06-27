# txt = "I am an automation tester"
#
# # setting the maxsplit parameter to 1, will return a list with 2 elements!
# x = txt.split()
#
# print(x)
# # x.reverse()
# print(x)
# print(type(x))
# # str= x[0]
# y = []
# for i in range(0, len(x)):
#     new_x = x[i][::-1]
#     y.append(new_x)
# print(y)
# print(' '.join(y))
# print(' '.join(x))
#


# # FIBBO
# n= 10
# n1,n2=0,1
#
# for i in range(0,n+1):
#     print(n1)
#     num=n1+n2
#     n1=n2
#     n2=num

# Factorial
# n=5
# fact=1
# for i in range(1,n+1):
#     fact= i*fact
# print(fact)

# #Pallindrome number
# num= 1234321
# print(type(num))
# str1= str(num)
# num1 =int(str1[::-1])
# if num1==num:
#     print("{} is pallindrome number".format(num))
# else:
#     print("{} is not pallindrome number".format(num))
#

num=1234
temp=0
for i in str(num):
    temp=temp+int(i)
print(temp)