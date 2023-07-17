def odd_series(a):
    series = []
    for i in range(1, a+1):
        series.append(2*i - 1)
    return series

a = int(input("Enter the value of a: "))

result = odd_series(a)

print("Output:", ', '.join(map(str, result)))
