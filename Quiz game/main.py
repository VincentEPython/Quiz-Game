import os

x=50
y=50

os.environ["SDL_VIDEO_WINDOW_POS"] = f"{x},{y}"

import pgzrun

WIDTH = 870
HEIGHT = 630


marquee_box = Rect(0,0,880,80)
question_box = Rect(0,0,650,150)
timer_box = Rect(0,0,150,150)
answer_box1 = Rect(0,0,300,150)
answer_box2 = Rect(0,0,300,150)
answer_box3 = Rect(0,0,300,150)
answer_box4 = Rect(0,0,300,150)
skip_box = Rect(0,0,150,330)


question_box.move_ip(20,100)
timer_box.move_ip(700,100)
answer_box1.move_ip(20,270)
answer_box2.move_ip(370,270)
answer_box3.move_ip(20,450)
answer_box4.move_ip(370,450)
skip_box.move_ip(700,270)
answer_boxes = [answer_box1,answer_box2,answer_box3,answer_box4]

score = 0
time_left = 10
marquee_message = ""
game_over = False
question_count = 0 # total of questions
question_index = 0 # current question
questions = [] # adding each line as a list item

def read_questions_from_file():
    global question_count,question_index,questions
    #opening questions.txt file
    question_file = open("questions.txt","r")

    # reading each row of the file one by one
    for row in question_file:
        questions.append(row)
        question_count +=1
    question_file.close()

def draw():
    screen.fill("navy blue")
    screen.draw.filled_rect(marquee_box,"black")
    screen.draw.filled_rect(question_box,"black")
    screen.draw.filled_rect(timer_box,"blue")
    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box,"green")
    screen.draw.filled_rect(skip_box,"dark green")
    
    # adding textbox in rectangle
    message = f"Welcome to the quiz game.You are at Q: {question_index} out of {question_count}"
    screen.draw.textbox(message,marquee_box,color = "white")
    screen.draw.textbox(str(time_left),timer_box,color = "white", shadow = (0.5,0.5),scolor = "light grey")
    screen.draw.textbox("SKIP",skip_box,color = "white",shadow = (0.5,0.5),scolor = "dim grey")
 
read_questions_from_file()

pgzrun.go()
