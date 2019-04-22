from netzob.all import *

def loadfile():
    #打开文件
    message_session1 = PCAPImporter.readFile("smtp14_1.pcap").values()
    message_session2 = PCAPImporter.readFile("smtp14_2.pcap").values()
    message_session3 = PCAPImporter.readFile("smtp14_3.pcap").values()
    message_session4 = PCAPImporter.readFile("smtp14_4.pcap").values()
    message_session5 = PCAPImporter.readFile("smtp11.pcap").values()
    message_session6 = PCAPImporter.readFile("smtp17.pcap").values()
    message_session7 = PCAPImporter.readFile("smtp60.pcap").values()
    message_session8 = PCAPImporter.readFile("smtp100.pcap").values()
    messages = message_session1 + message_session2 + message_session3 + message_session4 + message_session5 + message_session6 + message_session7 + message_session8
    # messages = message_session1
    # messages = message_session3
    # messages = PCAPImporter.readFile("http.pcap").values()

    #形成symbol
    symbol = Symbol(messages=messages)

    #将symbol内容转换为list格式
    symbol_list = symbol.getValues()

    #打印symbol_list的内容
    # print('you have load the list:' + str(symbol_list))

    return symbol_list