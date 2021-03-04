password = "13579"
u = 3 # 剩餘機會
while True:
	p = input("請輸入密碼")
	if p == password:
		print("密碼成功")
		break
	else:
		u = u - 1
		print("密碼錯誤", "剩", u, "次機會")
		if u == 0:
			break