import turtle
import pandas

screen = turtle.Screen()

screen.title("U.S states game")
image = "C:\\Users\\ROHIT\\Desktop\\100 Days Python\\day_25\\us-states-game-start\\us-states-game-start\\blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

# data collection
data = pandas.read_csv("C:\\Users\\ROHIT\\Desktop\\100 Days Python\\day_25\\us-states-game-start\\us-states-game-start\\50_states.csv")
all_states = data["state"].tolist()

guessed_states = []


while len(guessed_states) < 50:
    answer_state = str(screen.textinput(title=f"{len(guessed_states)}/50 States correct",prompt="What's another states name:")).title
    if answer_state == "Exit":
        missing_states = []
        for states in all_states:
            if states not in guessed_states:
                guessed_states.append(states)
        # new_data = pandas.DataFrame(missing_states)
        # new_data.to_csv("states_to_learn.csv")
        print(missing_states)
        break
    
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x) , int(state_data.y)) # type: ignore
        t.write(answer_state)
    
