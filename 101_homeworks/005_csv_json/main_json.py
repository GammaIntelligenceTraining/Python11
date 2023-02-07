import json


with open('data/quiz.json', 'r', encoding='UTF8') as file:
    quiz_data = json.load(file)


# function that takes list of answers as an argument
# returns answer picked by user as a string
def answer_question(question):
    while True:
        print(f'1. {question[0]}  2. {question[1]}\n3. {question[2]}  4. {question[3]}')

        user_choice = input('What is your answer? -> ')
        if user_choice.lower() == 'exit':
            print('Good bye')
            quit()
        if user_choice in '1234':
            return question[int(user_choice) - 1]

        else:
            print('Choice out of range. Try again or type "exit" to quit.')
            continue


def check_answer(answer, user_answer):
    if user_answer == answer:
        return True
    else:
        return False


def ask_questions(topic, data):
    quiz = data['quiz'][topic]
    score = 0
    for question in quiz.values():
        print(question.get('question'))
        user_answer = answer_question(question.get("options"))
        if check_answer(user_answer, question.get("answer")):
            score += 1
    print(f'You answered {score} questions right.')


def quiz(data):
    print('Hello. Welcome to our quiz!')
    print(f'You can choose from {len(data.get("quiz").keys())} ')
    cnt = 1
    for topic in data.get("quiz").keys():
        print(f'{cnt}. {topic}')
        cnt += 1
    print()
    while True:
        quiz_topic = input('Type topic name to continue or "exit" to quit.')
        if quiz_topic.lower() == 'exit':
            print('Good bye')
            quit()
        if quiz_topic.lower() in data.get('quiz').keys():
            ask_questions(quiz_topic, data)
            if input('Another quiz? y/n ').lower() == 'y':
                quiz(data)
                break
            else:
                print('Good bye!')
                quit()
        else:
            print(f'There is no {quiz_topic}')

# ask_questions('sport', quiz_data)
quiz(quiz_data)