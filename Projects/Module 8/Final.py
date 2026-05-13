def fillArray(SIZE):
    """Prompts the user for a name and 10 quiz scores."""
    name = input("Enter the student's name: ")
    scores = []
    
    print(f"Enter {SIZE} quiz scores:")
    for i in range(SIZE):
        while True:
            try:
                score = float(input(f"  Quiz {i + 1}: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("  Please enter a score between 0 and 100.")
            except ValueError:
                print("  Invalid input. Please enter a numeric value.")
                
    return name, scores

def swap(scores, y):
    """Swaps two elements in the list."""
    temp = scores[y]
    scores[y] = scores[y + 1]
    scores[y + 1] = temp

def sortArray(scores, SIZE):
    """Sorts the array in descending order (highest to lowest)."""
    comps = SIZE - 1
    for x in range(comps):
        for y in range(comps - x):
            # Sort descending: if the current score is less than the next, swap
            if scores[y] < scores[y + 1]:
                swap(scores, y)

def displayTotal(name, scores, MAX):
    """Calculates and displays the sum of the top MAX scores."""
    total = sum(scores[:MAX])
    print("\n" + "="*30)
    print(f"Results for: {name}")
    print(f"Top {MAX} Scores: {scores[:MAX]}")
    print(f"Total Points: {total}")
    print("="*30)

def main():
    # Declarations
    SIZE = 10
    MAX = 6
    
    # 1. Fill the array
    name, scores = fillArray(SIZE)
    
    # 2. Sort the array (Descending)
    sortArray(scores, SIZE)
    
    # 3. Display the top 6 scores
    displayTotal(name, scores, MAX)

if __name__ == "__main__":
    main()