#An extremely nieve implementation of conway's game of life

#create grid to be passed in with initial state
grid = [['|','|','|','|','|','|','|','|','|','|','|'],
		['|','|','|','|','|','|','|','|','|','|','|'],
		['|','|','+','|','|','|','|','|','|','|','|'],
		['|','|','+','|','|','|','|','|','|','|','|'],
		['|','|','+','|','|','|','|','|','|','|','|'],
		['|','|','+','|','|','|','|','|','|','|','|'],
		['|','+','|','|','|','|','|','|','|','|','|'],
		['|','|','|','|','|','|','|','|','|','|','|'],
		['|','|','|','|','|','|','|','|','|','|','|'],
		['|','|','|','|','|','|','|','|','|','|','|'],
		['|','|','|','|','|','|','|','|','|','|','|'],]

#in order to count up neighbors lets convert grid to 1s and 0s. 
#(I recognize this would have been easier with 1s and 0s as the grid itself but this looks cooler)

def convert_to_bool(grid):
	rows = len(grid)
	cols = len(grid[5])
	for row in range(rows):
		for col in range(cols):
			if grid[row][col] == "|":
				grid[row][col] = 0
			else:
				grid[row][col] = 1 

#need to keep track of number of neighbors that are active at each tick
def grid_with_neighborCount(grid):
	grid = convert_to_bool(grid)
	rows = len(grid) #set rows to be the number of lists in master list
	cols = len(grid[5]) #set cols to be the number of items in a given row (this should be the same for each row, I should add check to iterate over rows and make sure they all contain the same number of elements)

	NeighborCount = [] #this will soon contain the number of live neighbors that each cell has
	NeighborCount=[[0,] * cols for row in range (rows)] #found a cool list comprehension to help make a 0 matrix (https://docs.python.org/2/tutorial/datastructures.html)
	x=len(NeighborCount)
	y=len(NeighborCount[5])

	for row in range(rows):
		for col in range (cols):
			NeighborCount[x][y] = grid[]

convert_to_bool(grid)
grid_with_neighborCount(grid)
