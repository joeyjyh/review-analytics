data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 1000 == 0:  #用來求餘數
			print(len(data))
print('檔案讀取完畢, 總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('留言平均長度是', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '比留言長度小於100')
print(new[0])
print(new[1])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '比留言提到good')

# 快寫版
bad = [d for d in data if 'bad' in d]

#文字計數

wc = {}

for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))

while True:
	word = input('請輸入想查詢的單字: ')
	if word == 'q':		
		break
	elif word in wc:
		print(word, '出現的次數為: ', wc[word])
	else:
		print('查無此單字')
print('感謝使用本功能')


