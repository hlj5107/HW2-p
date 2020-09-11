# Author: Hannah Johnston hlj5107@psu.edu

def getGradePoint(grade):
  if grade == "A":
    return 4.0
  elif grade == "A-":
    return 3.67
  elif grade == "B+":
    return 3.33
  elif grade == "B":
    return 3.0
  elif grade == "B-":
    return 2.67
  elif grade == "C+":
    return 2.33  
  elif grade == "C":
    return 2.0
  elif grade == "D":
    return 1.0
  else:
    return 0.0

def run():
  gradepoint1 = (input("Enter your course 1 letter grade: "))
  credit1 = float(input("Enter your course 1 credit: "))
  print(f"Grade point for course 1 is: {getGradePoint(gradepoint1)}")
  newgradepoint1 = float(getGradePoint(gradepoint1))
  gradepoint2 = (input("Enter your course 2 letter grade: "))
  credit2 = float(input("Enter your course 2 credit: "))
  print(f"Gradepoint for course 2 is: {getGradePoint(gradepoint2)}")
  newgradepoint2 = float(getGradePoint(gradepoint2))
  gradepoint3 = (input("Enter your course 3 letter grade: "))
  credit3 = float(input("Enter your course 3 credit: "))
  print(f"Gradepoint for course 3 is: {getGradePoint(gradepoint3)}")
  newgradepoint3 = float(getGradePoint(gradepoint3))
  GPA = (newgradepoint1 * credit1 + newgradepoint2 * credit2 + newgradepoint3 * credit3)/(credit1 + credit2 + credit3)
  print(f"Your GPA is: {GPA}")

if __name__ == "__main__":
    run()