questions = [
    ["Who is the Prime Minister of India?", "Rahul Gandhi", "Mamta Banarjee", "Narendra Modi", "Amit Shah", 3],
    ["Who gave laws of motion?", "Thomas Edison", "Marie Curie", "Kirchoff", "Isaac Newton", 4],
    ["What is the square root of 49?", "3", "7", "8", "6", 2],
    ["Which state is the heart of India?", "Delhi", "Assam", "Madhya Pradesh", "Bihar", 3],
    ["Which is the smallest country?", "Vatican City", "Monaco", "Nauru", "Tuvalu", 1],
    ["Which is the longest river?", "Amazon", "Nile", "Yangtze", "Mississippi", 2],
    ["Which is the highest mountain?", "Mount Everest", "K2", "Kangchenjunga", "Lhotse", 1]
]

prizes = [10000, 20000, 40000, 60000, 100000, 140000, 180000]

i=0
for question in questions:

    print("\n" + question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    a = int(input("Enter your answer, 1 for a, 2 for b, 3 for c, 4  for d\n "))

    # check answer
    if question[5] == a:
        print("Correct Answer!")

    else:
        print(f"Incorrect! Correct answer was option {question[5]}")
        print("Better luck next time!")
        break
print(f"You won{prizes[i]}")
i+=1