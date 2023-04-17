def convert(n):

    result = []
# looping on string
    for num in str(n):
        result.insert(0, int(num))

    return result


print(convert(564987654))  # [4, 5, 6, 7, 8, 9, 4, 6, 5]
print(convert(529132))  # [2, 3, 1, 9, 2, 5]
