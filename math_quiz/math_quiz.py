import random
def rand_int(min, max):
    """
    Return Random integer within min and max.
    """
    return random.randint(min, max)
def rand_optr():
    """
    Return random operator
    """
    return random.choice(['+', '-', '*'])
def do_operation(num1, num2, optr):
    """
    perform operation on num1,num2 using operator
    """
    problem = f"{num1} {optr} {num2}"
    if optr == '+': ans = num1 + num2
    elif optr == '-': ans = num1 - num2
    else: ans = num1 * num2
    return problem, ans

def math_quiz():
    sum = 0
    total_qstns = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need      to provide the correct answers.")

    for _ in range(total_qstns):
        #Generate random numbers
        num1 = rand_int(1, 10);
        num2 = rand_int(1, 5);
        #Generate random operator 
        optr = rand_optr()
        #Generate problem,answer

        PROBLEM, ANSWER = do_operation(num1, num2, optr)
        print(f"\nQuestion: {PROBLEM}")
        #try-except for handling non-integer input from user
        try:
            useranswer = input("Your answer: ")
            useranswer = int(useranswer)
        #check if answer is correct
            if useranswer == ANSWER:
                print("Correct! You earned a point.")
                sum += 1
            else:
                print(f"Wrong answer. The correct answer is{ANSWER}.")
        except ValueError:print("Invalid input. Please enter a valid integer.")
    print(f"\nGame over! Your score is: {sum}/{total_qstns}")

if __name__ == "__main__":
    math_quiz()
