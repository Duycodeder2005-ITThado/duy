from turtle import*
setup(1366,768)

#ht()
speed(0)
pensize(3)
def face():
    up()
    seth(90)
    #fd(30)
    goto(-50,250)
    down()
    fd(20)
    
    circle(-50,20)
    begin_fill()
    color('black','black')
    seth(70)
    circle(-100,90)
    seth(340)
    fd(20)
    circle(-100,50)
    seth(-75)
    fd(40)
    circle(-100,10)
    seth(135)
    circle(10,70)
    seth(240)
    fd(50)
    seth(90)
    fd(100)
    seth(120)
    circle(100,50)
    fd(50)
    circle(43,70)
    end_fill()
    up()
    seth(170)
    #fd(30)
    goto(-50,250)
    down()
    begin_fill()
    color('black','lightsalmon')
    circle(70,197)
    fd(30)
    circle(30)
    circle(50,5)
    fd(170)
    seth(-40)
    circle(20,127)
    fd(35)
    circle(40,40)
    end_fill()
    up()
    begin_fill()
    color('black','lightsalmon')
    seth(90)
    #fd(30)
    goto(-50,250)
    fd(20)
    circle(-50,20)
    seth(70)
    circle(-100,90)
    seth(340)
    fd(20)
    circle(-100,50)
    seth(-75)
    fd(40)
    circle(-100,10)
    seth(135)
    circle(10,70)
    seth(240)
    fd(50)
    down()
    end_fill()

    up()
    seth(90)
    #fd(30)
    goto(-50,250)
    down()
    fd(20)
    circle(-50,20)
    begin_fill()
    color('black','black')
    seth(70)
    circle(-100,90)
    seth(340)
    fd(20)
    circle(-100,50)
    seth(-75)
    fd(40)
    circle(-100,10)
    seth(135)
    circle(10,70)
    seth(240)
    fd(50)
    seth(90)
    fd(100)
    seth(120)
    circle(100,50)
    fd(50)
    circle(43,70)
    end_fill()
    

    up()
    seth(170)
    goto(-50,250)
    down()
    circle(70,197)
    fd(30)
    begin_fill()
    color('black','brown')
    circle(30)
    end_fill()

face()
def eye():
    up()
    seth(0)
    #fd(30)
    goto(-50,230)
    fd(50)
    down()
    circle(25)
    up()
    goto(0,238)
    down()
    pensize(17)
    circle(16)
    pensize(3)
    up()
    seth(-6)
    fd(80)
    down()
    
    circle(25)
    up()
    goto(80,238)
    down()
    pensize(17)
    circle(16)
    pensize(3)
    up()
    seth(0)
    #fd(30)
    goto(-50,230)
    fd(45)
    circle(30,100)
    down()
    circle(30,190)
    up()
    seth(0)
    #fd(30)
    goto(-50,230)
    fd(128)
    circle(30,100)
    down()
    circle(30,190)
    up()
    seth(0)
    #fd(30)
    goto(-50,230)
    fd(75)
    seth(90)
    fd(65)
    down()
    seth(150)
    pensize(13)
    fd(35)
    seth(-150)
    fd(35)
    up()
    seth(0)
    #fd(30)
    goto(-50,230)
    fd(155)
    seth(90)
    fd(65)
    down()
    seth(150)
    pensize(13)
    fd(35)
    seth(-150)
    fd(35)

eye()

def body():
    up()
    seth(170)
    goto(-53,230)
    circle(70,75)
    seth(135) 
    pensize(3)
    down()
    fd(40)
    seth(-120)
    begin_fill()
    color('black','lightsalmon')
    fd(35)
    bk(28)
    seth(145)
    fd(15)
    seth(75)
    fd(10)
    circle(50,20)
    seth(130)
    circle(50,10)
    seth(-170)
    fd(25)
    bk(22)
    #fd(3)
    seth(110)
    fd(50)
    circle(5,170)
    fd(50)
    seth(135)
    fd(50)
    circle(5,170)
    fd(50)
    seth(100)
    circle(-9.5,120)
    seth(-170)
    fd(5)
    circle(8,180)
    fd(10)
    seth(-100)
    fd(10)
    up()
    seth(-170)
    fd(12)
    down()
    seth(95)
    fd(10)
    seth(140)
    fd(15)
    seth(-125)
    fd(3)
    circle(20,80)
    circle(8,190)
    seth(95)
    fd(10)
    seth(140)
    fd(13.5)
    seth(-125)
    fd(3)
    circle(20,30)
    seth(-140)
    fd(2)
    circle(18,80)
    circle(8,190)
    seth(-105)
    fd(5)
    circle(13,175)
    seth(-50)
    fd(22)
    end_fill()
    up()
    bk(44)
    begin_fill()
    color('black','lightsalmon')
    seth(-1)
    fd(14)
    seth(95)
    fd(10)
    seth(179)
    fd(12)
    end_fill()
    seth(-27)
    fd(80)
    down()
    seth(135) 
    pensize(3)
    down()
    begin_fill()
    color('black','red')
    fd(36)
    seth(-120)
    fd(35)
    circle(35,12)
    seth(-47)
    fd(140)
    seth(80)
    fd(15)
    bk(120)
    circle(-40,-30)
    seth(-11)
    circle(700,20)
    seth(93)
    fd(100)
    up()
    fd(97)
    seth(192)
    st()
    fd(181)
    seth(180)
    fd(20)
    circle(-70,100)
    end_fill()
    down()
    up()
    seth(135) 
    pensize(3)
    down()
    fd(36)
    seth(-120)
    fd(35)
    circle(35,12)
    seth(-47)
    fd(140)
    seth(80)
    fd(15)
    bk(120)
    circle(-40,-30)
    seth(-11)
    circle(700,20)
    seth(93)
    fd(100)
    down()
    up()
    seth(180)
    fd(20)
    seth(85)
    fd(50)
    down()
    seth(-95)
    fd(50)
    seth(0)
    fd(20)
    begin_fill()
    color('black','red')
    fd(50)
    seth(95)
    fd(74)
    circle(20,85)
    fd(18)
    seth(165)
    fd(15)
    #ht()
    end_fill()
    up()
    #st()
    seth(-15)
    fd(15)
    seth(-5)
    fd(18)
    circle(-20,85)
    fd(70)
    down()
    seth(-85)
    begin_fill()
    color('black','lightsalmon')
    circle(-80,30)
    seth(-95)
    fd(20)
    seth(-75)
    fd(20)
    circle(-5,60)
    #seth(-125)
    fd(20)
    circle(-5,170)
    seth(-150)
    circle(-5,170)
    seth(-150)
    circle(-5,170)
    fd(4)
    seth(150)
    circle(-5,110)
    fd(4)
    circle(8,55)
    fd(10)
    circle(70,18)
    circle(-95,15)
    end_fill()
    up()
    seth(-87)
    fd(100)
    down()
    #fd()
    seth(-83)
    fd(100)
    seth(181)
    fd(30)
    seth(-95)
    fd(110)
    bk(10)
    seth(-5)
    begin_fill()
    color('black','yellow')
    fd(7)
    seth(-87)
    fd(10)
    seth(-31)
    fd(35)
    seth(178)
    fd(60)
    seth(100)
    circle(-25,35)
    seth(2)
    fd(23)
    end_fill()
    bk(2.5)
    seth(85)
    begin_fill()
    color('black','white')
    fd(35)
    seth(240)
    circle(-30,57)
    seth(-85)
    fd(21)
    seth(2)
    fd(21)
    end_fill()
    up()
    seth(85)
    fd(35)
    seth(240)
    circle(-30,60)
    down()
    seth(95)
    begin_fill()
    color('black','lightsalmon')
    fd(90)
    seth(1)
    fd(37)
    up()
    seth(-95)
    fd(75)
    seth(240)
    circle(-30,56)
    down()
    end_fill()
    seth(95)
    fd(90)
    seth(181)
    fd(60)
    circle(-10,80)
    fd(20)
    seth(160)
    fd(20)
    bk(18)
    seth(-100)
    fd(29)
    seth(181)
    fd(40)
    seth(-95)
    fd(108)
    seth(-60)
    begin_fill()
    color('black','yellow')
    circle(-20,50)
    seth(182)
    fd(55)
    seth(35)
    fd(30)
    seth(87)
    fd(10)
    seth(2)
    fd(5)
    seth(-85)
    fd(10)
    seth(-2)
    fd(21)
    end_fill()
    seth(178)
    begin_fill()
    color('black','white')
    fd(21)
    seth(95)
    fd(35)
    seth(-60)
    circle(30,62)
    end_fill()
    seth(85)
    begin_fill()
    color('black','lightsalmon')
    fd(89)
    seth(181)
    fd(41)
    seth(-85)
    fd(77)
    end_fill()
    bk(77)
    seth(181)
    fd(42)
    seth(80)
    fd(110)
    #up()
    seth(-11)
    begin_fill()
    color('black','yellow')
    circle(700,20)
    seth(-83)
    fd(100)
    seth(181)
    fd(130)
    circle(-10,80)
    fd(20)
    seth(160)
    fd(20)
    bk(18)
    seth(-100)
    fd(29)
    seth(181)
    fd(126)
    seth(80)
    fd(110)    
    ht()
    end_fill()
    
body()    
done()
