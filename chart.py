import matplotlib.pyplot as plt
from collections import Counter
with open('data.txt') as f:
    lst = f.read().splitlines()
data = []
for line in lst :
    data.append(line.split('|')[1])
count = Counter(data)

bars = plt.bar(count.keys(), count.values())
plt.title("Số lần xuất hiện của các giá trị trong mảng")
plt.xlabel("Giá trị")
plt.ylabel("Số lần xuất hiện")
plt.xticks(rotation=20, fontsize=8)  # Xoay nhãn 45 độ và giảm kích thước font

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, str(yval), ha='center', va='bottom', fontsize=8)  

plt.show()
