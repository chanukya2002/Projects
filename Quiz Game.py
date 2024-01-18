class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question_number):
        question = self.questions[question_number]['question']
        options = self.questions[question_number]['options']
        print(f"\nQuestion {question_number + 1}: {question}")
        
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

    def get_user_answer(self):
        while True:
            try:
                user_answer = int(input("Enter the number of your answer: "))
                if 1 <= user_answer <= len(self.questions[0]['options']):
                    return user_answer
                else:
                    print("Invalid input. Please enter a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def check_answer(self, question_number, user_answer):
        correct_answer = self.questions[question_number]['correct_answer']
        if user_answer == correct_answer:
            print("Correct!")
            self.score += 1
        else:
            print(f"Incorrect. The correct answer is {correct_answer}.")

    def run_quiz(self):
        for i in range(len(self.questions)):
            self.display_question(i)
            user_answer = self.get_user_answer()
            self.check_answer(i, user_answer)

        print(f"\nYour final score is: {self.score}/{len(self.questions)}")


if __name__ == "__main__":
    quiz_questions = [
        {
            'question': 'What is the capital of France?',
            'options': ['Berlin', 'Madrid', 'Paris', 'Rome'],
            'correct_answer': 3
        },
        {
            'question': 'Which planet is known as the Red Planet?',
            'options': ['Mars', 'Jupiter', 'Venus', 'Saturn'],
            'correct_answer': 1
        },
        {
            'question': 'What is the largest mammal in the world?',
            'options': ['Elephant', 'Blue Whale', 'Giraffe', 'Hippopotamus'],
            'correct_answer': 2
        }
    ]

    quiz = Quiz(quiz_questions)
    quiz.run_quiz()
