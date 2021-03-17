# kiki-turtle 绘图库

在 turtle 库的基础上增强了功能。借鉴了 Processing 的绘图函数，schemdraw 的链式语法，ruby 和 logo 语言接近自然语言的编程环境。
## 安装
```
python -m pip install kiki-turtle
```


## processing
processing 是面相艺术家的编程语言
### p5.js
processing 的 JavaScript 版本

## schemdraw
电路绘制和计算库
## ruby
日本人松本行弘发明的编程语言。

## 教程
绘制顶点在 (0, 0) 的长方形
```
from kiki_turtle import Kiki
import turtle

kiki = Kiki()
kiki.rect(100, 20)

turtle.mainloop()
```
绘制中心点在 (0, 0) 的长方形
```
kiki.mode('center').rect(100, 20).rect(20, 100).ht()
```
Kiki-turtle 库的使用既保留了 turtle 库原本的用法，也支持链式操作

### repate 和 times 方法配合绘制正方形
```
kiki.repeate().fd(100).rt(90).times(4)
```
将前进 100 右转 90 重复 4 次，绘制正方形。