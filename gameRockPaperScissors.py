import random


def gameFunction(choose_user, choose_bot, v1, v2):
    # correction-arguments
    if choose_user == list_v[v1]:
        choose_user = list[v2]

    # game-match-process
    if (choose_user == "rock" and choose_bot == "scissor") or\
       (choose_user == "paper" and choose_bot == "rock") or\
       (choose_user == "scissor" and choose_bot == "paper"):
        return "You win!"
    elif (choose_user == "scissor" and choose_bot == "rock") or\
         (choose_user == "rock" and choose_bot == "paper") or\
         (choose_user == "paper" and choose_bot == "scissor"):
        return "You loss!"
    elif choose_user == choose_bot:
        return "Tie!"


# initialize-useful-variables
list = ["rock", "rocks", "paper", "papers", "scissor", "scissors"]
list_v = ["rocks", "papers", "scissors"]
list_r = ["rock", "paper", "scissor"]
n_l = len(list_v) - 1

# main-loop-game
while True:

    # choose-input
    choose = input("  Type your choose.\n"
                   "  Examples: [Rock, Paper or Scissors]\n"
                   "  ->").lower()

    # choose-of-bot
    choose_bot = list_r[random.randint(0, n_l)]

    # verification-choose-input
    flag = True
    for i in choose:
        if not i.isalpha():
            print("    Wrong input, try again.\n")
            flag = False
            break

    # flag-for-verification-choose
    if flag:

        # game-process
        result = ""
        if choose == "rock" or choose == "rocks":
            result = gameFunction(choose, choose_bot, 0, 0)
        elif choose == "paper" or choose == "papers":
            result = gameFunction(choose, choose_bot, 1, 2)
        elif choose == "scissor" or choose == "scissors":
            result = gameFunction(choose, choose_bot, 2, 4)

        # message-for-results
        print(f"\n  You: {choose}.\n"
              f"  Bot: {choose_bot}.\n"
              f"  ~{result}\n")

    else:

        # message-for-wrong-input
        print("    Wrong input, try again.\n")

    # rerun-process
    re_run = input("  Re-run? [yes] or any key to exit.\n"
                   "  ->").lower()
    if not re_run == "yes":
        break
