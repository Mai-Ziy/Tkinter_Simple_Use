This is a simple Tkinter experiment
This experiment is based on the python infrastructure tkiner

Experimental objectives：
1.Create a window and set the background image
2.Add a button and label control
3.Add button click event
4.Button signal slot binding label


前言
Tkinter 模块(Tk 接口)是 Python 的标准 Tk GUI 工具包的接口，是Python内的一个基础GUI库，广泛应用于需要简单GUI的应用场景，编程时不支持界面与逻辑分离，因此有着天生的缺陷，不过优势也很明显，Python 使用 Tkinter 可以快速的创建 GUI 应用程序。语法清晰，而且控件信号槽之间分离（具体表现为一个控件代码出错不会中断整个应用程序）。

使用引导
导入包
import tkinter as tk
from tkinter import *
初始化界面
main_window = tk.Tk()
main_window是整个界面的主窗口，名字可以自定义。

设置窗口标题
main_window.title("界面")
title函数用于设置标题，其传参内容为字符串，对中文有良好的支持。

设置窗口创建大小
main_window.geometry("1280x720")
geometry函数用于设置主窗口大小，其传参为自定义尺寸。

添加窗口背景图片
photo = tk.PhotoImage(file="background.png")  # file：t图片路径
imgLabel = tk.Label(main_window, image=photo)  # 把图片整合到标签类中
imgLabel.pack(side=tk.RIGHT)  # 自动对齐
定义photo变量，并把图片进行初始化；创建标签变量，给主窗口添加图片；pack函数用于布局定位，参数有以下三种

句法
widget.pack( pack_options )
这是可能的选项列表-

expand-设置为true时，小部件将扩展以填充小部件的父级中未使用的任何空间。

fill-确定小部件是否填充了打包程序分配给它的任何额外空间，还是保持其自己的最小尺寸：NONE（默认），X（仅水平填充），Y（仅垂直填充）或BOTH（水平和垂直填充） ）。

side-确定父窗口小部件的哪一侧相对：TOP（默认），BOTTOM，LEFT或RIGHT。

添加一个Label控件
tk.Label(main_window, text='功能预览', font="楷体 40 bold").place(x=0, y=0, anchor='nw')
 句法
widget.Lable(main_winodws,...,...,...)#添加变量用','分隔，共18个参数可调。
转载于：https://www.tutorialspoint.com/python/tk_label.htm

Sr.No.	Option & Description
1	
anchor（位置）

如果小部件的空间大于文本所需的空间，此选项控制文本的位置。默认值为anchor=CENTER，它使文本在可用空间中居中。

2	
bg（背景色）

显示在标签和指示器后面的正常背景色。

3	
bitmap（位图）

将此选项设置为位图或图像对象，标签将显示该图形。

4	
bd（边框）

指示器周围边框的大小。默认值为2像素。

5	
cursor（光标）

如果您将此选项设置为光标名称（箭头、点等），当鼠标光标位于checkbutton上时，它将更改为该模式.

6	
font（字体）

文本标签选项指定文本中显示的字体。

7	
fg（文本颜色）

如果要在此标签中显示文本或位图，则此选项指定文本的颜色。如果要显示位图，这是位图中1位位置处显示的颜色。

8	
height（高度）

设置控件高度。

9	
image（图片）

要在标签小部件中显示静态图像，请将此选项设置为图像对象。

10	
justify（对齐方式）

指定多行文本如何相互对齐：LEFT表示左对齐，CENTER表示居中（默认），RIGHT表示右对齐。

11	
padx（文本左右空间）

在小部件内文本的左右两侧添加了额外的空间。默认值为1。

12	
pady（文本上下空间）

在小部件内文本的上方和下方添加额外的空间。默认值为1。

13	
relief（边框）

指定标签周围装饰边框的外观。默认值是FLAT。

14	
text（文本）

显示指定文本，完美兼容中文。

15	
textvariable（文本变量）

要将标签小部件中显示的文本从属于StringVar类的控制变量，请将此选项设置为该变量。

16	
underline（下划线）

通过将此选项设置为n，可以在文本的第n个字母下显示下划线（U），从0开始计算。默认值为下划线=-1，表示没有下划线。

17	
width（宽度）

设置控件宽度

18	
wraplength（字符限制）

通过将此选项设置为所需的字符数，可以限制每行中的字符数。默认值0表示仅在换行处换行。

Button控件
testBtn = tk.Button(main_window, text='开始', width=15, height=2, font=ft2, command=Voice_do).place(
    x=165,
    y=440,
    anchor='n')
句法
w = Button ( master, option=value, ... )
参数
master − 这表示父（主）窗口。

options − 可填入下面的参数

Sr.No.	Option & Description
1	
activebackground

当按钮在光标下时的背景色。

2	
activeforeground

当按钮位于光标下时的activeforegroundForeground颜色。

3	
bd

bdBorder宽度（像素）。默认值为2。

4	
bg

背景颜色。

5	
command

单击按钮时要调用的方法。

6	
fg

前景文本颜色。

7	
font

字体样式。

8	
height

控件高度.

9	
highlightcolor

焦点高亮颜色

10	
image

放置于控件的图片

11	
justify

说明如何显示多个文本行：每行从左到左对齐；居中到居中；或从右到右对齐。

12	
padx

文本的左右附加填充。

13	
pady

文本上方和下方的附加填充。

14	
relief

指定边框的类型。可选值是SUNKEN, RAISED, GROOVE, and RIDGE。

15	
state

状态将此选项设置为DISABLED可使按钮灰显并使其无响应。当鼠标悬停在该值上时，该值处于活动状态。默认值为“正常”。

16	
underline

underlineDefault为-1，表示按钮上的文本字符将不带下划线。如果非负数，则相应的文本字符将加下划线。

17	
width

控件宽度

18	
wraplength

如果此值设置为正数，则文本行将换行以适合此长度。

Label应用实例
举个例子 通过一个按钮和一个文本控件

from tkinter import *
import tkinter as tk
# 主窗口
main_window = tk.Tk()
main_window.title("界面")
main_window.geometry("600x600")
# 添加背景图
photo = tk.PhotoImage(file="background.png")  # file：t图片路径
imgLabel = tk.Label(main_window, image=photo)  # 把图片整合到标签类中
imgLabel.pack(side=tk.RIGHT)  # 自动对齐
#字体样式
ft2 = "微软雅黑 30 bold"
 
#创建点击事件
def test_fun():
    a = "hellopython"
    print(a)
    var.set(a)#显示文本变量信息
#创建一个按钮，文本是“开始”，高度15，宽度2，字体是微软雅黑30号字体，点击事件的函数名为test_fun.
#place为放置位置，x，y为放置坐标，anchor为向上对齐格式。
test_Button = tk.Button(main_window, text='开始', width=15, height=2, font=ft2, command=test_fun).place(
    x=300,
    y=300,
    anchor='n')
#创建一个变量设置关联
var = tk.StringVar()  # 设置关联
#创建一个Label控件用于显示相关信息
#textvariable创建一个字符串变量，bg为设置控件颜色粉色，font为字体，设置宽度高度（像素），place控制放置位置
test_Label= tk.Label(main_window, textvariable=var, bg='pink', font=ft2, width=28, height=2).place(
    x=65, y=420)
