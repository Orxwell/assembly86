# theory-of-conjuntions-pertenence-code
class NumberConjuntion:
    def __init__(self):
        self.inputNum()

    def inputNum(self):
        num = input("\n  Digit a number, or the name of a number:\n"
                    "  ->").lower()
        true_num = num
        if not (num == "pi" or num == "e" or num == "golden"):
            num = num.replace("i", "j")
            try:
                complex(num)
            except ValueError:
                print("    Incoherent complex.\n")
                return False
            num = complex(num)
            if num.real == 0.0 and abs(num.imag) > 0.0:
                self.imaginary(true_num)
            elif abs(num.real) > 0.0 and num.imag == 0.0:
                self.real(num, True, true_num)
            else:
                self.complex(true_num)
        else:
            self.real(num, False, None)

    @staticmethod
    def imaginary(true_num):
        print(f'    The {true_num} belongs to the set [i].\n'
              '    (pure imaginary)\n')
        return True

    @staticmethod
    def complex(true_num):
        print(f'    The {true_num} belongs to the set [C].\n'
              '    (complexes)\n')
        return True

    @staticmethod
    def real(num, flag, true_num):
        if flag:
            number = int(num.real)
            if not abs((abs(number) - abs(num.real))) > 0:
                if num.real > 0:
                    print(f'    The {true_num} belongs to the set.\n'
                          '    [Real, Quotient, Zahlen, Natural]')
                else:
                    print(f'    The {true_num} belongs to the set.\n'
                          '    [Real, Quotient, Zahlen]')
            else:
                if num.real > 0:
                    print(f'    The {true_num} belongs to the set.\n'
                          '    [Real, Quotient, Fractional, Natural]')
                else:
                    print(f'    The {true_num} belongs to the set.\n'
                          '    [Real, Quotient, Fractional]')
        else:
            print(f"    The {num} number belongs to the set.\n"
                  "    [Real, Irrational, Natural]")
        return True


while True:
    numberObject = NumberConjuntion()
    if numberObject:
        re_run = input("  Re-run? [yes] or any key to exit.\n  ->").lower()
        if not re_run == "yes":
            break
