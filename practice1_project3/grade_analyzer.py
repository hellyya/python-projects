#step1
while True:
    try:
        num_students = int(input("enter number of students: "))
        if num_students > 0:
            break
        print("must be greater than zero.")
    except ValueError:
        print("invalid input. please enter a number.")
#step2
students = []
for i in range(num_students):
    print(f"studnets {i+1}:")
    name = input("enter name: ").strip()

    while True:
        try:
            grade = float(input(f"enter grade for {name}: "))
            if 0 <= grade <= 100:
                break
            print(" grade must be between 0 and 100.")
        except ValueError:
            print(" invalid. please enter a number for the grade.")

#store in dictionary and add to list
    students.append({"name": name, "grade": grade})
#step3
print("\n")
print(f"{'student name':<20}  {'grade'}")
print("-" * 30)
for s in students:
    print(f"{s['name']:<20}  {s['grade']:>5.2f}")
    
#step4
if students:
    all_grades = [s['grade'] for s in students]
    avg_grade = sum(all_grades) / len(all_grades)
    max_grade = max(all_grades)
    min_grade = min(all_grades)

    print("\n")
    print(f"class average: {avg_grade:.2f}")
    print(f"highest grade: {max_grade:.2f}")
    print(f"lowest grade: {min_grade:.2f}")

#step5
search_name = input("\nenter name to search for a students grade: ").strip().lower()
found = False
for s in students:
    if s['name'].lower() == search_name:
        print (f"result: {s['name']} has a grade of {s['grade']}")
        found = True
        break

if not found:
    print(f"sorry name '{search_name}' was not found.")


