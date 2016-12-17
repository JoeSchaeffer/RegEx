import re

fhand = open("Example.txt")
count = 0
find = 0
snum = 0
num = []

for line in fhand:
	find = re.findall("([0-9]+)", line)

	if len(find) >= 1:
		for i in find:
			num.append(int(i))
		find = num
		snum = sum(num)
		count = count + 1
	
	



print "There are",count,"values and the sum =",snum

	
print num

