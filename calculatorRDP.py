import math


def function_p():
    question = input("  Incoherent input, try again?.\n"
                     "  [yes] or any key to exit:\n"
                     "    ->").lower()
    return question


def function_v(v_1, v_2):
    n_v = input("  Type any variable of the two that you have:\n"
                f'* "{v_1}".\n'
                f'* "{v_2}".\n'
                "    ->").lower()
    return n_v


def function_input(v):
    while True:
        output = input(f"  Type the digit of the {v}, no units:\n"
                       "    ->")
        try:
            float(output)
        except ValueError:
            output = function_p()
            if output == "yes":
                continue
            break
        if output == "yes":
            continue
        output = float(output)
        return output
    exit()


def function_arg(t, r_f):
    print(f"  The {t} is:\n"
          f"    ->{r_f:.4f}")


list_v = ["radio", "diameter", "perimeter"]
pi = math.pi
while True:
    input_1 = input('  Digit what you want to find:\n'
                    '* "radio".\n'
                    '* "diameter".\n'
                    '* "perimeter"\n.'
                    '    ->').lower()
    if input_1 == list_v[0]:
        t = list_v[0]
        while True:
            n_v = function_v("diameter", "perimeter")
            if n_v == "diameter":
                v = "diameter"
                n_d = function_input(v)
                r = (n_d / 2)
                function_arg(t, r)
                break
            elif n_v == "perimeter":
                v = "perimeter"
                n_p = function_input(v)
                r = (n_p / (2 * pi))
                function_arg(t, r)
                break
            else:
                question = function_p()
                if question != "si":
                    break
    elif input_1 == list_v[1]:
        n_v = function_v("radio", "perimeter")
        t = list_v[1]
        while True:
            if n_v == "radio":
                v = "radio"
                n_r = function_input(v)
                d = (n_r * 2)
                function_arg(t, d)
                break
            elif n_v == "perimeter":
                v = "perimeter"
                n_p = function_input(v)
                d = (n_p / pi)
                function_arg(t, d)
                break
            else:
                question = function_p()
                if question != "yes":
                    break
    elif input_1 == list_v[2]:
        n_v = function_v("radio", "diameter")
        t = list_v[2]
        while True:
            if n_v == "radio":
                v = "radio"
                n_r = function_input(v)
                p = ((n_r * 2) * pi)
                function_arg(t, p)
                break
            elif n_v == "diameter":
                v = "diameter"
                n_d = function_input(v)
                p = (n_d * pi)
                function_arg(t, p)
                break
            else:
                question = function_p()
                if question != "yes":
                    break
    elif (input_1 != list_v[0] and input_1 != list_v[1]) and input_1 != list_v[2]:
        question = function_p()
        if question != "yes":
            break
    else:
        re_run = input("  re_run? [yes] o any key to exit:\n"
                       "    ->").lower()
        if re_run != "yes":
            break
    break
