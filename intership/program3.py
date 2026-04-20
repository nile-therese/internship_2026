import math

def k_closest_point(points, k):
    distance_list = []
    for (x, y) in points:
        distance = math.sqrt(x**2 + y**2)
        distance_list.append((distance, (x, y)))
    distance_list.sort()
    result = [distance_list[i][1] for i in range(k)]
    return result
if __name__ == "__main__":
    points = [(1, 3), (3, 4), (2, -1), (5, 2)]
    k = 2
    print("K closest points:", k_closest_point(points, k))