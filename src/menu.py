from src.exercises import exercise_1, exercise_2, edit_exercises_weights
from src.rand import randrange_step, START_VALUE, STOP_VALUE, STEP_VALUE


def menu() -> None:

    choice: str = ''
    score: float = 0.0
    max_score: float = 0.0

    weight_1: int = 10
    weight_2: int = 0

    while choice != 'q':

        print("\n Menu --- "
              "Score : {}/{} ---\n "
              "c = Commencer \n "
              "p = Changer les poids des exercices\n "
              "q = Quitter\n\n".format(score, max_score))

        choice = input()
        random: int = randrange_step(0, 10, 1)
        # TODO: if weight for ex1 is fixed at 10, it can sometimes launch ex 2

        if choice == 'c':

            if random < weight_1:
                score, max_score = exercise_1(score, max_score)

            else:
                score, max_score = exercise_2(score, max_score)

        elif choice == 'p':
            weight_1, weight_2 = edit_exercises_weights(weight_1,  weight_2)

        elif choice != 'q':
            print('{} is not recognized as a format.'.format(choice))

    print('Bye !')
