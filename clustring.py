from netzob.all import *
print('\033[1;32m' +"\n[++++++++++++++++++++ 将报文进行聚类 (the first one seems interesting) ++++++++++++++++++++]\n"+'\033[0m')
message_session1 = PCAPImporter.readFile("ftp1.pcap").values()
message_session2 = PCAPImporter.readFile("ftp2.pcap").values()
message_session3 = PCAPImporter.readFile("ftp3.pcap").values()
messages = message_session1 + message_session2 + message_session3
symbol = Symbol(messages=messages)

Format.splitDelimiter(symbol, ASCII(" "))#分隔符
print('\033[1;36m'+"[+] 分割后报文如下:"+'\033[0m')
print(symbol)

symbols = Format.clusterByKeyField(symbol, symbol.fields[0])

print('\033[1;34m'+"[+] 聚类个数: {0}".format(len(symbols))+'\033[0m')
print('\033[1;34m'+"[+] 聚类列表:"+'\033[0m')



for keyFieldName, s in symbols.items():
    print("  * {0}".format(keyFieldName))

for s in symbols.values():
    ## Step 4
    print('\033[1;32m' +"\n[++++++++++++++++++++ 采用序列比对方法分析报文 on the third field of the symbol: {0} ++++++++++++++++++++]\n".format(s.name)+ '\033[0m')
    print(s)