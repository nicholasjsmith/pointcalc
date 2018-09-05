tot = raw_input('Number of Points? ') #presumably everything is waited the same
tot = int(tot)
half = raw_input('Half points? yes/no ') #please to god just use yes or no
#sorry if you want more than half points
wrong = 0.0 
counter = tot
while counter > 0:
	print '%4.1f Wrong, %4.1f/%i, Score of %3i' %(wrong,counter,tot,round(counter/tot*100))
	if half == 'yes':
		counter += -0.5
		wrong += 0.5
	else:
		counter += -1.0
		wrong += 1.0
#this could be more efficient but i didn't want to do a lot of math
