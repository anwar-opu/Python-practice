questions = [["Which language used to first create facebook", "python", "C", "C++", "Php", 4],
             ["Which language used to first create facebook", "python", "C", "C++", "Php", 4],
             ["Which language used to first create facebook", "python", "C", "C++", "Php", 4],
             ["Which language used to first create facebook", "python", "C", "C++", "Php", 4],
             ["Which language used to first create facebook", "python", "C", "C++", "Php", 4],
             ]
Levels = [1000, 2000, 3000, 4000, 5000, 6000]

money = 0
for i in range(0, len(questions)):
    question = questions[i]

    print(f"\nQuestion for tk. {Levels[i]}")

    print(f"a. {question[1]}     b.{question[2]}\n"
          f"c. {question[3]}        d.{question[4]} ")
    reply = int(input("enter your answer : "))

    if reply == question[-1]:
        print(f"correct answer, you have won{Levels[i]}")
        if i == 2:
            money = 10000
        elif i == 3:
            money = 320000

    else:
        print("wrong answer !")
        break

print(f"Your take home money is {money}")
