def generate_series(a):
    series = []
    if a % 2 != 0:
        for i in range(1, a+1, 2):
            series.append(i)
    else:
        for i in range(1, a, 2):
            series.append(i)
    return series

a = int(input("Enter the value of a: "))

result = generate_series(a)

print("Output:", ', '.join(map(str, result)))
