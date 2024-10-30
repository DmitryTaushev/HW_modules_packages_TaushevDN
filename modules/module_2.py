def oddnum(a , b):
    odd_number = []
    for num in range(a , b):
        if num%2 == 0:
            odd_number.append(num)
    return odd_number