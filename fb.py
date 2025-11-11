for j in range(4, 15+1):
    if j % 3  == 0 or j % 5 == 0:
        print('fizz' * (j%3==0) + 'buzz' * (j%5==0))
    else:
        print(j)
