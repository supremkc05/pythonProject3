#kaun banega crorepati
class KBC:
    def __init__(self):
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["A. London", "B. Paris", "C. Rome", "D. Berlin"],
                "answer": "B"
            },
            {
                "question": "Who is the top scoreer of 2023?",
                "options": ["A. Cristiano Ronaldo", "B. Earling Haaland", "C. kelian Embapppe", "D. HArry KAne"],
                "answer": "A"
            },
            #  to add more questions similarly
        ]
        self.prize_money = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000]
        self.total_questions = len(self.questions)
        self.current_question = 0
        self.money_won = 0

    def display_question(self):
        current = self.questions[self.current_question]
        print(f"Question {self.current_question + 1}: {current['question']}")
        for option in current['options']:
            print(option)
        return input("Your answer (Enter A, B, C, or D): ").upper()

    def play_game(self):
        print("Welcome to Kaun Banega Crorepati!")
        print("You will be presented with multiple-choice questions. Choose the correct answer to win money.")
        print("Let's start:")
        while self.current_question < self.total_questions:
            user_answer = self.display_question()
            correct_answer = self.questions[self.current_question]['answer']
            if user_answer == correct_answer:
                print("Correct Answer!")
                self.money_won = self.prize_money[self.current_question]
                print(f"Congratulations! You've won ₹{self.money_won}")
                self.current_question += 1
            else:
                print("Incorrect Answer! Game Over!")
                break

        print(f"Total amount won: ${self.money_won}")

if __name__ == "__main__":
    game = KBC()
    game.play_game()
