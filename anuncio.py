while True:
    print("Please select the action you want to perform")
    print("1: Enter evaluation points and comments")
    print("2: Check previous results")
    print("3: Exit")
    num = input()

    if num.isdecimal():
        num = int(num)

        if num == 1:
            while True:
                print("Please enter a rating from 1 to 5")
                point = input()
                if point.isdecimal():
                    point = int(point)
                    if (
                        point <= 0 or point > 5
                    ):  # Condition for less than or equal to 0 or greater than 5
                        print("Please enter between 1 and 5")
                    else:
                        print("Please enter your comment")
                        comment = input()
                        post = f"Points: {point} Comment: {comment}"
                        file_pc = open("data.txt", "a")
                        file_pc.write(f"{ post } \n")
                        file_pc.close()
                        break
                else:
                    print("Please enter the rating points as numbers")
        elif num == 2:
            print("Previous results")
            read_file = open("data.txt", "r")
            print(read_file.read())
            read_file.close()
        elif num == 3:
            print("Exiting")
            break  # Syntax to end the loop
        else:
            print("Please enter between 1 and 3")
    else:
        print("Please enter between 1 and 3")
