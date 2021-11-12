# a121_catch_a_turtle.py
#-----import statements-----
from random import randrange
import turtle as trtl
import leaderboard as lb
#-----initialize turtle-----
bob = trtl.Turtle()
counter =  trtl.Turtle()
box = trtl.Turtle()
score_writer = trtl.Turtle()
#-----game configuration----
# leaderboard variables
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input ("Please enter your name:")
bob.color("pink")
bob.shape("square")
bob.shapesize(1)
bob.penup()
bob.speed(0)
font_setup = ("Arial", 20, "normal")
#-----game functions--------
def new_place():
  x = randrange(-200, 200)
  y = randrange(-200, 200)
  bob.goto(x, y)

score = 0
def bob_clicked(x, y):
  new_place()
  update_score_for_box(0, 0)

font_setup = ("Arial", 20, "normal")
def update_score_for_box(x,y):
  global score
  score += 1
  score_writer.clear()
  print(score_writer.write(score,font=font_setup))

score_writer.penup()
score_writer.goto(0, 220)

box.speed(0)
box.penup()
box.goto(0, 225)
box.pendown()
box.forward(50)
box.left(90)
box.forward(25)
box.left(90)
box.forward(100)
box.left(90)
box.forward(25)
box.left(90)
box.forward(50)
box.penup()
box.goto(0, 237.5)
box.forward(75)
box.right(45)
box.right(45)
box.forward(12.5)
box.left(45)
box.pendown()
box.circle(25,360,4)


timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

counter.penup()
counter.goto(77,225)
counter.pendown()
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("0", font=font_setup)
    box.color("white")
    bob.color("white")
    counter.color("white")
    manage_leaderboard()
    timer_up = True
  else:
    counter.write(" " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

#-----events----------------
# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global spot

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, bob, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, bob, score)

bob.onclick(bob_clicked)
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()


