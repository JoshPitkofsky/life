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

#in order to count up neighbors lets convert grid to 1s and 0s. 
#(I recognize this would have been easier with 1s and 0s as the grid itself but this looks cooler)

# def convert_to_cool(grid):
# 	rows = len(grid)
# 	cols = len(grid[5])
# 	for row in range(rows):
# 		for col in range(cols):
# 			if grid[row][col] == 0:
# 				grid[row][col] = 's'
# 			else:
# 				grid[row][col] = 'T' 
# 	return grid

#need to keep track of number of neighbors that are active at each tick
def grid_with_neighborCount(grid):
	#set rows to be the number of lists in master list
	rows = len(grid) 
	 #set cols to be the number of items in a given row 
	 #(this should be the same for each row, I should add check to iterate over rows and make sure they all contain the same number of elements)
	cols = len(grid[5])

	#this will soon contain the number of live neighbors that each cell has
	NeighborCount = [] 
	#found a cool list comprehension to help make a 0 matrix (https://docs.python.org/2/tutorial/datastructures.html)
	NeighborCount=[[0,] * cols for row in range (rows)] 

	#Might need a buffer (rows-1) (cols-1), we'll see if i can figure out infinite or at least make it wrap around
	for row in range(1,rows-1):
		for col in range (1,cols-1):
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
		for row in range(1,rows-1):
			for col in range(1,cols-1):
				#if the cell is alive and has either fewer than 2 or greater than 3 active neighbors, kill it
				if grid[row][col] == 1 and NeighborCount[row][col]<2 or NeighborCount[row][col]>3:
					grid[row][col] = 0
				#if the cell is dead but has 3 active neighbors. revive it
				elif grid[row][col] == 0 and NeighborCount[row][col] == 3:
					grid[row][col] = 1
		display(grid)
		i+=1
		time.sleep(.1)
		print(chr(27) + "[2J")

iterate(grid,2700)


