import random


def play_number_guessing_game():
    secret_number = random.randint(1, 10)
    print("\nI'm thinking of a number from 1 to 10.")

    while True:
        guess_text = input("Your guess: ").strip()
        if not guess_text.isdigit():
            print("Please enter a whole number.")
            continue

        guess = int(guess_text)
        if guess == secret_number:
            print("That's right! You guessed it.")
            return
        elif guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")


def manage_to_do_list(tasks):
    while True:
        print("\n=== To-Do List ===")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark a task complete")
        print("4. Return to main menu")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            task = input("Enter a task: ").strip()
            if task:
                tasks.append({"name": task, "complete": False})
                print("Task added.")
            else:
                print("A task can't be empty.")
        elif choice == "2":
            if not tasks:
                print("Your to-do list is empty.")
            else:
                for number, task in enumerate(tasks, start=1):
                    status = "done" if task["complete"] else "not done"
                    print(f"{number}. {task['name']} ({status})")
        elif choice == "3":
            if not tasks:
                print("There are no tasks to mark complete.")
                continue
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task['name']}")
            task_text = input("Enter the task number to mark complete: ").strip()
            if task_text.isdigit() and 1 <= int(task_text) <= len(tasks):
                tasks[int(task_text) - 1]["complete"] = True
                print("Task marked complete.")
            else:
                print("That isn't a task number on the list.")
        elif choice == "4":
            return
        else:
            print("Please choose an option from 1 to 4.")


def use_calculator():
    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    print("Choose an operation: +, -, *, /")
    operation = input("Operation: ").strip()

    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        if second_number == 0:
            print("You can't divide by zero.")
            return
        result = first_number / second_number
    else:
        print("Please choose +, -, *, or /.")
        return

    print(f"Result: {result}")


def format_name():
    name = input("Enter a name: ").strip()
    if name:
        print(f"Formatted name: {name.title()}")
    else:
        print("Please enter a name.")


def main():
    tasks = []

    while True:
        print("\n=== Beginner Toolkit ===")
        print("1. Number Guessing Game")
        print("2. To-Do List")
        print("3. Simple Calculator")
        print("4. Name Formatter")
        print("5. Quit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            play_number_guessing_game()
        elif choice == "2":
            manage_to_do_list(tasks)
        elif choice == "3":
            use_calculator()
        elif choice == "4":
            format_name()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Sorry, that's not on the menu. Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()