def class_photos(red_students, blue_students):
    red_students.sort(reverse=True)
    blue_students.sort(reverse=True)

    if red_students[0] > blue_students[0]:
        back_row = red_students
        front_row = blue_students
    elif blue_students[0] > red_students[0]:
        back_row = blue_students
        front_row = red_students
    else:
        return "Failed"

    for r, f in zip(back_row, front_row):
        if r <f: 
            return "Failed"
            
    
    return "Passed"

red = [5, 8, 1, 3, 4]
blue = [6, 9, 2, 4, 5]

answer = class_photos(red, blue)
print(answer)


#Time Complexity=O(n log n)
#Space Complexity = O(1)