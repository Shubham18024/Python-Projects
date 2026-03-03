import turtle
import pandas as pd


def setup_screen():
    screen = turtle.Screen()
    screen.title("U.S. State Game")
    screen.bgpic("blank_states_img.gif")
    screen.bgcolor("cyan")
    screen.setup(width=760, height=510)
    return screen


def setup_writer():
    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()
    return writer


def play_game(screen, writer, state_data):

    state_list = state_data.state.to_list()
    guessed_states = []

    while len(guessed_states) < 50:
        answer = screen.textinput(
            title=f"{len(guessed_states)}/50 States Correct",
            prompt="What's another state's name? (Type 'Exit' to quit)"
        )

        if answer is None:
            break  # user pressed cancel

        answer = answer.title()

        if answer == "Exit":
            break

        if answer in state_list and answer not in guessed_states:
            row = state_data[state_data.state == answer].iloc[0]

            writer.goto(row.x, row.y)
            writer.write(answer, font=("Arial", 12, "normal"))

            guessed_states.append(answer)

    print("Game Over")
    return guessed_states

def save_missed_states(state_data, guessed_states):
    missed_states = [state for state in state_data.state if state not in guessed_states]
    missed_data = pd.DataFrame(missed_states, columns=["state"])
    missed_data.to_csv("missed_states.csv", index=False)

def main():
    screen = setup_screen()
    writer = setup_writer()
    state_data = pd.read_csv("50_states.csv")

    guessed_states = play_game(screen, writer, state_data)
    save_missed_states(state_data, guessed_states)
    screen.exitonclick()  

if __name__ == "__main__":
    main()