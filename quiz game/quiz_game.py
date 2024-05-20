import random

quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "C"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["A. Charles Dickens", "B. J.K. Rowling", "C. Mark Twain", "D. William Shakespeare"],
        "answer": "D"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["A. Gold", "B. Oxygen", "C. Osmium", "D. Oxide"],
        "answer": "B"
    },
    {
        "question": "What is the square root of 64?",
        "options": ["A. 6", "B. 7", "C. 8", "D. 9"],
        "answer": "C"
    },
    {
        "question": "In which year did the Titanic sink?",
        "options": ["A. 1910", "B. 1911", "C. 1912", "D. 1913"],
        "answer": "C"
    },
    {
        "question": "What is the capital of Japan?",
        "options": ["A. Seoul", "B. Tokyo", "C. Beijing", "D. Bangkok"],
        "answer": "B"
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
        "answer": "B"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["A. Vincent Van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Claude Monet"],
        "answer": "C"
    },
    {
        "question": "What is the chemical formula for water?",
        "options": ["A. CO2", "B. H2O", "C. O2", "D. NaCl"],
        "answer": "B"
    },
    {
        "question": "What is the capital of Italy?",
        "options": ["A. Rome", "B. Venice", "C. Milan", "D. Naples"],
        "answer": "A"
    },
    {
        "question": "What is the largest mammal?",
        "options": ["A. Elephant", "B. Whale", "C. Shark", "D. Giraffe"],
        "answer": "B"
    },
    {
        "question": "Who discovered penicillin?",
        "options": ["A. Marie Curie", "B. Albert Einstein", "C. Alexander Fleming", "D. Isaac Newton"],
        "answer": "C"
    },
    {
        "question": "What is the capital of Canada?",
        "options": ["A. Toronto", "B. Ottawa", "C. Vancouver", "D. Montreal"],
        "answer": "B"
    },
    {
        "question": "What is the smallest country in the world?",
        "options": ["A. Monaco", "B. Vatican City", "C. San Marino", "D. Liechtenstein"],
        "answer": "B"
    },
    {
        "question": "What is the tallest mountain in the world?",
        "options": ["A. K2", "B. Kangchenjunga", "C. Mount Everest", "D. Lhotse"],
        "answer": "C"
    },
    {
        "question": "Who wrote '1984'?",
        "options": ["A. Aldous Huxley", "B. George Orwell", "C. J.R.R. Tolkien", "D. Ernest Hemingway"],
        "answer": "B"
    },
    {
        "question": "What is the boiling point of water?",
        "options": ["A. 50°C", "B. 75°C", "C. 100°C", "D. 150°C"],
        "answer": "C"
    },
    {
        "question": "What is the longest river in the world?",
        "options": ["A. Nile", "B. Amazon", "C. Yangtze", "D. Mississippi"],
        "answer": "A"
    },
    {
        "question": "What is the capital of Australia?",
        "options": ["A. Sydney", "B. Melbourne", "C. Canberra", "D. Brisbane"],
        "answer": "C"
    }
]

def ask_question(question_data):
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)
    answer = input("Your answer (A, B, C, D): ").upper()
    while answer not in ['A', 'B', 'C', 'D']:
        print("Invalid input. Please enter A, B, C, or D.")
        answer = input("Your answer (A, B, C, D): ").upper()
    return answer

def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer

def run_quiz(quiz_questions):
    score = 0
    selected_questions = random.sample(quiz_questions, 10)
    for question_data in selected_questions:
        user_answer = ask_question(question_data)
        if check_answer(user_answer, question_data["answer"]):
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer is {question_data['answer']}.")
        print()
    total_questions = len(selected_questions)
    percentage = (score / total_questions) * 100
    print(f"Your final score is {score}/{total_questions}.")
    print(f"Your score percentage is {percentage:.2f}%.")

def main():
    print("Welcome to the Basic Quiz Game!")
    run_quiz(quiz_questions)

if __name__ == "__main__":
    main()
