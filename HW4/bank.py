import sys
from inspect import currentframe, getframeinfo
debug = True
# takes two 2d arrays and subtracts them from one another (a - b)
def sub2d(a,b):
	if (len(a) != len(b)):
		sys.exit("ERROR: Lists are not the same size. Code A line {}".format(getframeinfo(currentframe()).lineno))
	elif (len(a[0]) != len(b[0])):
		sys.exit("ERROR: Lists are not the same size. Code B line {}".format(getframeinfo(currentframe()).lineno))
	else:
		rows = len(a)
		columns = len(a[0])
	
		answer = [[0 for x in range(columns)] for y in range(rows)]
		i = 0
		j = 0
		
		while(i<rows):
			j = 0
			while(j<columns):
				answer[i][j] = a[i][j] - b[i][j]
				j += 1
			i += 1

		return answer
	
# takes two 1d arrays and subtracts them from one another (a - b)
def sub1d(a,b):
	if (len(a) != len(b)):
		sys.exit("ERROR: Lists are not the same size. Code C line {}".format(getframeinfo(currentframe()).lineno))
	else:
		rows = len(a)
		
		answer = [0 for x in range(rows)]
		
		i = 0
		result = True
		
		while(i<rows):
			answer[i] = a[i] - b[i]
			i += 1
		return answer
		
# takes two 1d arrays and adds them from one another
def add1d(a,b):
	if (len(a) != len(b)):
		sys.exit("ERROR: Lists are not the same size. Code D line {}".format(getframeinfo(currentframe()).lineno))
	else:
		rows = len(a)
		
		answer = [0 for x in range(rows)]
		
		i = 0
		result = True
		
		while(i<rows):
			answer[i] = a[i] + b[i]
			i += 1
		return answer

# checks to see if A's values are less than or equal to B's values, for a 1d array (a <= b)
def lessThan(a,b):
	if (len(a) != len(b)):
		sys.exit("ERROR: Lists are not the same size. Code E line {}".format(getframeinfo(currentframe()).lineno))
	else:
		rows = len(a)
		
		i = 0
		result = True
		
		while(i<rows):
			if (a[i] <= b[i]):
				i += 1
			else:
				return False
		return True
	
# it updates the arrays: available, allocation, and need, with the process's request
def updatingBankers(process, request, available, allocation, need):
	available = sub1d(available, request)
	allocation[process] = add1d(allocation[process], request)
	need[process] = sub1d(need[process], request)
	
	return available, allocation, need
	
# runs the bankers algorithm
def bankers(process, request):
	global available
	global max
	global allocation
	global need
	
	# step 1
	if (lessThan(request, need[process])):
		# step 2
		if (lessThan(request, available)):
			# step 3
			available, allocation, need = updatingBankers(process, request, available, allocation, need)
			
			# step 4
			saftey(available, allocation, need)
		else:
			sys.exit("Wait. Request is larger than available. Code G")
	else:
		sys.exit("ERROR: Exceeds Needs. Code F line {}".format(getframeinfo(currentframe()).lineno))
		
# Step 3 of Safety: updates the work and finish arrays
def updatingSafety(work, finish, allocation, process):
		work = add1d(work, allocation[process])
		finish[process] = True
		return work, finish

# this is the second step of the safety algorithm: it 
def safteyCheck(work, finish, allocation, need):
	i = 0
	# it takes the length of allocation to find the number of process
	while(i<len(allocation)):
		# if job is finished then go to next
		if(finish[i] != False):
			i += 1
		else:
			if(lessThan(need[i], work)):
				print "p{}".format(i)
				# step 3 of safety
				work, finish = updatingSafety(work, finish, allocation, i)
			i += 1

	return work, finish
	
def saftey(available, allocation, need):	
	
	work = available
	# takes the length of allocation to determine how many jobs there are
	finish = 	[False for x in range(len(allocation))]
	# will be used to compare with finish to tell if all processes have finished
	doneArray = [True for x in range(len(allocation))]
	
	done = False
	
	# loops until all process are finished
	while(done == False):
		# step 2
		work, finish = safteyCheck(work, finish, allocation, need)
		
		# uses the equals too part of lessThan to check if all process are finished
		done = lessThan(doneArray, finish)
	
	

available = 	 [3,3,2]
max = 			[[7,5,3], [3,2,2], [9,0,2], [2,2,2], [4,3,3]]
allocation = 	[[0,1,0], [2,0,0], [3,0,2], [2,1,1], [0,0,2]]
need = sub2d(max, allocation)

# process shortcuts
p0 = 0
p1 = 1
p2 = 2
p3 = 3
p4 = 4

# resource shortcuts
A = 0
B = 1
C = 2

p1_request = [1,0,2]

bankers(p1, p1_request)