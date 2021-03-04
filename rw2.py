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

new = []
for d in data:
	if len(d) < 100:
		new.append(data)
print("總共有", len(new), "筆資料")

good = [] # 設一個資料夾為good
for e in data: # 從data中找出我要的資料e
	if "good" in e: # 如果我找到的資料中有字串good
		good.append(data) # 把找到的字串放入設的資料夾good中
print("總共有",len(good),"好的留言")

good = [e for e in data if "good" in e] # 設立一個Good的資料夾,把有good留言的各條資料從data中找出
print(len(good))
new = [d for d in data if len(d) < 100] # 設立一個New的資料夾,把所有留言少於100字的資料找出來
print(len(new))
