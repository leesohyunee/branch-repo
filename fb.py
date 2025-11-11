for j in range(4, 15+1):
    if j % 15  == 0:
        print('fizzbuzz')
    if j % 5  == 0:
        print('buzz')
    elif j % 3 == 0:
        print('fizz')
    else:
        print(j)
