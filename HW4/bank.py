def sub(a,b):
	if (len(a) != len(b)):
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
	
def bankers(request):
	global available
	global max
	global allocation
	global need

available = 	[10,5,7]
max = 			[[7,5,3], [3,2,2], [9,0,2], [2,2,2], [4,3,3]]
allocation = 	[[0,1,0], [2,0,0], [3,0,2], [2,1,1], [0,0,2]]
need = sub(max, allocation)

#process shortcuts
p0 = 0
p1 = 1
p2 = 2
p3 = 3
p4 = 4

#resource shortcuts
A = 0
B = 1
C = 2

p1_request = [1,0,2]
