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

#need to keep track of number of neighbors that are active at each tick
def replace_with_neighborCount(grid):
	rows = len(grid) #set rows to be the number of lists in master list
	cols = len(grid[5]) #set cols to be the number of items in a given row (this should be the same for each row, I should add check to iterate over rows and make sure they all contain the same number of elements)

	NeighborCount = [] #this will soon contain the number of live neighbors that each cell has
	NeighborCount=[[0,] * cols for row in range (rows)]
	print NeighborCount

replace_with_neighborCount(grid)
