import random


def play_game():
    number = random.randint(1, 100)
    max_attempts = 7
    attempts = 0

    print("\n===== Number Guessing Game =====")
    print("Maine 1 se 100 ke beech ek number socha hai.")
    print("Aapke paas 7 attempts hain.")

    while attempts < max_attempts:
        guess = int(input("\nApna guess enter kare: "))
        attempts += 1

        if guess < number:
            print("Too Low! Thoda bada number try karo.")

        elif guess > number:
            print("Too High! Thoda chhota number try karo.")

        else:
            print("🎉 Congratulations! Aapne sahi number guess kar liya.")
            print("Number:", number)
            print("Attempts:", attempts)
            return

    print("\n❌ Game Over!")
    print("Sahi number tha:", number)
    print("Total attempts:", attempts)


while True:
    play_game()

    again = input("\nNew round khelna hai? (yes/no): ")

    if again.lower() != "yes":
        print("Thanks for playing! 👋")
        break
