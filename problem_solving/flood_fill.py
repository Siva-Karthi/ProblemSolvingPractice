
def validate_helper(next_pixel, m , n , prev_colour, new_colour, screen):
	x, y = next_pixel
# 	print("next_pixel", next_pixel, x, y, m,n)
	if (x < 0) or (y<0) or (x>=m) or (y>=m) or screen[x][y] != prev_colour or  screen[x][y] == new_colour:
		return False
	return True
	

def flood_fill(screen, m , n, x, y, prev_colour, new_colour):
	queue = []
	queue.append([x,y])
	screen[x][y] == new_colour
	while queue:
		current = queue.pop()
		x, y = current
		right = [x +1,y]
		left = [x-1,y]
		up = [x,y-1]
		down = [x,y+1]

		if validate_helper(right, m , n , prev_colour, new_colour, screen):
			screen[x+1][y] = new_colour
			queue.append(right)
		if validate_helper(left, m , n , prev_colour, new_colour, screen):
			screen[x-1][y] = new_colour
			queue.append(left)
		if validate_helper(up, m , n , prev_colour, new_colour, screen):
			screen[x][y-1] = new_colour
			queue.append(up)
		if validate_helper(down, m , n , prev_colour, new_colour, screen):
			screen[x][y+1] = new_colour
			queue.append(down)
	for i in screen:
# 		for j in screen[i]:
# 			print(screen[i][j], end="")
		print(i)
	

screen =[
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 0, 0],
[1, 0, 0, 1, 1, 0, 1, 1],
[1, 2, 2, 2, 2, 0, 1, 0],
[1, 1, 1, 2, 2, 0, 1, 0],
[1, 1, 1, 2, 2, 2, 2, 0],
[1, 1, 1, 1, 1, 2, 1, 1],
[1, 1, 1, 1, 1, 2, 2, 1],
    ]
     
# Row of the display
m = len(screen)
 
# Column of the display
n = len(screen[0])
 
# Co-ordinate provided by the user
x = 4
y = 4
 
# Current color at that co-ordinate
prevC = screen[x][y]
 
# New color that has to be filled
newC = 3
 
flood_fill(screen, m, n, x, y, prevC, newC)
