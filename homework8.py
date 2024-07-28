grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_students=(sorted(students))
gpa_aaron=(sum(grades[0]))/(len(grades[0]))
gpa_bilbo=(sum(grades[1]))/(len(grades[1]))
gpa_johnny=(sum(grades[2]))/(len(grades[2]))
gpa_khendrik=(sum(grades[3]))/(len(grades[3]))
gpa_steve=(sum(grades[4]))/(len(grades[4]))
dict={'Aaron':gpa_aaron,'Bilbo':gpa_bilbo,'Johnny':gpa_johnny,'Khendrik':gpa_khendrik,'Steve':gpa_steve}
print(dict)




