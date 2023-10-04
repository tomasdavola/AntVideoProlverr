from manim import *
import manim
import time
import random
# manim.config.save_last_frame = True

def gen_points():
    group = Group()
    for i in range(50):
        point = Point(location=[random.uniform(-2.5, 2.5) * 1, random.uniform(-1.4, 1.4) * 1, 0], color=RED)
        group.add(point)
    return group

class CreateCircle(Scene):
    def construct(self):
        circle = Rectangle(color='#000000', height=2.0, width=4.0)  # create a circle
        circle.set_fill(PINK, opacity=0.5)
        self.play(Create(circle))

class RectangleExample(Scene):
    def construct(self):
        #Rectangle cration
        rect2 = Rectangle(width=6.0, height=3.0)
        self.play(Create(rect2))
        self.wait(5)
        one_m=BraceText(rect2, "1 Meter")
        self.play(Create(one_m))
        self.add(one_m)
        self.wait(5)

        #Ant Creation
        left = gen_points()
        right = gen_points()
        self.play(FadeIn(left))
        print(left)
        self.wait(5)

        #Arrows
        arrow_3 = Arrow(start=LEFT, end=RIGHT, buff=25).move_to([3, 3, 0])
        arrow_4 = Arrow(start=RIGHT, end=LEFT, buff=25).move_to([-3,3,0])
        self.play(Create(arrow_4))
        self.play(Create(arrow_3))
        self.wait(5)

        #Movement
        t1=left.animate.shift([5,0,0])
        t2=right.animate.shift([-5, 0, 0])
        self.play(t1,t2,rate_func=linear)
        self.wait(5)

        uncreates=[Uncreate(rect2), Uncreate(one_m),Uncreate(arrow_4),Uncreate(arrow_3)]
        self.play(Uncreate(rect2), Uncreate(one_m),Uncreate(arrow_4),Uncreate(arrow_3), FadeOut(left), FadeOut(right))

class CloseUpAnt(Scene):
    def construct(self):
        ant1 = ImageMobject("assets/ant.png").move_to([-5, 0, 0]).scale(0.3)
        ant2 = ImageMobject("assets/ant2.png").move_to([5, 0, 0]).scale(0.3)
        self.play(FadeIn(ant1,ant2))
        self.wait(1.5)
        l1 = Line([-5, 0, 0],[-0.1, 0, 0])
        l2 = Line([5, 0, 0], [0.1, 0, 0])
        self.play(MoveAlongPath(ant1, l1), MoveAlongPath(ant2, l2), rate_func=linear)
        self.play(ant1.animate.flip(Y_AXIS), ant2.animate.flip(Y_AXIS))
        l1 = Line([-0.1, 0, 0], [-5, 0, 0])
        l2 = Line([0.1, 0, 0], [5, 0, 0])
        self.play(MoveAlongPath(ant1, l1), MoveAlongPath(ant2, l2), rate_func=linear)
        self.wait(0.7)
        self.play(FadeOut(ant1,ant2))

        # self.play(Create(ant1))

class Hint3(Scene):
    def construct(self):
        ant1 = ImageMobject("assets/ant.png").move_to([-5, 0, 0]).scale(0.3)
        ant2 = ImageMobject("assets/ant2.png").move_to([5, 0, 0]).scale(0.3)
        self.add(ant1,ant2)
        self.wait(0.5)
        l1 = Line([-5, 0, 0],[0, 0, 0])
        l2 = Line([5, 0, 0], [0, 0, 0])
        self.play(MoveAlongPath(ant1, l1).set_run_time(2), MoveAlongPath(ant2, l2).set_run_time(2), rate_func=linear)
        self.remove(ant1,ant2)
        ant1 = ImageMobject("assets/ant.png").move_to([0, 0, 0]).scale(0.3)
        ant2 = ImageMobject("assets/ant2.png").move_to([0, 0, 0]).scale(0.3)
        self.add(ant1,ant2)
        l1 = Line([0, 0, 0], [-5, 0, 0])
        l2 = Line([0, 0, 0], [5, 0, 0])
        self.play(MoveAlongPath(ant2, l1).set_run_time(2), MoveAlongPath(ant1, l2).set_run_time(2), rate_func=linear)
        self.wait(0.5)
        # self.play(Create(ant1))

class QuestionMark(Scene):
    def construct(self):
        questionM = Text('?').scale(5)
        self.play(Write(questionM).set_run_time(1.5))
        self.wait(0.5)
        new_questionM =  Text('?').scale(2.5).move_to([-6.3, 3, 0])
        self.play(Transform(questionM, new_questionM))
        question = Text("Over all possible configurations what is the longest amount of time \nyou would need to wait to guarantee that the table has no more ants?", should_center=True).scale(0.5).move_to([0,0.5,0])
        self.play(Write(question).set_run_time(6))
        self.wait(1)
        or_text = Text("or").scale(0.5).move_to([0,-0.5,0])
        self.play(FadeIn(or_text))
        self.wait(1)
        new_question = Text("What is the longest time the ants would take to walk off the table?").scale(0.5).move_to([0,-1,0])
        self.play(Write(new_question).set_run_time(3))
        self.wait(5)

class Rules(Scene):
    def construct(self):
        rules = Text('Rules:').scale(1).move_to([-5, 3, 0])
        self.play(Write(rules).set_run_time(1.5))

        rule1 = Text('1. Table is 1 meter long.').move_to([-1, 2, 0])
        rule2 = Text('2. There are 100 ants, each facing either left or right.').move_to([-1, 1, 0])
        rule3 = Text('3. Collisions are instant, ants keep their speed of 1 meter per minute.').move_to([-1, 0, 0])
        rule4 = Text('4. What is the longest time the ants would take to walk off the table?').move_to([-1, -1, 0])
        rule5 = Text('5. Treat ants as points.').move_to([-1, -2, 0])
        x = VGroup(rule1, rule2, rule3, rule4, rule5).arrange(direction=DOWN, aligned_edge=LEFT).scale(0.7)
        self.play(DrawBorderThenFill(x).set_run_time(2.5))
        question = Text("Over all possible configurations what is the longest amount of time \nyou would need to wait to guarantee that the table has no more ants?", should_center=True).scale(0.5).move_to([0,0.5,0])
        # self.play(Write(question).set_run_time(6))
        # self.wait(1)
        # or_text = Text("or").scale(0.5).move_to([0,-0.5,0])
        # self.play(FadeIn(or_text))
        # self.wait(1)
        # new_question = Text("What is the longest time the ants would take to walk off the table?").scale(0.5).move_to([0,-1,0])
        # self.play(Write(new_question).set_run_time(3))
        self.wait(100)

class idleCrawl(Scene):
    def construct(self):
        ant1 = ImageMobject("assets/ant.png").move_to([-5.17, 1, 0]).scale(0.15)
        ant2 = ImageMobject("assets/ant2.png").move_to([4.3, 0.5, 0]).scale(0.15)
        ant3 = ImageMobject("assets/ant.png").move_to([-5, 0, 0]).scale(0.15)
        ant4 = ImageMobject("assets/ant2.png").move_to([5.5, -0.5, 0]).scale(0.15)
        ant5 = ImageMobject("assets/ant.png").move_to([-5, -1, 0]).scale(0.15)
        ant6 = ImageMobject("assets/ant2.png").move_to([4.5, -1.5, 0]).scale(0.15)
        self.play(FadeIn(ant1,ant2,ant3,ant4,ant5,ant6))
        l1 = Line([-5.17, 1, 0], [5.17, 1, 0])
        l2 = Line([4.3, 0.5, 0], [-4.5, 0.5, 0])
        l3 = Line([-5, 0, 0], [5, 0, 0])
        l4 = Line([5.5, -0.5, 0], [-3.7, -0.5, 0])
        l5 = Line([-5, -1, 0], [4.7, -1, 0])
        l6 = Line([4.5, -1.5, 0], [-4.5, -1.5, 0])
        self.play(MoveAlongPath(ant1,l1).set_run_time(6), MoveAlongPath(ant2,l2).set_run_time(8), MoveAlongPath(ant3,l3).set_run_time(7), MoveAlongPath(ant4,l4).set_run_time(12), MoveAlongPath(ant5,l5).set_run_time(4), MoveAlongPath(ant6,l6).set_run_time(8), rate_func=linear)
        self.wait(5)

class Solution(Scene):
    def construct(self):
        ant1 = ImageMobject("assets/ant.png").move_to([-5, 2, 0]).scale(0.3)
        ant2 = ImageMobject("assets/ant2.png").move_to([5, 2, 0]).scale(0.3)
        ant3 = ImageMobject("assets/ant.png").move_to([-5, -2, 0]).scale(0.3)
        ant4 = ImageMobject("assets/ant2.png").move_to([5, -2, 0]).scale(0.3)
        self.play(FadeIn(ant1, ant2, ant3, ant4))
        self.wait(0.7)
        self.play(ant1.animate.shift([5,0,0]), ant2.animate.shift([-5,0,0]), ant3.animate.shift([5,0,0]), ant4.animate.shift([-5,0,0]), rate_func=linear)
        self.remove(ant1,ant2)
        ant1 = ImageMobject("assets/ant.png").move_to([0,2,0]).scale(0.3)
        ant2 = ImageMobject("assets/ant2.png").move_to([0,2,0]).scale(0.3)
        self.add(ant1,ant2)
        self.play(ant1.animate.shift([5, 0, 0]), ant2.animate.shift([-5, 0, 0]), ant3.animate.shift([5, 0, 0]),ant4.animate.shift([-5, 0, 0]), rate_func=linear)
        self.wait(9)

class Thumbnail(Scene):
    def construct(self):
        ant1 = ImageMobject("assets/ant.png").scale(2)
        self.add(ant1)

class pfp(Scene):
    def construct(self):
        ant1 = MathTex(r"\varphi \vartheta").scale(5)
        self.add(ant1)

class Baner(Scene):
    def construct(self):
        ant1 = Text("Math puzzles with no math")
        ant2 = ImageMobject("assets/ant.png").rotate(70).move_to([3,0.7,0]).scale(0.15)
        ant3 = ImageMobject("assets/ant.png").rotate(270).move_to([3, -0.7, 0]).scale(0.15)
        self.add(ant1)
        self.add(ant2)
        self.add(ant3)
        ant2 = ImageMobject("assets/ant.png").rotate(140).move_to([-3,0.7,0]).scale(0.15)
        ant3 = ImageMobject("assets/ant.png").rotate(-800).move_to([-1, -0.7, 0]).scale(0.15)
        self.add(ant2)
        self.add(ant3)

class QuestionMarkShort(Scene):
    def construct(self):
        # questionM = Text('?').scale(5)
        # self.play(Write(questionM).set_run_time(0.5))
        # new_questionM =  Text('?').scale(2.5).move_to([-6.3, 3, 0])
        new_question = Text("Thanks for watching!").scale(1)
        self.play(Write(new_question).set_run_time(2))
        self.wait(5)