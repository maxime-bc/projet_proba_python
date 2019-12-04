from src.exercises import exercise_1, exercise_2, edit_exercises_weights
from src.rand import randrange_step, START_VALUE, STOP_VALUE, STEP_VALUE


def menu() -> None:

    choice: str = ''
    score: float = 0.0

    weight_1: int = 5
    weight_2: int = 5

    while choice != 'q':

        print("\n Menu --- "
              "Score : {} ---\n "
              "c = Commencer \n "
              "p = Changer les poids des exercices\n "
              "q = Quitter\n\n".format(score))

        choice = input()
        random: int = randrange_step(START_VALUE, STOP_VALUE, STEP_VALUE)

        if choice == 'c':

            if random < weight_1:
                exercise_1(score)

            else:
                exercise_2(score)

        elif choice == 'p':
            weight_1, weight_2 = edit_exercises_weights(weight_1,  weight_2)

        elif choice != 'q':
            print('{} is not recognized as a format.'.format(choice))

    print('Bye !')
