H=int(input('請輸入身高'))
W=int(input('請誠實輸入體重'))
Z=int(input('想賺多少錢'))
if H >= 150:
	print("蠻高的喔", '身高', H)
if H < 150:
	print("該墊腳尖了", '身高', H, 'cm')
if W > 100:
	print("該減肥了", '體重', W, '公斤')
if W == 100:
	print("超人體重",'體重', W, '公斤')
if W < 100:
	print("該多吃點了",'體重', W, '公斤')
if Z > 10000:
	u = input("賺這樣就夠了嗎?")
	if u == "不夠":
		print("身價", Z*100,"別太貪心阿")
	if u != "不夠":
		print("負債", Z*100, "該奮鬥了")
if Z == 10000:
	print("恭喜中頭獎")
if Z < 10000:
	print("看你可憐", Z*10)