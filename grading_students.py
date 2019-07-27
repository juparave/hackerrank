# Grading Students

def gradingStudents(grades):
    rgrades = []
    for i in grades:
        if i < 38:
            rgrades.append(i)
        elif (((int(i / 5)) + 1) * 5 - i) < 3:
            rgrades.append(((int(i / 5)) + 1) * 5)
        else:
            rgrades.append(i)

    return rgrades

if __name__ == "__main__":
    grades = [73, 67, 38, 33]

    result = gradingStudents(grades)

    print('\n'.join(map(str,result)))