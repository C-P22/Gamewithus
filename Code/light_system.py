from icecream import ic
from config import *
def path_finder(y,x,tiles,maze_matrix,visited):
    #ic(y,x)
    visited[y][x] = 'T' 
    if maze_matrix[y][x] == 'E':
        #ic(x,y)
        return True, tiles
    neighbors = [[y - 1, x], [y + 1, x], [y, x + 1], [y, x - 1]]
    for neighbor in neighbors:  # Iterate over a copy of the list

        y_now, x_now = neighbor
        if maze_matrix[y_now][x_now] != 'X'and visited[y_now][x_now] == 'f'  :
            tile = tiles.copy()
            tile.append(neighbor)
            x, end_tiles = path_finder(y_now,x_now,tile,maze_matrix,visited)
            #ic(x)
            if x:
                return True, end_tiles
    return False, False
            
def light_paht(maze_matrix,player_pos):
    position_x,position_y = player_pos

    visited = [['f' for _ in range(len(maze_matrix))] for _ in range(len(maze_matrix[0]))]
    light_value_matrix_change = [[0 for _ in range(len(maze_matrix))] for _ in range(len(maze_matrix[0]))]

    found, paths = path_finder(position_y,position_x,[],maze_matrix,visited)

    for path in paths: 
        y,x = path
       # print(path)
        light_value_matrix_change[x][y] = START_PLAYER_LIGHT_RANGE+3
    light_value_matrix_change[position_y][position_x] = 3
    return light_value_matrix_change
def get_light_matrix(wall_matrix, target_tile, target_light_range):
    # room is dark at the start
    light_matrix = [[0 for _, _ in enumerate(wall_matrix)] for _, _ in enumerate(wall_matrix[0])]

    currently_inspecting_tiles = [target_tile]
    currently_inspecting_tile_light_values = [target_light_range]
    is_tile_inspected = [[False for _, _ in enumerate(wall_matrix)] for _, _ in enumerate(wall_matrix[0])]
    light_matrix[target_tile[0]][target_tile[1]] = target_light_range + 1

    iterations = 0
    while len(currently_inspecting_tiles) != 0:
        iterations += 1
        new_currently_inspecting_tiles = []
        new_currently_inspecting_tiles_light_values = []

        for i in range(len(currently_inspecting_tiles)):
            x = currently_inspecting_tiles[i][0]
            y = currently_inspecting_tiles[i][1]

            if is_tile_inspected[x][y]:
                continue
            if wall_matrix[x][y] == 1 and (x, y) != target_tile:
                continue

            is_tile_inspected[x][y] = True

            if currently_inspecting_tiles[i][0] != 0 and not is_tile_inspected[x - 1][y]:
                light_matrix[x - 1][y] = max(light_matrix[x - 1][y], currently_inspecting_tile_light_values[i] - 1)
                new_currently_inspecting_tiles.append((x - 1, y))
                new_currently_inspecting_tiles_light_values.append(currently_inspecting_tile_light_values[i] - 1)

            if currently_inspecting_tiles[i][1] != 0 and not is_tile_inspected[x][y - 1]:
                light_matrix[x][y - 1] = max(light_matrix[x][y - 1], currently_inspecting_tile_light_values[i] - 1)
                new_currently_inspecting_tiles.append((x, y - 1))
                new_currently_inspecting_tiles_light_values.append(currently_inspecting_tile_light_values[i] - 1)

            if currently_inspecting_tiles[i][0] != len(light_matrix) - 1 and not is_tile_inspected[x + 1][y]:
                light_matrix[x + 1][y] = max(light_matrix[x + 1][y], currently_inspecting_tile_light_values[i] - 1)
                new_currently_inspecting_tiles.append((x + 1, y))
                new_currently_inspecting_tiles_light_values.append(currently_inspecting_tile_light_values[i] - 1)

            if currently_inspecting_tiles[i][1] != len(light_matrix[0]) - 1 and not is_tile_inspected[x][y + 1]:
                light_matrix[x][y + 1] = max(light_matrix[x][y + 1], currently_inspecting_tile_light_values[i] - 1)
                new_currently_inspecting_tiles.append((x, y + 1))
                new_currently_inspecting_tiles_light_values.append(currently_inspecting_tile_light_values[i] - 1)
        
        currently_inspecting_tiles = new_currently_inspecting_tiles
        currently_inspecting_tile_light_values = new_currently_inspecting_tiles_light_values

    return light_matrix