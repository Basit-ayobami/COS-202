def ppc_calculator():
    print("="*40)
    print(" PERSONAL POCKET CGPA CALCULATOR - COS202")
    print("="*40)
    print("Grading System: A=5, B=4, C=3, D=2, E=1, F=0")
    print("="*40)
    
    try:
        num_courses = int(input("Enter number of courses: "))
        
        if num_courses <= 0:
            print("Number of courses must be greater than 0")
            return
            
        total_units = 0
        total_points = 0
        
        for i in range(1, num_courses + 1):
            print(f"\n--- Course {i} ---")
            course_code = input("Course code: ")
            unit = int(input("Course unit: "))
            
            score = float(input("Enter score (0-100): "))
            
            # Selection control statements for grading
            if score >= 70 and score <= 100:
                grade = 'A'
                point = 5
            elif score >= 60 and score <= 69:
                grade = 'B'
                point = 4
            elif score >= 50 and score <= 59:
                grade = 'C'
                point = 3
            elif score >= 45 and score <= 49:
                grade = 'D'
                point = 2
            elif score >= 40 and score <= 44:
                grade = 'E'
                point = 1
            elif score >= 0 and score < 40:
                grade = 'F'
                point = 0
            else:
                print("Invalid score. Must be 0-100")
                return
            
            course_points = unit * point
            total_units += unit
            total_points += course_points
            
            print(f"Result: {course_code} | Score: {score} | Grade: {grade} | Points: {course_points}")
        
        if total_units > 0:
            cgpa = total_points / total_units
            print("\n" + "="*40)
            print(f"Total Units: {total_units}")
            print(f"Total Grade Points: {total_points}")
            print(f"Your CGPA: {cgpa:.2f}")
            
            # CGPA classification
            if cgpa >= 4.50:
                print("Class: First Class")
            elif cgpa >= 3.50:
                print("Class: Second Class Upper")
            elif cgpa >= 2.40:
                print("Class: Second Class Lower")
            elif cgpa >= 1.50:
                print("Class: Third Class")
            else:
                print("Class: Pass")
            print("="*40)
        else:
            print("Total units cannot be 0")
            
    except ValueError:
        print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    ppc_calculator()