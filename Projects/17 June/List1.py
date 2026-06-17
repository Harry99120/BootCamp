# A = [2,3,4,5]
# res = [val ** 2 for val in A]
# print(res)

# A = [1,2,3,4,5]
# res = [val for val in A if val % 2 == 0]
# print(res)

# B = [5,12,7,18,3,20]
# res = [val for val in B if val > 10]
# print(res)

# A = [i for i in range(10)]
# print(A)

# C = [(x,y) for x in range(3) for y in range(3)]
# print(C)

Mat = [[1,2,3],[4,5,6],[7,8,9]]
res = [val for row in Mat for val in row]
print(res)