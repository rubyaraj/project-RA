import sys

sum=0
n=0

# su input values
# second change
for num in open('data.txt'):
	sum += float(num)
	n += 1

print sum/n

