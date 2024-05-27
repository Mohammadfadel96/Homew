# Type python quiz program that takes a text or json or csv file as input for (20 (Questions, Answers)).
# It asks the questions and finally computes and prints user results
# and store user name and result in separate file csv or json file.
import json
def load_questions(f_name):
    with open(f_name, 'r') as file:
        data = json.load(file)
    return data["Questions"]
def quiz(questions):
    score = 0
    total_questions = len(questions)
    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['Question']}")
        user_answer = input("your answer: ")
        if user_answer.lower() == q['Answer'].lower():
            score += 1
    return score, total_questions
def main():
    questions = load_questions('c:/Users/Techno.Home/Desktop/quiz.json')
    user_name = input("enter your name !\n")
    score, total_questions = quiz(questions)
    result = {
        'name': user_name,
        'score': score,
        'total_questions': total_questions
    }
    with open('c:/Users/Techno.Home/Desktop/user_result.json', 'w') as file:
        json.dump(result, file, indent=4)
    print(f"Finished !\nyour score is {score}/{total_questions}")
if __name__ == "__main__":
    main()
