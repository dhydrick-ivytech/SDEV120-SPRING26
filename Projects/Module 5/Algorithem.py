def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"

def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    pass_count= 0

    #priming Input
    mark=int(input("Enter a number (-1 to quit): "))
        

    #loop until the user enters -1
    while (mark >= 0):
        grade = get_grade(mark)
        print(f"Grade: {grade}")

        if (mark >= 70):
            pass_count += 1

        #get the next mark
        mark=int(input("Enter a number (-1 to quit): "))
    print(f"Total number of passing grades: {pass_count}")

 
main()

