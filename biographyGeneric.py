from datetime import datetime


def generic_text_v1_02(text):
    for i in text:
        if not i == " ":
            bool = i.isalpha()
            if bool:
                list_text.append(i)
            else:
                print("\033[m" + "  | | " +
                      "\033[1;30;43m" + " Incoherent input, try again. " +
                      "\033[m" + "  | |\n  | |                                 | |")
                list_text_f.clear()
                flag = False
                return flag
        else:
            list_text.append(i)
    flag = True
    return flag


def generic_text_v1_01(text):
    for i in text:
        v_bool = i.isalpha()
        if v_bool:
            list_text.append(i)
        else:
            print("\033[m" + "  | | " +
                  "\033[1;30;43m" + " Incoherent input, try again. " +
                  "\033[m" + "   | |\n  | |                                  | |")
            list_text.clear()
            flag = False
            return flag
    flag = True
    return flag


def generic_text_v2(text, v_text, bool_generic):
    if bool_generic:
        flag = generic_text_v1_01(v_text)
    else:
        flag = generic_text_v1_02(v_text)
    g_text = ""
    if flag:
        for i in list_text:
            g_text += i
        list_text_f.append(g_text + text)
        list_text.clear()
    return flag


n = 0
flag = ""
flag_v = ""
text_c1 = ". "
text_c2 = " "
list_text = []
list_text_f = []
list_var_names = ["\033[1;32;40m" + "first name",
                  "\033[1;32;40m" + "second name",
                  "\033[1;32;40m" + "first surname",
                  "\033[1;32;40m" + "second surname"]
list_interface = ["       | |", "      | |", "    | |", "   | |"]
format = "%d/%m/%Y"
bool_date = True
run = True
while run:
    print("\033[m" + "     ____________________________________\n   /______________" +
          "\033[1;30;47m" + " NAME " +
          "\033[m" + "_______________/ |")
    while True:
        name = input(
            "\033[m" + "  | | " +
            "\033[1;37;40m" + f" What is your {list_var_names[n]}" +
            "\033[1;37;40m" + "? " +
            "\033[m" + list_interface[n] + "\033[m" + "\n  | | " +
            "\033[0;31;40m" + " [skip, if you haven't] " + "\033[m" + "         | |\n  | | " +
            "\033[1;37m" + " ->")
        l = len(name)
        bool_generic = True
        if l == 0:
            if n == 3:
                flag_v = False
            else:
                flag_v = True
                n += 1
        elif l == 1:
            flag = generic_text_v2(text_c1, name, bool_generic)
        else:
            flag = generic_text_v2(text_c2, name, bool_generic)
        if l >= 1:
            if not flag:
                continue
            elif n == 3:
                break
            else:
                n += 1
        if not (flag_v or flag_v == ""):
            break
    g_text = ""
    if not list_text_f == []:
        for i in list_text_f:
            g_text += i
        name = g_text
    else:
        name = "\033[0;37m" + "None Provide"
    list_text_f.clear()
    print("\033[m" + "  | |__________________________________|_|\n  |/______________" +
          "\033[1;30;47m" + " NAME " +
          "\033[m" + "_______________|/\n\n     ____________________________________\n   /___________" +
          "\033[1;30;47m" + " BIRTH-DATE " +
          "\033[m" + "____________/ |")
    while True:
        birth_date = input(
            "\033[m" + "  | | " +
            "\033[1;37;40m" + " When were you born?" +
            "\033[m" + "             | |\n  | | " +
            "\033[0;31;40m" + " [dd/mm/aaaa] " +
            "\033[m" + "                   | |\n  | | " +
            "\033[1;37;40m" + " Example:" +
            "\033[0;32;40m" + " ->30/09/2003 " +
            "\033[m" + "          | |\n  | | " +
            "\033[1;37m" + " -> ")
        l = len(birth_date)
        if l > 0:
            try:
                bool_date = datetime.strptime(birth_date, format)
            except ValueError:
                bool_date = False
            if bool_date:
                birth_date += " "
                break
            else:
                print("\033[m" + "  | | " +
                      "\033[1;30;43m" + " Incoherent input, try again. " +
                      "\033[m" + "   | |\n  | |                                  | |")
        else:
            birth_date = "\033[0;37m" + "None Provide"
            break
    print("\033[m" + "  | |__________________________________|_|\n  |/___________" +
          "\033[1;30;47m" + " BIRTH-DATE " +
          "\033[m" + "____________|/\n\n     ____________________________________\n   /___________" +
          "\033[1;30;47m" + " BIRTH-PLACE " +
          "\033[m" + "___________/ |")
    while True:
        birth_place = input(
            "\033[m" + "  | | " +
            "\033[1;37;40m" + " Where were you born? " +
            "\033[m" + "           | |\n  | | " +
            "\033[0;31;40m" + " [country] " +
            "\033[m" + "                      | |\n  | | " +
            "\033[1;37;40m" + " Example:" +
            "\033[0;32;40m" + " ->Venezuela " +
            "\033[m" + "           | |\n  | |" +
            "\033[1;37m" + " -> ")
        l = len(birth_place)
        if l > 0:
            for i in birth_place:
                bool = i.isalpha()
                if not bool:
                    print("\033[m" + "  | | " +
                          "\033[1;30;43m" + " Incoherent input, try again. " +
                          "\033[m" + "   | |\n  | |                                  | |")
                    flag = False
                    break
                else:
                    flag = True
            if flag:
                birth_place += " "
                break
        else:
            birth_place = "\033[0;37m" + "None Provide"
            break
    print("\033[m" + "  | |__________________________________|_|\n  |/___________" +
          "\033[1;30;47m" + " BIRTH-PLACE " +
          "\033[m" + "___________|/\n\n     ____________________________________\n   /___________" +
          "\033[1;30;47m" + " LIVE-PLACE " +
          "\033[m" + "____________/ |")
    while True:
        live_place = input(
            "\033[m" + "  | | " +
            "\033[1;37;40m" + " Where do you live? " +
            "\033[m" + "             | |\n  | | " +
            "\033[0;31;40m" + " [city] " +
            "\033[m" + "                         | |\n  | | " +
            "\033[1;37;40m" + " Example:" +
            "\033[0;32;40m" + " ->Valencia " +
            "\033[m" + "            | |\n  | | " +
            "\033[1;37m" + " -> ")
        l = len(live_place)
        flag_v = False
        bool_generic = False
        if l > 0:
            if not live_place[0] == " ":
                if l == 0:
                    flag_v = True
                else:
                    flag_v = generic_text_v2(text_c2, live_place, bool_generic)
                if flag_v:
                    break
            else:
                print("\033[m" + "  | | " +
                      "\033[1;30;43m" + " Not spaces at the beginning. " +
                      "\033[m" + "   | |\n  | |                                  | |")
        else:
            break
    g_text = ""
    if not list_text_f == []:
        for i in list_text_f:
            g_text += i
        live_place = g_text
    else:
        live_place = "\033[0;37m" + "None Provide"
    print("\033[m" + "  | |__________________________________|_|\n  |/___________" +
          "\033[1;30;47m" + " LIVE-PLACE " +
          "\033[m" + "____________|/")
    list_total_info = [name, birth_date, birth_place, live_place]
    n = 0
    personal_vars = " Personal information "
    print("\033[m" + "\n    ____________________________________\n   -_______" +
          "\033[1;30;47m" + personal_vars +
          "\033[m" + "_______-")
    for i in list_total_info:
        if not i == "\033[0;37m" + "None Provide":
            print("\033[m" + "  " +
                  "\033[1;33m" + "-. " +
                  "\033[1;37;40m" + f" {i}" + "\033[m")
        else:
            print("\033[m" + "  " +
                  "\033[1;33m" + "-. " +
                  "\033[m" + f"{i}")
    print("\033[m" + "   -____________________________________-")
    re_run = input("\033[m" + "\n  " +
                   "\033[1;30;47m" + " Re-run? " +
                   "\033[m" + "\n  " +
                   "\033[1;30;47m" + " [yes] or any key to exit. " +
                   "\033[m" + "\n  " +
                   "\033[1;30;47m" + " -> ")
    if re_run == "yes":
        print("\033[m")
    else:
        break
