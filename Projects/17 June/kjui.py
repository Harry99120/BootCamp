for i in range(2,9):
    for j in range(1,11):
            if i == 5 or i == 10 or j == 5 or j == 10:
                continue
            print(i,'*',j, '=',i*j)
    print()

