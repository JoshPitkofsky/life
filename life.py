#An extremely nieve implementation of conway's game of life

#create grid to be passed in with initial state
grid = [[|,|,|,|,|,|,|,|,|,|,|],
		[|,+,|,|,|,|,|,|,|,|,|],
		[|,|,+,|,|,|,|,|,|,|,|],
		[|,|,+,|,|,|,|,|,|,|,|],
		[|,|,+,|,|,|,|,|,|,|,|],
		[|,|,|,|,|,|,|,|,|,|,|],
		[|,|,|,|,|,|,|,|,|,|,|]]

#need to keep track of number of neighbors that are active at each tick
def replace_with_neighborCount(grid)