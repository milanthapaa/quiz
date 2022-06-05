import time
from pytimedinput import timedInput


def quiz():
    print("Welcome to KO HUNCHA LAKHPATI.")
    time.sleep(3)
    print(
        "You'll be asked series of question try to answer the question before "
        "10 seconds else you'll not get point for that question.")
    time.sleep(5)
    points = 0
    questions = [
        "Where is highest mountain located? ",
        "Which is the best programming language? ",
        "In which city would you find the world’s tallest building? ",
        "With an average altitude of 1.56 miles, "
        "what is the highest continent? ",
        "Growing up to 18 meters long, "
        "which is the world’s largest living fish? ",
        "Aside from other humans, which animal is responsible? "
        "for the most human fatalities? ",
        "Which of these animals swims in an upright position? ",
        "What gives flamingos their pink color? ",
        "Who coined the term \"Cold War\"? ",
        "What is the nation animal of Nepal? "
    ]
    answers = [
        'nepal',
        "python",
        "dubai",
        "antarctica",
        "whale fish",
        "mosquito",
        "seahorse",
        "diet",
        "george orwell",
        "cow"

    ]

    for index, question in enumerate(questions):
        ask_user = timedInput(question, timeout=10)
        user_answers = list(ask_user)[0]
        if user_answers.lower() == answers[index].lower():
            points += 1


if __name__ == "__main__":
    quiz()
