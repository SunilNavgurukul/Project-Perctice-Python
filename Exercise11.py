users=int(input("Enter the any number"))
for x in (2,users):
	if users%x:
		print("It is not prime number ")
		break
else:
	print("It is a prime number")