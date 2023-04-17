def convert(n):
    # convert int to string
    st = str(n)
    # empty list
    result = []
# looping on string
    for num in st:
        result.append(int(num))
    result.reverse()

    return result


print(convert(564987654))  # [4, 5, 6, 7, 8, 9, 4, 6, 5]
print(convert(529132))  # [2, 3, 1, 9, 2, 5]
