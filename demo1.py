# print("okk")
#
# print('a',end='')
# print("b",end='')
#
# def print_message(x,y):
#     '''Print the maximum of two numbers.
#
#     The two value must be integers.'''
#     if x>y:
#         print(x,'is maximum')
#     if x<y:
#         print(y,'is maximum')
# print(3,5)
# print(print_message.__doc__)
# help(print_message)


#编写显示学校老师和学生的信息的继承类
# class Schoolmember:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print("这个人叫",self.name)
#
#     def tell(self):
#         # print("name：",self.name,"age:",self.age,end=" ")  #end表示print不另起一行！
#         print('name:"{}",age:"{}"'.format(self.name,self.age))
#
# class Student(Schoolmember):
#     def __init__(self,name,age,salary):
#         Schoolmember.__init__(self,name,age)
#         self.salary=salary
#         print('(Initialized Student: {})'.format(self.name))
#     def tell(self):
#         Schoolmember.tell(self)
#         #print("salary:",self.salary)
#         print('salary:"{}" '.format(self.salary))
#
#
# class Leader(Schoolmember):
#     def __init__(self,name,age,fee):
#         Schoolmember.__init__(self,name,age)
#         self.fee=fee
#     def tell(self):
#         #Schoolmember.tell(self)
#         print('leader的fee是："{}"'.format(self.fee))
#
# l=Leader("lingyue",21,1000000)
# l.tell()
#


#文件
poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''

f=open('poem.txt','w')
f.write(poem)
f.close()

f=open('poem.txt','r')
while True:
    line=f.readline()
    if len(line) == 0 :
        break
    print(line,end='')
f.close()
