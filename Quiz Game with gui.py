import tkinter as tk
from tkinter import messagebox
import random

class QuizGUI:
    def __init__(self, master, questions):
        self.master = master
        self.questions = questions
        self.score = 0
        self.current_question = 0
        self.shuffle_questions()

        self.label_question = tk.Label(master, text="")
        self.label_question.pack(pady=10)

        self.radio_var = tk.StringVar()
        self.radio_buttons = []
        for i in range(4):
            radio_button = tk.Radiobutton(master, text="", variable=self.radio_var, value=str(i+1))
            radio_button.pack(anchor=tk.W)
            self.radio_buttons.append(radio_button)

        self.next_button = tk.Button(master, text="Next", command=self.next_question)
        self.next_button.pack(pady=10)

        self.display_question()

    def shuffle_questions(self):
        random.shuffle(self.questions)

    def display_question(self):
        question_data = self.questions[self.current_question]
        self.label_question.config(text=question_data['question'])

        for i, option in enumerate(question_data['options']):
            self.radio_buttons[i].config(text=option)

    def next_question(self):
        user_answer = self.radio_var.get()

        if user_answer:
            user_answer = int(user_answer)
            correct_answer = self.questions[self.current_question]['correct_answer']

            if user_answer == correct_answer:
                messagebox.showinfo("Correct!", "Your answer is correct!")
                self.score += 1
            else:
                correct_option = self.questions[self.current_question]['options'][correct_answer - 1]
                messagebox.showinfo("Incorrect", f"Wrong answer!\nCorrect answer: {correct_option}")

            self.current_question += 1
            self.radio_var.set("")  # Clear radio button selection

            if self.current_question < len(self.questions):
                self.display_question()
            else:
                messagebox.showinfo("Quiz Completed", f"Your final score is: {self.score}/{len(self.questions)}")
                self.master.destroy()

        else:
            messagebox.showwarning("Warning", "Please select an answer.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quiz Game")

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
        },
        {
            'question': 'Which country is known as the Land of the Rising Sun?',
            'options': ['China', 'Japan', 'South Korea', 'Vietnam'],
            'correct_answer': 2
        },
        {
            'question': 'What is the capital of Australia?',
            'options': ['Canberra', 'Sydney', 'Melbourne', 'Brisbane'],
            'correct_answer': 1
        },
        {
            'question': 'Who wrote the play "Romeo and Juliet"?',
            'options': ['William Shakespeare', 'Jane Austen', 'Charles Dickens', 'Emily Bronte'],
            'correct_answer': 1
        },
        {
            'question': 'What is the largest ocean on Earth?',
            'options': ['Atlantic Ocean', 'Indian Ocean', 'Southern Ocean', 'Pacific Ocean'],
            'correct_answer': 4
        },
        {
            'question': 'Which element has the chemical symbol "O"?',
            'options': ['Oxygen', 'Gold', 'Iron', 'Silver'],
            'correct_answer': 1
        },
    ]

    app = QuizGUI(root, quiz_questions)
    root.mainloop()
