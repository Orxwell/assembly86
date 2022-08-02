while True:
    text = input("  Letter counter, input a text:\n"
                 "  ->")
    letters = 0
    for i in text:
        bool = i.isalpha()
        if bool:
            letters += 1
    print(f"    The total of letters is {letters}.\n")
    re_run = input("  Re-run?\n"
                   "  [yes] or any key to exit.\n"
                   "    ->")
    if re_run != "yes":
        break
    else:
        print("")
