print("hello world")
a=98
c='b'
# ASCII码
print(chr(98))
#中文输出
print(ord('北'))
print(chr(21271),chr(20140))
#输出数据到文件中
fp=open('note,txt','w') #打开文件
print('北京欢迎你',file=fp) #将信息写入文件
fp.close()
print('hello',end='->')
print('world')
print('hel'+'lo')
'''
这是一条注释
'''