import LoadFile
import GetLCS
import ListOperate
import time
start = time.clock()

symbol_list_readfile = LoadFile.loadfile()

symbol_list = LoadFile.loadfile()
symbol_list = list(set(symbol_list))
ExtractKeyWord = []
result_index = []
symbol_list_old = []
print(symbol_list)

matrix = [[999 for i in range(len(symbol_list))] for j in range(len(symbol_list))]
while len(symbol_list) != 1:#and ListOperate.GetMaxElement(matrix) > 0.1 and not ListOperate.CmpList(symbol_list,symbol_list_old):
    for i in range(0, len(symbol_list)):
        for j in range(0, len(symbol_list)):
            if i == j:
                matrix[i][j] = 0
            else:
                result = GetLCS.GetLCS2(symbol_list[i], symbol_list[j])
                matrix[i][j] = len(result) / max(len(symbol_list[i]),len(symbol_list[j]))
    print(matrix)
    x, y = ListOperate.GetMaxElementIndex(matrix)
    print("symbol_list is " + str(symbol_list))
    print("x=" + str(x) + " y=" + str(y) + " symbol_list_lenth=" + str(len(symbol_list)))
    result = GetLCS.GetLCSandIndex(symbol_list[x], symbol_list[y])
    print(result)

    symbol_list_old = symbol_list[:]
    ListOperate.RemoveSymbolList(symbol_list,x,y)

    symbol_list.append(result[0])
    symbol_list = list(set(symbol_list))

    flag = 0
    for k in range(0, len(ExtractKeyWord)):
        if result[0] == ExtractKeyWord[k][0]:
            ExtractKeyWord[k].append(result[1])
            ExtractKeyWord[k].append(result[2])
            flag = 1
            break
    if flag == 0:
        ExtractKeyWord.append(result)

    matrix = [[999 for i in range(len(symbol_list))] for j in range(len(symbol_list))]

print(ExtractKeyWord)



#去重位置属性
for k in range(len(ExtractKeyWord)):
    tmp = []
    for element in ExtractKeyWord[k]:
        if element not in tmp:
            tmp.append(element)
    ExtractKeyWord[k] = tmp[:]

print("ExtractKeyWord:")
print(ExtractKeyWord)
print(len(ExtractKeyWord))

for i in range(0,len(ExtractKeyWord)):
    print(ExtractKeyWord[i])

#对提取出来的LCS进行去重，如果某个提取出来的LCS是另一个提取出来的LCS的LCS那么，留下更长的那一个，去掉短的那一个LCS
ExtractKeyWord_new = ExtractKeyWord[:]
label = []
for i in range(0,len(ExtractKeyWord)):
    for j in range(i+1, len(ExtractKeyWord)):
        result = GetLCS.GetLCS2(ExtractKeyWord[i][0],ExtractKeyWord[j][0])
        if result == ExtractKeyWord[i][0] or result == ExtractKeyWord[j][0]:
            if len(ExtractKeyWord[i][0]) > len(ExtractKeyWord[j][0]):
                label.append(j)
            else:
                label.append(i)
label = list(set(label))
print(label)

for i in range(0,len(label)):
    ExtractKeyWord.remove(ExtractKeyWord_new[label[i]])

for i in range(0,len(ExtractKeyWord)):
    print(ExtractKeyWord[i])

#根据提取到的LCS在原来报文中的位置是否连续，提取出关键词
wordtmp = []
ExtractKeyWord_single = []
for i in range(0,len(ExtractKeyWord)):
    for j in range(1,len(ExtractKeyWord[i])):
        for k in range(0,len(ExtractKeyWord[i][j])-1):
            if ExtractKeyWord[i][j][k] + 1 == ExtractKeyWord[i][j][k + 1]:
                wordtmp.append(ExtractKeyWord[i][0][k])
                if k == len(ExtractKeyWord[i][j])-2:
                    wordtmp.append(ExtractKeyWord[i][0][k+1])
                    ExtractKeyWord_single.append(bytes(wordtmp))
                    wordtmp = []
            else:
                wordtmp.append(ExtractKeyWord[i][0][k])
                ExtractKeyWord_single.append(bytes(wordtmp))
                wordtmp = []

# print(list(set(ExtractKeyWord_single)))
ExtractKeyWord_single = list(set(ExtractKeyWord_single))
print('ExtractKeyWord_single is ')
for i in range(len(ExtractKeyWord_single)):
    print(ExtractKeyWord_single[i])
# num = [0 for i in range(len(ExtractKeyWord_single))]
# for i in range(len(ExtractKeyWord_single)):
#     for j in range(len(symbol_list_readfile)):
#         if GetLCS.GetLCS2(ExtractKeyWord_single[i],symbol_list_readfile[j]) == ExtractKeyWord_single[i]:
#             num[i] = num[i] + 1
#
# print('Extracted key word is ')
# for i in range(0,len(ExtractKeyWord_single)):
#     print(str(ExtractKeyWord_single[i]) + ' and the times is ' + str(num[i]))
#
# ExtractKeyWord_final = []
# for i in range(len(num)):
#     if num[i] >= 5:
#         ExtractKeyWord_final.append(ExtractKeyWord_single[i])
#
# print("")
# print("")
# for i in range(len(ExtractKeyWord_final)):
#     print(ExtractKeyWord_final[i])

ExtractKeyWord_single_tmp = ExtractKeyWord_single[:]
for i in range(len(ExtractKeyWord_single_tmp)):
    if len(ExtractKeyWord_single_tmp[i])<=3:
        ExtractKeyWord_single.remove(ExtractKeyWord_single_tmp[i])

print("")
print("")
print("Extracted key word is:")
for i in range(len(ExtractKeyWord_single)):
    print(ExtractKeyWord_single[i])
print("The lenth of extracted key word is " + str(len(ExtractKeyWord_single)))

#
# #对提取出来的LCS进行去重，如果某个提取出来的LCS是另一个提取出来的LCS的LCS那么，留下更长的那一个，去掉短的那一个LCS
# ExtractKeyWord_new = ExtractKeyWord_single[:]
# label = []
# for i in range(0,len(ExtractKeyWord_single)):
#     for j in range(i+1, len(ExtractKeyWord_single)):
#         result = GetLCS.GetLCS2(ExtractKeyWord_single[i],ExtractKeyWord_single[j])
#         if result == ExtractKeyWord_single[i] or result == ExtractKeyWord_single[j]:
#             if len(ExtractKeyWord_single[i]) > len(ExtractKeyWord_single[j]):
#                 label.append(j)
#             else:
#                 label.append(i)
# label = list(set(label))
# print(label)
#
# for i in range(0,len(label)):
#     ExtractKeyWord_single.remove(ExtractKeyWord_new[label[i]])
#
# for i in range(0,len(ExtractKeyWord_single)):
#     print(ExtractKeyWord_single[i])
end = time.clock()
print("")
print('Running time: %s Seconds'%(end-start))