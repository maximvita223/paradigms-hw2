def is_valid(x,y,maze):
    if x < 0 or y < 0 or x >= len(maze) or y >= len(maze[0]):
        return False
    if maze[x][y] == '1':
        return False
    return True

def wave_algoritm(maze, start, end):

    queue = [start]
    visited = set()
    visited.add(start)
    width = len(maze)
    height = len(maze[0])


    while queue:
        x, y, dist = queue.pop(0)

        if (x,y) == end:
            return dist
        

        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            new_x, new_y = x + dx, y + dy

            if is_valid(new_x, new_y, maze) and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                queue.append((new_x, new_y, dist + 1))

    return -1

maze = [['0','1','1','1','1','1','0'],
        ['0','1','0','0','0','1','0'],
        ['0','1','0','1','0','1','0'],
        ['0','0','0','1','0','0','0']]


start = (0,0,0)
end = (1,6)

dist = wave_algoritm(maze, start,end)

print(dist+2) # Расстояние до конца лабиринта