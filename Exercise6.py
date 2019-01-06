name = input("Enter your name:)\n ")
i=len(name)
a=""
while i>0:
	i-=1
	a+=name[i]
if name==a:
	print("That is Palindrome")
else:
	print("That is not")

