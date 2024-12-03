
total_distance = 0



with open('AoC\day_1\day1_data.txt', 'r') as file:
    list_a = []
    list_b = []

    for line in file:
        left, right = map(int, line.split())
        list_a.append(left)
        list_b.append(right)
        list_a.sort()
        list_b.sort()

    for a, b in zip(list_a, list_b):
        if a > b:
            total_distance += a - b
        elif b > a:
            total_distance += b - a
    
print(total_distance)
        