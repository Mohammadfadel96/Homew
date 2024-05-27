# If you have two lists, L1=[‘HTTP’,’HTTPS’,’FTP’,’DNS’] L2=[80,443,21,53],
# convert it to generate this dictionary d={‘HTTP’:80,’HTTPS’:443,’FTP’:21,’DNS’:53}
l1 = ['HTTP','HTTPS','FTP','DNS']
l2 = [80,443,21,53]
d = dict(zip(l1,l2))
print(d)

# Write a Python program that calculates the factorial of a given number entered by user.
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter a number to find it's factorial\n"))
fact_n=fact(n)
print(f"the factorial of {n} is: {fact_n}")

# L=[‘Network’ , ’Bio’ , ’Programming’, ‘Physics’ , ‘Music’]
# In this exercise,you will implement a Python program that reads the items of the previous list
# and identifies the items that starts with ‘B’ letter,then print it on screen.
# Tips: using loop, len() , startswith() methods.
l = ['Network','Bio','Programming','Physics','Music']
for i in range (0,len(l)):
    if l[i].startswith('B'):
        print(l[i])

# Using Dictionary comprehension, Generate this dictionary d={0:1,1:2,2:3,3:4,4:5,5:6,6:7,7:8,8:9,9:10,10:11}
d = {x:x+1 for x in range(11)}
print(d)


