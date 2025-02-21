questions = [
    {
        "prompt": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "prompt": "What is the first name of Iron Man?",
        "options": ["A. John", "B. Tony", "C. Bruce", "D. Clark"],
        "answer": "B"
    },
    {
        "prompt": "In Smallville, what is Clark Kent's father's name?",
        "options": ["A. John", "B. Tony", "C. Bruce", "D. Jonathan"],
        "answer": "D"
    },
    {
        "prompt": "From Mighty Morphin Power Rangers, what is the name of the Red Ranger?",
        "options": ["A. Jason", "B. Tommy", "C. Billy", "D. Zack"], 
        "answer": "A"
    },
    {
        "prompt": "What is HULK's weakness?",
        "options": ["A. Water", "B. Air", "C. Fire", "D. Thunder"],
        "answer": "D"
    },
    {
        "prompt": "In the process of building a computer, what are the first components to be installed?",
        "options": ["A. RAM", "B. CPU", "C. GPU", "D. Motherboard"],
        "answer": "D"
    },
    {
        "prompt": "Who is the founder of Microsoft?",
        "options": ["A. Bill Gates", "B. Steve Jobs", "C. Mark Zuckerberg", "D. Elon Musk"],
        "answer": "A"
    },
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer: (A, B, C, or D):  ")
        if answer == question["answer"]:
            print("Correct!, You got a point\n")
            score += 1
        else:
            print("Whats wrong with you!, The correct answer is: ", question["answer"], "\n")

    print(f"You got {score} out of {len(questions)} questions right. Thank you for playing!")



run_quiz(questions)