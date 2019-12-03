from src.rand import randrange_step


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
        print(choice)

        # random: int = random_with_step(1.0, 10.0, 1.0)

        if choice == 'c':
            print('You choose c')

            # if random < weight_1:
            # pass
            # exercise_1(score)
            # else:
            # pass
            # exercise_2(score)

        elif choice == 'p':
            print('You choose p')
            # edit_exercises_weights(p_weight_ex1, p_weight_ex2)

        elif choice != 'q':
            print('{} is not recognized as a format.'.format(choice))
            pass
            # printf("%c n'est pas un choix reconnu\n", choice)

    print('Bye !')
