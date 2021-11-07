

def distance(p1: list, p2: list):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 1/2

def solve(points: list):


    num_inter = 0
    for point1 in points:
        curr_point_dct = {}
    
        for point2 in points:
            if point2 == point1:
                continue
            dist = distance(point1, point2)
            curr_inter_pt = curr_point_dct.get(dist, 0)
            num_inter += curr_inter_pt
            curr_point_dct[dist] = curr_inter_pt + 1
    
    num_inter *= 2  # i, j, k is the same as i, k, j => * 2
    return num_inter
    

