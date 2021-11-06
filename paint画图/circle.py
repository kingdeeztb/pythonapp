'''
turtle库是python标准库之一，入门级绘图库。import turtle之后即可使用。

1、绘图窗口设置命令

turtle.setup(400,300,200,100)：参数以此（宽，高，距离屏幕左边距离，距离屏幕上方距离），屏幕左上角原点，单位像素。

2、运动命令

turtle.goto(x,y)：直接跳转到（x,y）点，以绘图窗口中心为原点，向右为x轴，向上为y轴。

turtle.fd(d)、turtle.forward(d)：以当前方向，往前行进d像素。

turtle.bk(d)、turtle.backword(d)：保持当前方向不变，往后退行d像素。

turtle.circle(r,angle)：从当前位置以r为半径圆的angle角度旋转。

 

    circle(100,180)              circle(100，-180)            ciecle(-100,180)            circle(-100，-180) 

                            

3、方向设置命令

turtle.seth(angle)：以x轴方向为起点将方向偏转为angle度，逆时针为正。只改变行进方向但不行进。

turtle.left(angle)：在当前行进方向的基础上，向左旋转angle度。

turtle.right(angle)：在当前行进方向的基础上，向右旋转angle度。

4、画笔控制命令

turtle.penup()：台笔

turtle.pendown()：落笔

turtle.pensize(width)：画笔粗细

turtle.pencolor(颜色名red/RGB三元组/颜色编码)：画笔颜色

turtle.fillcolor(colorstring)：绘制图形的填充颜色

turtle.begin_fill()：开始填充

turtle.end_fill()：结束填充

turtle.filling()：返回当前是否在填充状态
————————————————
版权声明：本文为CSDN博主「eook767117193」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/u014041590/java/article/details/88913903
'''
# import turtle as t
# d = 0
# k = 1
# for j in range(100000):
#     for i in range(4):
#         t.fd(k)
#         d += 91
#         t.seth(d)
#         k += 2
# t.done()
# import turtle as t
# d=0
# for i in range(4):
#     t.fd(200)
#     d=d+90
#     t.seth(d)
# t.done()

# import turtle as t
# d=0
# for i in range(1):
#     t.circle(100,360)
#     t.seth(d)
# t.done()
# import turtle as t
# d = 0
# for i in range(400):
#     t.fd(200)
#     d=d+90
#     t.seth(d)
# t.done()
# import turtle as t
# d=0
# for i in range(10000):
#     t.fd(100)
#     d=d+99
#     t.seth(d)
# t.done()

# import turtle as t
# for i in range (1):
#     t.circle(100,360)
#     t.done()
# sudo apt search python3-tk 
import turtle as tr #Ubuntu需要安装python3-tk
d=0
for i in range(3):
    tr.fd(200)
    d+=120
    tr.seth(d)
tr.done()