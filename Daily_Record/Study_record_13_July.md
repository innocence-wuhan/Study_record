# **windows cmd** 
*检查版本号* --version ag：python --version 

# **python**

## 程序语言的分类

语言类型|解释                  |举例                              |
-------|----------------------|---------------------------------|
机器语言|二进制语言             |00100111                         |
汇编语言|使用机器语言中的指令之类| add 4,r1,r2                     |
高级语言|更贴近于自然语言        |python:```print("hello world")```|

**编译型代码和解释型代码：**
解释型：解释器只解释运行到的源代码，不产生中间文件，每次执行都会重新解释源代码，下载源代码时是下载了包括开发环境，解释器，源代码在内的所有文件，解释型语言不可脱离开发环境，这个特性使其可跨平台，eg:python;Javascript;PHP

## python编程基础

### IPO程序编写方法 input，process, output 

#### **输出函数** print();
**完整格式** ```print(value,...,sep=' ',end='\n',file=None)```
*语法结构*：```print(输出内容)```
*输出中文* ```print(ord('北'))；print(chr(21271),chr(20140))```

##### **将数据输出到文件中**
python:```fp=open('note,txt','w') #打开文件
print('北京欢迎你',file=fp) #将信息写入文件
fp.close()```

##### **使用连接连接两个字符串**
python:```print('hel'+'lo')```
*不能连接一个字符串连接一个其他型*

##### **改变尾部的'\n'**
python:```print('hello',end='->')
print('world')```

### **输入函数** input();
**完整格式** x=input('提示文字)
python:```name=input('your name:')
print('my name is '+name)```


### **注释**
#单行注释
'''
这是一条注释
这也是一条注释，这是多行注释————
'''
#coding=utf-8 //编译方式
#中文声明注释一定要写在第一行

