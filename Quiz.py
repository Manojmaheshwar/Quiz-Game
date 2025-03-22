import random
import sys

questions = [
    {
        "question": "What does the term 'phishing' refer to?",
        "options": ["A) Fishing techniques", "B) Hacking a database", "C) Tricking someone to reveal sensitive information", "D) Encrypting data"],
        "answer": "C"
    },
    {
        "question": "What is the main purpose of a firewall?",
        "options": ["A) Block malware", "B) Monitor network traffic", "C) Prevent unauthorized access", "D) Encrypt communications"],
        "answer": "C"
    },
    {
        "question": "Which of the following is considered a strong password?",
        "options": ["A) 123456", "B) Password123", "C) $tr0ngP@ss!", "D) admin"],
        "answer": "C"
    },
    {
        "question": "What is a DDoS attack?",
        "options": ["A) Data destruction over servers", "B) Distributed Denial of Service", "C) Direct denial of services", "D) Data duplication over system"],
        "answer": "B"
    },
    {
        "question": "What does SSL stand for?",
        "options": ["A) Secure Sockets Layer", "B) System Security Lock", "C) Server Secure Layer", "D) Secure System Layer"],
        "answer": "A"
    }
]

def display_intro():
    print("🔐 Welcome to the Cybersecurity Quiz Game! 🔐")
    print("Test your cybersecurity knowledge with multiple-choice questions.")
    print("Type the correct option (A, B, C, or D) and hit Enter. Type 'exit' to quit.")
    print("-" * 50)

def ask_question(question):
    print("\n" + question["question"])
    for option in question["options"]:
        print(option)
    answer = input("Your answer (A, B, C, D): ").strip().upper()

    if answer == "EXIT":
        print("Exiting the game. Stay secure! 🔒")
        sys.exit()

    return answer == question["answer"]

def start_game():
    display_intro()
    score = 0
    random.shuffle(questions)

    for question in questions:
        if ask_question(question):
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {question['answer']}.")

    print("\nGame Over! 🎮")
    print(f"Your final score is: {score}/{len(questions)}")
    if score == len(questions):
        print("🏆 Excellent! You're a cybersecurity pro!")
    elif score >= len(questions) // 2:
        print("👍 Good job! Keep learning!")
    else:
        print("📚 Keep studying to strengthen your cybersecurity knowledge!")

if __name__ == "__main__":
    start_game()
