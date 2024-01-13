q_a = {
    "question1": {
        "question": "What is the capital of France?",
        "answer": "Paris",
    },
    
    "question2": {
        "question": "What is the largest planet in our solar system?",
        "answer": "Jupiter",
    },

    "question3": {
        "question": "Who wrote 'Romeo and Juliet'?",
        "answer": "Shakespeare"
    }
}


print("Welcome to my quiz!")
score = 0
for key, value in q_a.items():
    
    print(value["question"])
    answer = input("Answer: ")
    if answer.lower() == value["answer"].lower():
        score += 1
        print("Correct! \n")
    else:
        print("Incorrect.")
        print(f"The answer is: {value['answer']}\n")

print(f"Your Score is: {score} / 3")