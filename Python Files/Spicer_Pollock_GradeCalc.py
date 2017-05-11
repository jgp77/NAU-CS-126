__author__='Jack Spicer and Joshua Pollock'


def percentage_per_category(score_list, max_list):
    '''Calculate the percentage of possible points earned in a category'''
    score_total=float(sum(score_list))
    score_max_total=float(sum(max_list))
    percentage=score_total / score_max_total
    return percentage


def letter_grade(percent):
    '''Return the letter grade equivalent of the given percentage.'''
    if percent >= .90:
        return "A"
    elif percent >= .80 and percent <= .89:
        return "B"
    elif percent >= .70 and percent <= .79:
        return "C"
    elif percent >= .60 and percent <= .69:
        return "D"
    elif percent <= .59:
        return "F"


def weighted_score(percentage, weight):
    '''Calculates the weighted contribution of a
    category to the overall course grade'''
    weight_percent=percentage * weight
    return weight_percent


def main():
    homework=[39, 40, 29, 40, 0, 5]
    # Given list of recieved homework grades
    homework_max=[40, 40, 40, 40, 40, 5]
    # Given list of points possible
    quizzes=[10, 10, 9, 2, 10, 10, 10]
    # Given list of recieved quiz grades
    quizzes_max=[10, 10, 10, 10, 10, 10, 10]
    # Given list of points possible
    tests=[66, 82, 77,57]
    # Given list of recieved test grades
    tests_max=[100, 100, 100, 100]
    # Given list of points possible
    homework_weight=0.2
    quizzes_weight=0.2
    tests_weight=0.6
    # Given weights of each assignment
    quiz_grade=((percentage_per_category(quizzes, quizzes_max)))
    homework_grade=((percentage_per_category(homework, homework_max)))
    test_grade=((percentage_per_category(tests, tests_max)))
    final_grade=(
        weighted_score(
            quiz_grade,
            quizzes_weight) +
        weighted_score(
            homework_grade,
            homework_weight) +
        weighted_score(
            test_grade,
            tests_weight))
    # Calculations for giving the final grade from the other weighted grades
    print("Homework grade: " + str(
        round((percentage_per_category(
            homework, homework_max) * 100), 0)) + '(' + str(
                letter_grade(percentage_per_category(
                    homework, homework_max))) + ')')
    print("Quiz grade: " + str(
        round((percentage_per_category(
            quizzes, quizzes_max) * 100), 0)) + '(' + str(
                letter_grade(percentage_per_category(
                    quizzes, quizzes_max))) + ')')
    print("Tests grade: " + str(
        round((percentage_per_category(
            tests, tests_max) * 100), 0)) + '(' + str(
                letter_grade(percentage_per_category(
                    tests, tests_max))) + ')')
    # Prints the recieved percentage, unweighted
    print('Final score: ' + str(
        final_grade * 100) + '(' + letter_grade(
            final_grade) + ')')
    # Prints the weighted final grade
