#An extremely nieve implementation of conway's game of life
import time
#create grid to be passed in with initial state
grid = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		]

#need to keep track of number of neighbors that are active at each tick
def grid_with_neighborCount(grid):
	#set rows to be the number of lists in master list
	rows = len(grid) 
	 #set cols to be the number of items in a given row 
	 #(this should be the same for each row, I should add check to iterate over rows and make sure they all contain the same number of elements)
	cols = len(grid[5])

	#this will contain the number of live neighbors that each cell has
	NeighborCount = [] 
	#found a cool list comprehension to help make a 0 matrix with same dimensions of grid(https://docs.python.org/2/tutorial/datastructures.html)
	#If cols is 6 then [0,] * cols generates [0,0,0,0,0,0] and it does this for i in range rows
	NeighborCount=[[0,] * cols for row in range (rows)] 

	#ignore buffer
	for row in range(1,rows-1):
		for col in range (1,cols-1):
			#count the number of active cells around each cell 
			#if neighborhood of x was:
			#     000
			#     1x0
			#	  000
			# then x should be set to 1	
			NeighborCount[row][col] = grid[row-1][col-1]+grid[row][col-1]+grid[row+1][col-1]\
									+grid[row-1][col]					+grid[row+1][col]\
									+grid[row+1][col+1]+grid[row][col+1]+grid[row-1][col+1]
	return NeighborCount

#for each row excluding the first and last
#print each cell except the first and last in the list
#(chop off buffer)
def display(grid):
	for row in grid[1:-1]:
		print row[1:-1]

def iterate(grid, iterations):
	rows = len(grid)
	cols = len(grid[5])
	i=0
	while i != iterations:
		#call neighborcount() on the grid so we can use the number of neighbors in our logic
		NeighborCount = grid_with_neighborCount(grid) 
		#ignore the buffer
		for row in range(1,rows-1):
			for col in range(1,cols-1):
				#if the cell is alive and has either fewer than 2 or greater than 3 active neighbors, kill it
				if grid[row][col] == 1 and (NeighborCount[row][col]<2 or NeighborCount[row][col]>3):
					grid[row][col] = 0
				#if the cell is dead but has 3 active neighbors, revive it
				elif grid[row][col] == 0 and NeighborCount[row][col] == 3:
					grid[row][col] = 1
		display(grid)
		#increment counter
		i+=1
		#pause
		time.sleep(0.1)
		#clear screen, was going to try to use a carriage return but couldn't figure out how to do that on multiple lines
		print(chr(27) + "[2J") 

iterate(grid,2700)


