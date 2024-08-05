def process_evaluation():
    """
    A method to process evaluations and comments.
    """
    while True:
        print("Please select the process you want to perform")
        print("1: Enter evaluation points and comments")
        print("2: Check previous results")
        print("3: Exit")
        choice = input("Enter your choice (1-3): ")

        if choice.isdigit():
            choice = int(choice)

            if choice == 1:
                input_evaluation()
            elif choice == 2:
                display_results()
            elif choice == 3:
                print("Exiting the process.")
                break
            else:
                print("Please enter a value between 1 and 3")
        else:
            print("Invalid input. Please enter a number.")


def input_evaluation():
    """
    Handles input of evaluation points and comments.
    """
    while True:
        point = input("Please enter a rating from 1 to 5: ")
        if point.isdigit():
            point = int(point)
            if 1 <= point <= 5:
                comment = input("Please enter your comment: ")
                save_evaluation(point, comment)
                break
            else:
                print("Please enter a valid rating between 1 and 5.")
        else:
            print("The evaluation point must be a number.")


def display_results():
    """
    Displays the previous results from the data file.
    """
    try:
        with open("data.txt", "r") as file:
            print("Previous results:")
            print(file.read())
    except FileNotFoundError:
        print("No results found.")


def save_evaluation(point, comment):
    """
    Saves the evaluation and comment to a data file.
    """
    with open("data.txt", "a") as file:
        file.write(f"Points: {point}, Comment: {comment}\n")
        print("Evaluation saved successfully.")


if __name__ == "__main__":
    process_evaluation()
