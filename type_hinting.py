'''
Type hinting: is a feature to indicate the expected data types of variables, function parameters and return values.
'''

def student(name: str, grade: int, marks: list[int] = [0,0,0,0,0]) -> str:
    school: str = 'Jawahar Navodaya Vidyalaya'
    avg_marks: float = sum(marks)/len(marks)
    return f'{name}, studied in grade {grade} at {school}, has scored an average of {avg_marks}'

print(student('Shivu', 12, [89, 67, 84, 95, 85])) # Output: Success: no issues found in 1 source file
print(student('Kavya', 12, [85, 64, 78, 77, 70.0])) # Output: error: List item 4 has incompatible type "float"; expected "int"  [list-item]

# Pre-requisite to run this script: mypy module should be installed
# Run command to check type hinting by the aid of mypy: 
# mypy .\type_hinting.py