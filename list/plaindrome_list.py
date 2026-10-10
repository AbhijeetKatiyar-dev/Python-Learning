# (This code is for checking whether the list is a palindrome or not)
list=[]
lis1=list.append(input("Enter your 1st element:"))
lis2=list.append(input("Enter your 2nd element:"))
lis3=list.append(input("Enter your 3rd element:"))
lis4=list.append(input("Enter your 4th element:"))
lis5=list.append(input("Enter your 5th element:"))
rev=list.copy()
rev.reverse()
if list==rev:
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")   
