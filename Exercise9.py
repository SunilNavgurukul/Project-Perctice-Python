import random
user=int(input("Enter the your input:)\n"))
num = random.randint(1,10	)
print(num)
if user==num:
	print("Exactly right")
if user<num:
	print("too short")
else:
	print("Too high")