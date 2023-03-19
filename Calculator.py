
def calculator():

        print("\n\nCalculator\n")

        print("Operations: Addition (add), Subtraction (sub), Multiplication (mult), or Division (div).\n")

        while True: 
            try:
                num_1 = float(input("Number 1: "))
                break
            except ValueError:
                print("Please enter a number.")
        while True: 
            try:
                num_2 = float(input("Number 2: "))
                break
            except ValueError:
                print("Please enter a number.")

        def operations():
                operation = input("Choose operation: ")

                global answer

                addition = ['addition', 'add']
                subtraction = ['subtraction', 'sub']
                multiplication = ['multiplication', 'mult']
                division = ['division', 'div']
                    
                if operation.lower() in addition:
                    answer = num_1 + num_2
                elif operation.lower() in subtraction:
                    answer = num_1 - num_2
                elif operation.lower() in multiplication:
                    answer = num_1 * num_2
                elif operation.lower() in division:
                    answer = num_1 / num_2
                else:
                    print("Try again.")
                    operations()
            
        operations()

        print(f"Your answer is {answer}.\n")

        def continues():
                user_continue = input("\nWould you like to continue? Yes (y) or No (n): ")
                if user_continue.lower() == 'yes' or user_continue.lower() == 'y':
                    print("\n\nSounds good!\n")
                    calculator()
                elif user_continue.lower() == 'no' or user_continue.lower() == 'n':
                    print("\n\nThanks for using the calculator!")
                else: 
                    print("\nHmm. Not sure what you mean by that.\nTry again")
                    continues()
        continues()
calculator()