# Даны три списка students_ids, students_names, students_grades, содержащие информацию о студентах.

# Дополните приведенный код, используя генератор, так, чтобы получить result,
# содержащий вложенные словари в соответствии с образцом:
# [{'S001': {'Camila Rodriguez': 86}}, {'S002': {'Juan Cruz: 98'}},...]

# Примечание 1. Для параллельной итерации по всем трем спискам одновременно можно использовать
# встроенную функцию zip().

student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti',
                 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman',
                 'Tom Hardy']
student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]

result = [{k: dict(v)} for k, v in zip(student_ids, zip(student_names, student_grades))]
print(result)
