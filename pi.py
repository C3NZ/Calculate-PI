digits = int(raw_input("How many times do you want to want to carry out the series?"))

def pi(digits):
	piv = 3 #initial value of pi before the series actually starts
	counter = 1 #counts the cycles of the loop, also used to determine whether addition or subtraction is done in the series
	increment = 2 #increments used in the denominator of the series
	for x in xrange(counter, digits):
		if counter % 2 != 0:
			 piv += (4.0 / (increment * (increment + 1) * (increment + 2))) 
		elif counter % 2 == 0: 
			 piv -= (4.0 / (increment * (increment + 1) * (increment + 2)))
		increment += 2		
		counter += 1
		
	return piv


print(pi(digits))