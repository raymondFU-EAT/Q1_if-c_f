z = []
count = 0
with open ("reviews.txt", "r") as f: # 把檔案開啟並且取檔案,更把檔案列命名為f
	for line in f: # 把f中的訊息每一行取名為line
		z.append(line) # 把讀取到所有line丟入z倉庫中
		count += 1
		if count % 10000 == 0:
			print(len(z))
		
print(len(z)) # 印出一條條line的長度
print(z[0]) # 印出第一條資料
print("...............")
print(z[1])