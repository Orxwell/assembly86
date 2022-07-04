import math


def funcion_p():
    pregunta = input(
        '  No has digitado algo coherente.\n'
        '  ¿Deseas re-preguntar? [si] o cualquier tecla para salirse:\n'
        '    ->'
    ).lower()
    return pregunta


def funcion_v(v_1, v_2):
    n_v = input(
        '  Digíte alguna variable que posea:\n'
        f'* "{v_1}".\n'
        f'* "{v_2}".\n'
        '    ->'
    ).lower()
    return n_v


def funcion_input(v):
    while True:
        output = input(
            f'  Digíte el dato de la variable {v}, sin unidades:\n'
            '    ->'
        )
        try:
            float(output)
        except ValueError:
            output = funcion_p()
            if output == "si":
                continue
            break
        if output == "si":
            continue
        output = float(output)
        return output
    exit()


def funcion_arg(t, r_f):
    print(
        f'  El {t} es de:\n'
        f'    ->{r_f:.4f}'
    )


lista_v = ["radio", "diametro", "perimetro"]
pi = math.pi
while True:
    input_1 = input(
        '  Digíte lo que desee hayar:\n'
        '* "radio".\n'
        '* "diametro".\n'
        '* "perimetro"\n.'
        '    ->'
    ).lower()
    if input_1 == lista_v[0]:
        t = lista_v[0]
        while True:
            n_v = funcion_v("diametro", "perimetro")
            if n_v == "diametro":
                v = "diámetro"
                n_d = funcion_input(v)
                r = (n_d / 2)
                funcion_arg(t, r)
                break
            elif n_v == "perimetro":
                v = "perímetro"
                n_p = funcion_input(v)
                r = (n_p / (2 * pi))
                funcion_arg(t, r)
                break
            else:
                pregunta = funcion_p()
                if pregunta != "si":
                    break
    elif input_1 == lista_v[1]:
        n_v = funcion_v("radio", "perimetro")
        t = lista_v[1]
        while True:
            if n_v == "radio":
                v = "radio"
                n_r = funcion_input(v)
                d = (n_r * 2)
                funcion_arg(t, d)
                break
            elif n_v == "perimetro":
                v = "perímetro"
                n_p = funcion_input(v)
                d = (n_p / pi)
                funcion_arg(t, d)
                break
            else:
                pregunta = funcion_p()
                if pregunta != "si":
                    break
    elif input_1 == lista_v[2]:
        n_v = funcion_v("radio", "diametro")
        t = lista_v[2]
        while True:
            if n_v == "radio":
                v = "radio"
                n_r = funcion_input(v)
                p = ((n_r * 2) * pi)
                funcion_arg(t, p)
                break
            elif n_v == "diametro":
                v = "diámetro"
                n_d = funcion_input(v)
                p = (n_d * pi)
                funcion_arg(t, p)
                break
            else:
                pregunta = funcion_p()
                if pregunta != "si":
                    break
    elif (input_1 != lista_v[0] and input_1 != lista_v[1]) and input_1 != lista_v[2]:
        pregunta = funcion_p()
        if pregunta != "si":
            break
    else:
        ejecutar = input(
            '  Ya has terminado el script.\n'
            '  ¿Deseas re-ejecutar? [si] o cualquier tecla para salirse:\n'
            '    ->'
        ).lower()
        if ejecutar != "si":
            break
    break
