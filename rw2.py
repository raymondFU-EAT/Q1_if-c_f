count = 0
data = []
with open("reviews.txt", "r") as f: 
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))
print("收尋資料總共為", len(data), "筆資料")
number = 0
for count_1 in data:
	number = number + len(count_1)
print("每行資料平均為", number/len(data), "個字")

