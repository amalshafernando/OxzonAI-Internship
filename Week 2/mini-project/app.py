def input_student_data():
    students = []
    while True:
        try:
            name = input("Enter student name (or type 'done' to finish): ")
            if name.lower() == 'done':
                break
            score = float(input(f"Enter score for {name}: "))
            students.append((name, score))
        except ValueError:
            print("Invalid input. Please enter a valid score.")
    return students


def calculate_statistics(students):
    if not students:
        print("No student data available.")
        return None
    
    scores = [score for _, score in students]
    average_score = sum(scores) / len(scores)
    highest_score = max(scores)
    lowest_score = min(scores)

    print(f"\nAverage Score: {average_score:.2f}")
    print(f"Highest Score: {highest_score}")
    print(f"Lowest Score: {lowest_score}")

    return average_score, highest_score, lowest_score


def save_to_file(students):
    with open("student_scores.txt", "w") as file:
        for name, score in students:
            file.write(f"{name}: {score}\n")
    print("\nStudent data saved to 'student_scores.txt'.")


def main():
    students = input_student_data()
    if students:
        calculate_statistics(students)
        save_to_file(students)


if __name__ == "__main__":
    main()
