while True:
    question = "yes"
    num = input("  Type a positive integer number.\n  ->")
    try:
        int(num)
        num = int(num)
        div = num % 2
        if div == 0:
            question = input("    The number is even.\n"
                             "    re-run? [yes] or any key to exit.\n"
                             "      ->")
            if question != "yes":
                break
        else:
            question = input("    The number is odd.\n"
                             "    Re-run? [yes] or any key to exit.\n"
                             "      ->")
            if question != "yes":
                break
    except ValueError:
        question = input("  Incoherent digit.\n"
                         "  re-run? [yes] or any key to exit.\n"
                         "    ->")
        if question != "yes":
            break
