import random
r = random.randint(1, 100)
nu = 0
while True:	
	s = input("請猜數字")
	s = int(s)
	nu += 1 # nu = nu + 1
	if s == r:
		print("猜對瞜")
		print("總共猜了", nu, "次")			
		break
	elif s > r:
		print("再小一點")
	elif s < r:
		print("再大一點")
	print("總共猜了", nu, "次")