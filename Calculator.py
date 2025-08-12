# calculator.py - simple CLI calculator
def calculator():
    try:
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
    except ValueError:
        print("Please enter valid integers.")
        return

    c = input("Press (a) add, (s) subtract, (d) divide, (m) multiply: ").lower()

    if c == "a":
        print("Sum:", num1 + num2)
    elif c == "s":
        print("Difference:", abs(num1 - num2))
    elif c == "d":
        if num2 == 0:
            print("❌ Cannot divide by zero!")
        else:
            print("Division:", num1 / num2)
    elif c == "m":
        print("Multiply:", num1 * num2)
    else:
        print("Invalid operation.")
        
if __name__ == "__main__":
    while True:
        cmd = input("Type 'run' to open calculator or 'exit' to quit: ").lower()
        if cmd == "run":
            calculator()
        elif cmd == "exit":
            print("Goodbye!")
            break
        else:
            print("Type 'run' or 'exit'.")
