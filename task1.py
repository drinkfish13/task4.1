data = [
    [13, 25, 23, 34],
    [45, 32, 44, 47],
    [12, 33, 23, 95],
    [13, 53, 34, 35],
    ]
def sum_of_square(data):
    sum_ = 0
    for i in range(len(data)):
        sum_ = sum_ + int(data[i][i])
    return sum_

print(sum_of_square(data))