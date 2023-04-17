def convert(n):
    return[int(num) for num in str(n)[::-1]]
 
print(convert(564987654))  # [4, 5, 6, 7, 8, 9, 4, 6, 5]
print(convert(529132))  # [2, 3, 1, 9, 2, 5]
