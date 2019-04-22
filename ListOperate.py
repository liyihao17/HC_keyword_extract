import operator

#返回matrix（二维列表）最大值的索引
def GetMaxElementIndex(matrix):
    a = [(matrix.index(i), i.index(max(i))) for i in matrix if max([max(i) for i in matrix]) in i]
    x = a[0][0]
    y = a[0][1]
    return x,y

#返回matrix（二维列表）的最大值
def GetMaxElement(matrix):
    a = [(matrix.index(i), i.index(max(i))) for i in matrix if max([max(i) for i in matrix]) in i]
    x = a[0][0]
    y = a[0][1]
    return matrix[x][y]

#移除symbol_list索引为x和y的两行
def RemoveSymbolList(symbol_list,x,y):
    tmp = symbol_list[:]
    symbol_list.remove(tmp[x])
    symbol_list.remove(tmp[y])

#对比两个二维列表的元素是否一一对应相等
def CmpList(a,b):
    return operator.eq(a,b)

# def FindIndex(result,ExtractKeyWord):
#     for i in range(0, len(ExtractKeyWord)):
#         if result[0] == ExtractKeyWord[i][0]:
#             for j in range(0,len(ExtractKeyWord[i])):
#                 if result[1] == ExtractKeyWord[i][]
# matrix = [[1,0,0],[0,100,0],[0,1,3]]
# print(GetMaxElementIndex(matrix))
# print(GetMaxElement(matrix))