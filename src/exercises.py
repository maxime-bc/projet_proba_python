from math import isnan
from typing import Tuple

from src.format import format_quadratic_equation, format_pow1, format_pow2, format_trigo1, format_trigo2, format_trigo3, \
    format_log
from src.generate import generate_pow1, generate_pow2, generate_trigo, generate_log
from src.integrals import integral_pow1, integral_pow2, integral_trigo1, integral_trigo2, integral_trigo3, integral_log
from src.quadratic_equations import solve_quadratic_equation
from src.rand import randrange_exclude, randrange_step, START_VALUE, STOP_VALUE, STEP_VALUE

HARD_EXERCISE = 2
NORMAL_EXERCISE = 1


def exercise_1(score: float) -> float:

    res1: float
    res2: float
    solutions_num: int
    a: float = randrange_exclude(0.0, START_VALUE, STOP_VALUE, STEP_VALUE)
    b: float = randrange_step(START_VALUE, START_VALUE, STEP_VALUE)
    c: float = randrange_step(START_VALUE, START_VALUE, STEP_VALUE)

    res1, res2, solutions_num = solve_quadratic_equation(a, b, c)

    print("Equation du 2nd dégré générée : \n")
    format_quadratic_equation(a, b, c)

    print("Equation du second degré\n")
    print("Entrez le(s) solution(s) ou n si il n'y en a pas (arrondir au centième).\n")

    if solutions_num == 0:

        answer = input()

        if answer == 'n':
            print("Bravo ! \n En effet, cette équation n'a pas de solutions.\n")
            score = score + 1.0

        else:
            print("Faux ! \n Cette équation ne possède pas de solutions.\n")

    elif solutions_num == 1:

        answer = input()

        if answer == res1:
            print("Bravo ! \n En effet, cette équation possède une solution : {:0.2f}\n".format(res1))
            score = score + 1.0

        else:
            print("Faux ! \n Cette équation possède une solution : {:0.2f}\n".format(res1))

    else:

        answer1, answer2 = input().split()

        if answer1 == res1 and answer2 == res2:
            print("Bravo ! \n En effet, cette équation possède deux solutions : {:0.2f} et {:0.2f}\n".format(res1, res2))
            score = score + 1.0

        else:

            if answer1 == res2 and answer2 == res1:
                print("Bravo ! \n En effet, cette équation possède deux solutions : {:0.2f} et {:0.2f}\n".format(res1, res2))
                score = score + 1.0

            else:
                print("Faux ! \n Cette équation possède deux solutions : {:0.2f} et {:0.2f}\n".format(res1, res2))

    return score


def exercise_2(score: float) -> float:

    choice: str = ''
    weight_1: int = 5
    weight_2: int = 5
    weight_3: int = 5

    while choice != 'q':

        print("\nIntégration sur R\n");
        print("Poids actuels : "
              "Fonctions puissance : {}\n"
              "Fonctions trigonométriques : {}\n"
              "Fonctions logarithmiques : {}\n".format(weight_1, weight_2, weight_3))

        print("p = Changer les poids des exercices\n"
              "c = Commencer un exercice\n"
              "q = Revenir au menu\n")

        choice = input()

        if choice == 'c':

            random: float = randrange_step(1.0, 15.0, 1.0)
            res: float

            if random < weight_1:

                print("Fonction puissance\n")
                random: float = randrange_step(1.0, 2.0, 1.0)

                if random == 1:
                    res = pow1()

                else:
                    res = pow2()

                print("{:0.2f}\n".format(round(res)))
                check_exercise2_answers(round(res), score, HARD_EXERCISE)

            elif weight_1 < random <= (weight_1 + weight_2):

                print("Fonction trigonométrique\n")

                random: int = randrange_step(1.0, 3.0, 1.0)

                if random == 1:
                    res = trigo1()

                elif random == 2:
                    res = trigo2()

                else:
                    res = trigo3()

                print("{:0.2f}\n".format(round(res)))
                check_exercise2_answers(round(res), score, NORMAL_EXERCISE)

            else:
                print("Fonction logarithmique\n")
                res = log1()

                print("{:0.2f}\n", round(res))
                check_exercise2_answers(round(res), score, NORMAL_EXERCISE)

        elif choice == 'p':
            pass
            # edit_ex2_weights(p_weight_1, p_weight_2, p_weight_3);

        elif choice != 'q':
            print("{} n'est pas un choix reconnu\n".format(choice))

    return score


def check_exercise2_answers(res: float, score: float, difficulty: int) -> None:

    answer: str = input()

    if res == answer:
        print("Bravo ! \n En effet, cette intégrale vaut {:0.2f}\n".format(res))

        if difficulty == NORMAL_EXERCISE:
            score = score + 1.0

        elif difficulty == HARD_EXERCISE:
            score = score + 1.5

    else:
        print("Faux ! \n Cette intégrale vaut {:0.2f}\n".format(res))


def pow1() -> float:
    a, b, c, d, alpha = generate_pow1()
    res = integral_pow1(a, b, c, d, alpha)
    while isnan(res):
        res = integral_pow1(a, b, c, d, alpha)

    format_pow1(c, d, alpha)
    return res


def pow2() -> float:
    a, b, c = generate_pow2()
    res = integral_pow2(a, b, c)
    while isnan(res):
        res = integral_pow2(a, b, c)

    format_pow2(c)
    return res


def trigo1() -> float:
    a, b, c = generate_trigo()
    res = integral_trigo1(a, b, c)
    while isnan(res):
        res = integral_trigo1(a, b, c)

    format_trigo1(c)
    return res


def trigo2() -> float:
    a, b, c = generate_trigo()
    res = integral_trigo2(a, b, c)
    while isnan(res):
        res = integral_trigo2(a, b, c)

    format_trigo2(c)
    return res


def trigo3() -> float:
    a, b, c = generate_trigo()
    res = integral_trigo3(a, b, c)
    while isnan(res):
        res = integral_trigo3(a, b, c)

    format_trigo3(c)
    return res


def log1() -> float:
    a, b, c = generate_log()
    res = integral_log(a, b, c)
    while isnan(res):
        res = integral_log(a, b, c)

    format_log(c)
    return res


def edit_exercises_weights(weight_ex1: int, weight_ex2: int) -> Tuple[int, int]:

    weight: int
    print("--- Poids actuels --- \n "
          "ex1 = {}\n "
          "ex2 = {}\n".format(weight_ex1, weight_ex2))
    print("Choisissez le poids de l'ex 1, celui de l'ex 2 sera ajusté automatiquement (q pour quitter):\n")
    print("Le poids doit être compris entre 1 et 10 : \n")
    weight = input()

    while weight < 0or weight > 10:
        print("Le poids doit être compris entre 1 et 10 : \n")
        weight = input()

    weight_ex1 = weight
    weight_ex2 = 10-weight
    print("Nouveaux poids : \n "
          "ex1 = {}\n "
          "ex2 = {}\n".format(weight_ex1, weight_ex2))

    return weight_ex1, weight_ex2


def edit_ex2_weights(weight_1: int, weight_2: float, weight_3: float) -> Tuple[float, float, float]:

    print("--- Poids actuels --- \n"
          "Fonctions puissance = {}\n"
          "Fonctions trigonométriques = {}\n"
          "Fonctions logarithmiques : {}\n".format(weight_1, weight_2, weight_3))

    print("Choisissez les poids pour les exercices sur les fonctions puissances et trigonométriques, "
          "celui des fonctions logarithmiques sera ajusté automatiquement (q pour quitter):\n")

    weight_1_choice: int = input('1 - Entrez le poids des fonctions puissance (compris entre 1 et 15) : \n')
    while weight_1_choice < 0 or weight_1_choice > 15:
        weight_1_choice = input('1 - Entrez le poids des fonctions puissance (compris entre 1 et 15) : \n')

    if weight_1_choice != 15:
        weight_2_choice: int = input("2 - Entrez les 2 poids (ils doivent être compris entre 1 et 15) : \n")
        while weight_2_choice < 1 or weight_2_choice > (15 - weight_1):
            weight_2_choice: int = input("2 - Entrez les 2 poids (ils doivent être compris entre 1 et 15) : \n")

    else:
        weight_2_choice = 0
        print("2 - Poids des fonctions logarithmiques automatiquement passé à {}\n".format(weight_2_choice))

    weight_3_choice: int = 15 - (weight_1_choice + weight_2_choice)
    print("3 - Poids des fonctions logarithmiques automatiquement passé à {}\n".format(weight_3_choice))

    return weight_1_choice, weight_2_choice, weight_3_choice


# WIP
def integer_input(message: str) -> int:

    user_input = input(message)

    while not user_input.isdigit():
        user_input = input(message)

    return user_input