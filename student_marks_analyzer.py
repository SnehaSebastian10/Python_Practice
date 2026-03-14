# Student Marks Analyzer
def calculate_grade(avg):
  if average >= 90:
      return "A"
  elif average >= 75:
      return "B"
  elif average >= 60:
      return "C"  
  else:
      return "D"
name=input("Enter student name: ")
subjects=int(input("enter number of students"))
marks = []
for i in range(subjects):
    mark = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)
total = sum(marks)
average = total / len(marks)
grade= calculate_grade(average)
print("\nStudent:", name)
print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Grade:", grade)
