import random
r = random.randint(1, 100)
while True:
	s = input("請猜數字")
	s = int(s)
	if s == r:
		print("猜對瞜")
		break
	else:
		if s > r:
			print("再小一點")
		if s < r:
		    print("再大一點")
