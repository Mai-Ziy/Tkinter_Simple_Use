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