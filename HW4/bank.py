# takes two 2d arrays and subtracts them from one another (a - b)
def sub2d(a,b):
	if (len(a) != len(b)):
		print "Error lists are not the same size"
	elif (len(a[0]) != len(b[0])):
		print "Error lists are not the same size"
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
		print "Error lists are not the same size"
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
		print "Error lists are not the same size"
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
		print "Error lists are not the same size"
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
	
def updating(process, request):
	global available
	global max
	global allocation
	global need
	
	available = sub1d(available, request)
	allocation[process] = add1d(allocation[process], request)
	need[process] = sub1d(need[process], request)
	
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
			updating(process, request)
			
			# step 4
			saftey()
		else:
			print "Wait"
	else:
		print "ERROR: Exceeds Needs"
		
def safteyCheck(work, finish):
	i = 0
	while(i<0):
		if(finish[i] != False):
			i += 1
		else:
			if(lessThan(need[i], work):

	return work, finish
	
def saftey():
	global available
	global max
	global allocation
	global need
	
	work = available
	# takes the length of max to determine how many jobs there are
	finish = 	[False for x in range(len(max)]
	# will be used to compare with finish to tell if all processes have finished
	doneArray = [True for x in range(len(max)]
	
	done = False
	
	while(!done):
		work, finish = safteyCheck(work, finish)
		
		done = lessThan(doneArray, finish)
	
	

available = 	[10,5,7]
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

bankers(p0, p1_request)
