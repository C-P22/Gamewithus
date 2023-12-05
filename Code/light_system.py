

def get_light_matrix(wall_matrix, target_tile, target_light_range, ignore_walls, light_matrix = [[]]):
    # if light_matrix wasn't set initialize a completely dark one
    if light_matrix == [[]]:
        light_matrix = [[0 for _, _ in enumerate(wall_matrix)] for _, _ in enumerate(wall_matrix[0])]
    
    if target_light_range == 0:
        return light_matrix

    # if tile is brighter don't make it darker
    # if this is a wall, illuminate it but don't continue
    if light_matrix[target_tile[0]][target_tile[1]] >= target_light_range or (wall_matrix[target_tile[0]][target_tile[1]] == 1 and not ignore_walls):
        light_matrix[target_tile[0]][target_tile[1]] = target_light_range
        return light_matrix
    
    light_matrix[target_tile[0]][target_tile[1]] = target_light_range

    # only illuminate neighbouring tiles if they exist
    if (target_tile[0] != 0):
        light_matrix = get_light_matrix(wall_matrix, (target_tile[0] - 1, target_tile[1]), target_light_range - 1, False, light_matrix)
    if (target_tile[1] != 0):
        light_matrix = get_light_matrix(wall_matrix, (target_tile[0], target_tile[1] - 1), target_light_range - 1, False, light_matrix)
    if (target_tile[0] != len(light_matrix) - 1):
        light_matrix = get_light_matrix(wall_matrix, (target_tile[0] + 1, target_tile[1]), target_light_range - 1, False, light_matrix)
    if (target_tile[1] != len(light_matrix[0]) - 1):
        light_matrix = get_light_matrix(wall_matrix, (target_tile[0], target_tile[1] + 1), target_light_range - 1, False, light_matrix)
    
    return light_matrix

def get_light_matrix_new(wall_matrix, target_tile, target_light_range):
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