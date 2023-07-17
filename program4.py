def count_multiples(numbers, multiples):
    counts = {}
    for num in multiples:
        counts[num] = 0
        for value in numbers.values():
            if value % num == 0:
                counts[num] += 1
    return counts

numbers_list = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
multiples = [1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers_dict = {i: i for i in numbers_list}

result = count_multiples(numbers_dict, multiples)

print("Output:", result)
