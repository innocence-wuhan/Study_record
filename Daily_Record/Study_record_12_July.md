# 7.12号学习规划
- [ ] **python** linearlist
- [ ] **deep-learning**
- [ ] **CET-6** - [ ] *vocabulary*
                - [ ] *translation*
                - [ ] *reading*
                - [ ] *listenning*

## **C++ transfer python**
概念	 |C++代码	                                    |Python 代码                      |
---------|----------------------------------------------|--------------------------------|
变量声明  |int age = 23;                            	|age = 23 # 自动类型推导           |
字符串处理|string name = "John";                        | 	name = "John"                 |	
列表/数组 |vector<float> scans = {3.1, 4.2};            |	scans = [3.1, 4.2]	          |
字典/Map  |map<string, int> teeth = {{"molar", 36}};	|teeth = {"molar": 36}	          |
循环      |for(int i=0; i<5; i++){...}	                |for i in range(5): ...	          |
函数定义  |int add(int a, int b){...}                  	|def add(a, b): ...	              |
类与对象  |class Patient{...};Patient p1;               |class Patient: ...p1 = Patient()  |
文件操作  |#include <fstream> ofstream file("data.txt");|with open("data.txt", "w") as file|
标准输出  |cout << "Hello";	                            |print("Hello")	自动换行，无需\n    |
格式化输出|printf("尺寸: %.2fmm", size);	             |print(f"尺寸: {size:.2f}mm")	    |f-string是神器！
单值输入  |cin >> age;	                                |age = input("输入年龄: ")	        |返回字符串需类型转换
多值输入  |cin >> a >> b;	                            |a, b = input().split()	           |配合split()解包