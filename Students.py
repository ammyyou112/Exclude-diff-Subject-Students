#function for getting student info from user
def students():

    #get total number of students
    total_students = int(input('Enter total number of students in the class: '))

    #get mathemathic and biology students
    maths_students = int(input('Enter Number of Maths Student: '))
    bio_students = int(input('Enter num of Bio Students: '))

    #Exclude the maths and bio studetns from total students
    maths_bio_students = maths_students + bio_students
    exclude_maths_bio = total_students - maths_bio_students

    #print the result
    print('Total Students: ', total_students)
    print('Maths & Bio Students: ', maths_bio_students)
    print('Remaining Students: ',exclude_maths_bio)

students()
