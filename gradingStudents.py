def gradingStudents(grades):
    result = []
    for i in grades:
        a = 5 - i % 5
        if a < 3 and i >= 38:
            result.append(i+a)
        else: 
            result.append(i)
    return result