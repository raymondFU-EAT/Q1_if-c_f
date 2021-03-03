driver = input("請問有開過車嗎?")


age = int(input("請問年齡?"))
if driver == "有":
	if age <= 18:
		print("違法喔")
	if age > 18:
		print("測驗成功")
elif driver =="沒有":
	if age <= 18:
		print("過幾年就能考摟")
	if age > 18:
		print("該考個駕照瞜")
else:
	print("請輸入有或沒有")

