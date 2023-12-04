

def get_light_matrix(wall_matrix, target_tile, target_light_range, ignore_walls, light_matrix = [[]]):
    # if light_matrix wasn't set initialize a completely dark one
    if light_matrix == [[]]:
        light_matrix = [[0 for _, _ in enumerate(wall_matrix)] for _, _ in enumerate(wall_matrix[0])]

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
