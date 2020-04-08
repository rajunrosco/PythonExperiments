import sys

for i in range(0,100):
	for j in range(0,500000):
		wait = True
	sys.stdout.write("count: %d \r" % i)
	# sys.stdout.flush()