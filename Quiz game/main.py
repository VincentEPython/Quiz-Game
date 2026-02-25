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

index = 1
score = 0
time_left = 10
marquee_message = ""
is_game_over = False
question_count = 0 # total of questions
question_index = 0 # current question
questions = [] # adding each line as a list item

def draw():
    global marquee_message, index
    screen.clear()
    screen.fill("navy blue")
    screen.draw.filled_rect(marquee_box,"black")
    screen.draw.filled_rect(question_box,"black")
    screen.draw.filled_rect(timer_box,"blue")
    screen.draw.filled_rect(skip_box,"dark green")
    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box,"green")
    
    # adding textbox in rectangle
    marquee_message = f"Welcome to the quiz game.You are at Q: {question_index} out of {question_count}"
    screen.draw.textbox(marquee_message,marquee_box,color = "white")
    screen.draw.textbox(str(time_left),timer_box,color = "white", shadow = (0.5,0.5),scolor = "light grey")
    screen.draw.textbox("SKIP",skip_box,color = "white",shadow = (0.5,0.5),scolor = "dim grey")
    screen.draw.textbox(question[0].strip(),question_box,color = "white")

    # adding text to answer boxes
    
    index = 1
    for answerbox in answer_boxes:
        screen.draw.textbox(question[index].strip(),answerbox,color = "white")
        index = index+1


def read_questions_from_file():

    global question_count,question_index,questions
    #opening questions.txt file 
    # the "r" specifies the read mode 
    question_file = open("questions.txt","r")

    # reading each row of the file one by one
    for row in question_file:
        questions.append(row)
        question_count +=1
    question_file.close()
    
def move_marquee():
    marquee_box.x -= 2
    if marquee_box.right < 0 :
        marquee_box.left = WIDTH

def update():
    move_marquee()

def read_next_question():
    global question_index
    question_index += 1
    question = questions.pop(0).split(",") 
    # .pop(0) is deleting the zeroth index an split is splitting that index multiple packages making the question
    #variable a list
    return question

def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            if index is int(question[5]):
                correct_answer()
            else:
                game_over_func()
        index = index +1
    if skip_box.collidepoint(pos):
        skip_question()


def correct_answer():
    global score,question,time_left,questions
    score = score +1
    # this part of the code means if there are any questions left then read the next one and reset the timer
    if questions:
        question = read_next_question()
        time_left = 10
    else:
        game_over_func()     

def game_over_func():
    global question,time_left,is_game_over
    message = f"Game Over!!, You got {score} questions correct!" 
    question = [message,"-","-","-","-",5]
    time_left = 0
    is_game_over = True

def skip_question():
    global question, time_left
    if questions and not is_game_over:
        question = read_next_question()
        time_left = 10
    else:
        game_over_func()
    

def update_time_left():
    global time_left
    if time_left:
        time_left = time_left -1
    else:
        game_over_func()

                
read_questions_from_file()
question = read_next_question()
print(question)
clock.schedule_interval(update_time_left,1)

pgzrun.go()
