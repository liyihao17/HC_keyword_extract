#返回LCS的list
def GetLCS(a,b):

    def lcs(a, b):
        lena = len(a)
        lenb = len(b)
        c = [[0 for i in range(lenb + 1)] for j in range(lena + 1)]
        flag = [[0 for i in range(lenb + 1)] for j in range(lena + 1)]
        for i in range(lena):
            for j in range(lenb):
                if a[i] == b[j]:
                    c[i + 1][j + 1] = c[i][j] + 1
                    flag[i + 1][j + 1] = 'ok'
                elif c[i + 1][j] > c[i][j + 1]:
                    c[i + 1][j + 1] = c[i + 1][j]
                    flag[i + 1][j + 1] = 'left'
                else:
                    c[i + 1][j + 1] = c[i][j + 1]
                    flag[i + 1][j + 1] = 'up'
        return c, flag


    def printLcs(flag, a, i, j):
        if i == 0 or j == 0:
            return
        if flag[i][j] == 'ok':
            printLcs(flag, a, i - 1, j - 1)
            result.append(a[i - 1])
            result_index.append(i-1)
        elif flag[i][j] == 'left':
            printLcs(flag, a, i, j - 1)
        else:
            printLcs(flag, a, i - 1, j)
        return bytes(result)

    result = []
    c, flag = lcs(a, b)
    result_index = []
    result = printLcs(flag, a, len(a), len(b))
    return [result,result_index]

def GetLCSandIndex(a,b):
    [result,result_index_1] = GetLCS(a,b)
    [result,result_index_2] = GetLCS(b,a)
    return [result,result_index_1,result_index_2]

def GetLCS2(a,b):

    def lcs(a, b):
        lena = len(a)
        lenb = len(b)
        c = [[0 for i in range(lenb + 1)] for j in range(lena + 1)]
        flag = [[0 for i in range(lenb + 1)] for j in range(lena + 1)]
        for i in range(lena):
            for j in range(lenb):
                if a[i] == b[j]:
                    c[i + 1][j + 1] = c[i][j] + 1
                    flag[i + 1][j + 1] = 'ok'
                elif c[i + 1][j] > c[i][j + 1]:
                    c[i + 1][j + 1] = c[i + 1][j]
                    flag[i + 1][j + 1] = 'left'
                else:
                    c[i + 1][j + 1] = c[i][j + 1]
                    flag[i + 1][j + 1] = 'up'
        return c, flag


    def printLcs(flag, a, i, j):
        if i == 0 or j == 0:
            return
        if flag[i][j] == 'ok':
            printLcs(flag, a, i - 1, j - 1)
            result.append(a[i - 1])
        elif flag[i][j] == 'left':
            printLcs(flag, a, i, j - 1)
        else:
            printLcs(flag, a, i - 1, j)
        return result

    result = []
    c, flag = lcs(a, b)

    result = printLcs(flag, a, len(a), len(b))
    return bytes(result)
a = b'\x03\x00\x00\x16\x11\xe0\x00\x00\x00\x07\x00\xc1\x02\x01\x00\xc2\x02\x01\x02\xc0\x01\n'
b = b'\x03\x00\x00\x16\x11\xd0\x00\x07\x00\x03\x00\xc0\x01\n\xc1\x02\x01\x00\xc2\x02\x01\x02'
print(a)
print(b)
result = GetLCSandIndex(a,b)
print(result)
print(result[0])
print(result[1][0])
print(result[1][1])