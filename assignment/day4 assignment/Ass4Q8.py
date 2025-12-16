data = (
    (10, 10, 10, 12),
    (30, 45, 56, 45),
    (81, 80, 39, 32),
    (1, 2, 3, 4)
)

result = []

cols = len(data[0])

for i in range(cols):
    column_sum = 0
    for row in data:
        column_sum += row[i]
    avg = column_sum / len(data)
    result.append(avg)

print(result)
