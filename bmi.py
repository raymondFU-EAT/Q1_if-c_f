h = input ("請輸入身高(cm)")
w = input ("請輸入體重(kg)")
h = int (h)
w = int (w)
h = h / 100
b = w / h / h
if b < 18.5:
    print("BMI", b, "體重過輕")
elif b <= 18.5 and b < 24:
    print("BMI", b, "正常範圍")
elif b >= 24 and b <27:
    print("BMI", b, "過重")
elif b >= 27 and b <30:
    print("BMI", b, "輕度肥胖")
elif b >= 30 and b <35:
    print("BMI", b, "中度肥胖")
else :
    print("BMI", b, "重度肥胖")