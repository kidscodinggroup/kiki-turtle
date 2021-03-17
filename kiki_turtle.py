"""
Author: langxm
Email: 964683112@qq.com
Kiki 是英文单词 kitten 的前两个字母
用作名字也感觉很卡哇伊，我喜欢这个名气
"""
import turtle

class Kiki:
    def __init__(self):
        pass
        self.pen = turtle.Turtle()
        
        self.stack = []
        self._mode = 'corner'
        self._fill_color = None
        self._stroke_color = 'black'
        self._repeat_stack = []

        self.v = self.pen.speed
        self._complex_command = False

    def __getattr__(self, name):
        # print(name)
        def hi(*args, **kwargs):
            getattr(self.pen, name)(*args, **kwargs)
            if self._repeat_flag:
                self._simple_command = True
                self.repeat_manager(getattr(self.pen, name), (args, kwargs))
            
            if name == 'dot':
                args = [1]
                print('INFO: dot 方法不提供参数默认值改为 1 与 turtle 行为不同')
            if len(args) == 0:
                if name in ['pu', 'pd']:
                    return self
                return getattr(self.pen, name)()
            return self
        return hi
    
    def noFill(self):
        self._fill_color = None
        return self
    
    def noStorke(self):
        self._stroke_color = None
        self.pu()
        return self
    
    def mode(self, m):
        self._mode = m
        return self

    def _color(self, color):
        if type(color) == type(''):
            return color
        if type(color) == type(()):
            if len(color) == 3 and color[0] <= 1 and color[1] <= 1 and color[2] <= 1:
                return color
        if type(color) == type(1.0):
            return (color, color, color)
            
        raise(ValueError('目前颜色参数只支持三个 0 到 1 的小数 rgb 或者整数参数的灰度或者字符串'))
            
    
    def fill(self, color):
        self._fill_color = color
        self.fillcolor(self._color(color))
        return self
    
    def stroke(self, color):
        self._stroke_color = color
        self.pencolor(self._color(color))
        return self
    
    def push(self):
        self.stack.append((self.position(), self.heading()))
        return self
    
    def strokeWeight(self, value):
        self.pensize(value)
        return self
    
    
    
    def pop(self):
        pos, heading = self.stack.pop()
        x, y = pos
        self.move(x, y)
        self.setheading(heading)
        return self

    def move(self, x, y):
        self.pu()
        self.goto(x, y)
        self.pd()
        return self
    
    def line(self, *args):
        if len(args) == 4:
            x1, y1, x2, y2 = args
        elif len(args) == 2:
            x1, y1 = self.position()
            x2, y2 = args
        else:
            raise(SyntaxError('直线需要 2 个或者 4 个参数'))
        self.move(x1, y1)
        self.goto(x2, y2)
        return self
    
   

    def square(self, *args, **kwargs):
        if len(args) == 1:
            return self.rect(args[0], args[0])
        return self.rect(self, *args, **kwargs)

    def circle(self, *args, **kwargs):
        if self._repeat_flag:
            self._repeat_stack.append((self.circle, (args, kwargs)))
        if self._mode == 'center':
            if len(args) == 3:
                x, y, r = args
                self.move(x, y)
            elif len(args) == 1:
                r = args[0]
            else:
                raise(SyntaxError('圆需要 1 个或者 4 个参数'))
            self.push()
            self.pu()
            self.rt(90)
            self.fd(r)
            self.lt(90)
            self.pd()
            if self._fill_color:
                self.begin_fill()
            if not self._stroke_color:
                self.pu()
            self.pen.circle(r)
            
            if self._fill_color:
                self.end_fill()
            self.pop()
        elif self._mode == 'corner':
            if len(args) == 3:
                x, y, r = args
                self.move(x, y)
            elif len(args) == 1:
                r = args[0]
            else:
                raise(SyntaxError('圆需要 1 个或者 4 个参数'))
            self.push()
            self.pu()
            self.fd(r)
            self.rt(90)
            self.fd(r*2)
            self.lt(90)
            self.pd()
            if self._fill_color:
                self.begin_fill()
            if not self._stroke_color:
                self.pu()
            self.pen.circle(r)
            if self._fill_color:
                self.end_fill()
            self.pop()
        return self

    def rect(self, *args, **kwargs):
        if self._repeat_flag:
            self._complex_command = True
            self._simple_command = False
            self.repeat_manager(self.rect, (args, kwargs))
        if self._mode == 'corner':
            if len(args) == 4:
                x, y, w, h = args
                self.move(x, y)
            elif len(args) == 2:
                w, h = args
            else:
                raise(SyntaxError('直线需要 2 个或者 4 个参数'))
            if 'angle' in kwargs:
                self.lt(kwargs['angle'])
            self.push()
            if self._fill_color:
                self.begin_fill()
            if not self._stroke_color:
                self.pu()
            for i in range(2):
                self.fd(w)
                self.rt(90)
                self.fd(h)
                self.rt(90)
            if self._fill_color:
                self.end_fill()
            self.pop()
        elif self._mode == 'center':
            if len(args) == 4:
                x, y, w, h = args
                self.move(x, y)
            elif len(args) == 2:
                w, h = args
            else:
                raise(SyntaxError('直线需要 2 个或者 4 个参数'))
            self.push()
            # self.move(self.xcor()-w/2, self.ycor()+h/2)
            if 'angle' in kwargs:
                self.lt(kwargs['angle'])
            self.pu()
            
            self.bk(w/2)
            self.lt(90)
            self.fd(h/2)
            self.rt(90)
            self.pd()
            
            
            if self._fill_color:
                self.begin_fill()
            if not self._stroke_color:
                self.pu()
            for i in range(2):
                self.fd(w)
                self.rt(90)
                self.fd(h)
                self.rt(90)
            if self._fill_color:
                self.end_fill()
            self.pop()
        
        if self._repeat_flag:
            self._complex_command = False
            self._simple_command = True
        return self
    def repeat_manager(self, func, params):
        
        # print(len(self._repeat_stack))
        if not self._repeat_flag:
            return 
        if self._simple_command and not self._complex_command:
            self._repeat_stack.append((func, params))
            return self
        if self._complex_command and not self._simple_command:
            self._repeat_stack.append((func, params))
        
        
            
    
    def arc(self, *args, **kwargs):
        
        if len(args) == 5:
            x, y, start_angle, end_angle, r = args
        else:
            raise(SyntaxError('圆弧参数有问题'))
        
        if self._repeat_flag:
            self._repeat_stack.append((self.arc, (args, kwargs)))
        self.move(x, y)
        if self._fill_color:
                self.begin_fill()
        if not self._stroke_color:
            self.pu()
        # self.push()
        self.rt(start_angle)
        self.fd(r)
        self.rt(90)
        self.pen.circle(-r, end_angle-start_angle)
        self.rt(90)
        self.fd(r)
        if self._fill_color:
            self.end_fill()
        # self.pop()
        return self

        
    def border(self, shape='circle'):
        # self.fd(10)
        return self
    def home(self):
        self.pen.home()
        return self
    def bgcolor(self, color):
        screen = self.pen.screen
        screen.bgcolor(color)
    
    
    def repeat(self,*args, **kwargs):
        self._repeat_flag = True
        self._repeat_stack = []
        return self
    
    def times(self, times):
        self.times = times
        self._repeat_flag = False
    
        # return self
        for _ in range(self.times-1):
            for i in range(len(self._repeat_stack)):
                func, params = self._repeat_stack[i]
                args, kwargs = params
                func(*args, **kwargs)
        self._repeat_flag = False
        self._repeat_stack = []
        return self
        
    def done(self):
        turtle.done()
if __name__ == "__main__":
    kiki = Kiki()
    # kiki.noStorke().fill('red').arc(0,0,45, 90, 100).home()
    # 精灵球
    # kiki.mode('center').noStorke().bgcolor('gray')
    # kiki.fill('white').circle(100).fill('red').arc(0,0,180, 360, 100).home()
    # kiki.strokeWeight(8).line(-97, 0, 97, 0)
    # kiki.home().strokeWeight(6).stroke('black').fill('white').circle(20).ht()

    # 八卦
    # kiki.rt(90)
    # kiki.mode('center').fill('white').circle(100)
    # kiki.fill('black').arc(0, 0, 90, -90, 100).circle(0, 50, 50)
    # kiki.noStorke().fill('white').circle(0, -50, 50)
    # kiki.noStorke().home().rt(90).fill('black').push().fd(50).circle(25).pop()
    # kiki.pu().home().lt(90).fill('white').push().fd(50).circle(25).pop().ht()
    # 重复执行
    # kiki.repeat().rect(90, 90).rt(27).times(13)
    # kiki.speed(0).repeat().fd(100).rt(90).fd(100).lt(90).times(4)
    # kiki.speed(0).mode('center').repeat().rect(200, 200).rt(7).times(36).ht()
    kiki.mode('center').repeat().rect(100, 10).rect(10, 100).rt(30).times(3).ht()
    turtle.mainloop()