## 函数参数(二)

### <1>. 缺省参数

调用函数时，缺省参数的值如果没有传入，则取默认值。

下例会打印默认的age，如果age没有被传入：
	
```python
def printinfo(name, age=35):
   # 打印任何传入的字符串
   print("name: %s" % name)
   print("age %d" % age)
 
# 调用printinfo函数
printinfo(name="miki")  # 在函数执行过程中 age去默认值35
printinfo(age=9 ,name="miki")
```

以上实例输出结果：

```python
name: miki
age: 35
name: miki
age: 9
```
#### 总结：
* 在形参中默认有值的参数，称之为缺省参数
* 注意：带有默认值的参数一定要位于参数列表的最后面
	```python
	>>> def printinfo(name, age=35, sex):
	... 	print name
	...
	  File "<stdin>", line 1
	SyntaxError: non-default argument follows default argument
	```
