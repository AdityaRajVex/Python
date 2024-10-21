def calc_avg(grade_list):
    try:
        return sum(grade_list)/len(grade_list)
    except ZeroDivisionError:
        print('Invalid Input')
        return


def converter(avg_grade):
    if 0 <= avg_grade <= 100:
        if avg_grade < 60:
            return 'F'
        if avg_grade < 70:
            return 'D'
        if avg_grade < 80:
            return 'C'
        if avg_grade < 90:
            return 'B'
        else:
            return 'A'

if __name__ == '__main__':
    grades = []
    for i in range(5):
        grade = float(input('Enter a grade (0~100):'))