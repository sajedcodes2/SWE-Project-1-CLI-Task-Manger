import datetime


def start_quiz():

    score_tracker = 0
    score_tracker += 1

    # Display question and choices
    # Collect user answer
    # Check the answer
    # Update score

    for i, question in enumerate(questions, start=1):
        print(f"Question {i}: {question['question']}")

        for number, choice in enumerate(question["choices"], start=1):
            print(f"{number}) {choice}")

        user_answer = input("Choose an answer (1-4): ")
        user_answer = int(user_answer)
        if user_answer - 1 == question["answer_index"]:
            print()
            print("Correct!")
            score_tracker += 1
        else:
            print("Incorrect!")
        print()
    print(f"Your final score is {score_tracker}/{len(questions)}")

    print()

    percentage = (score_tracker / len(questions)) * 100
    print(f"Your score percentage is : {percentage:.0f}%\n")
    print("Check out the high scores to see if you made the leaderboard!\n")

    if len(high_scores) < 3:
        add_high_score(percentage)

    else:
        lowest_score = min(high_scores, key=lambda player: player["score"])

        if percentage > lowest_score["score"]:
            add_high_score(percentage)
        else:
            print("Sorry, you didn't make the top 3.")


# Questions is for the entire list of questions
# Questions is one dictionary from that list

questions = [
    {
        "question": "What is Capital of New York State?",
        "choices": ["Albany", "Flint", "Bronx", "New Haven"],
        "answer_index": 0,
    },
    {
        "question": "What is Capital of Georgia ?",
        "choices": ["Atlanta", "Flint", "Bronx", "New Haven"],
        "answer_index": 0,
    },
    {
        "question": "What is Capital of Delaware ?",
        "choices": ["Wilmington", "Flint", "Bronx", "New Haven"],
        "answer_index": 1,
    },
    {
        "question": "What is Capital of Texas ?",
        "choices": ["Bronx", "Brooklyn ", "Austin", "Bronx", "New Haven"],
        "answer_index": 2,
    },
]

high_scores = [{"name": "Ace", "score": 75, "date": "11/12/26"}]


def add_high_score(percentage):
    player_name = input("Enter your name: ")
    today = datetime.date.today().strftime("%m/%d/%y")

    new_score = {"name": player_name, "score": percentage, "date": today}
    high_scores.append(new_score)
    high_scores.sort(key=lambda player: player["score"], reverse=True)
    high_scores[:] = high_scores[:3]


def check_high_scores():
    print("Total scores:", len(high_scores))
    if len(high_scores) == 0:
        print("No high scores yet. Be the first to make the leaderboard!")
    else:
        print("HIGH SCORES")
        for player in high_scores:
            print(
                f"Player: {player['name']} | Score: {player['score']}% | Date: {player['date']}"
            )
