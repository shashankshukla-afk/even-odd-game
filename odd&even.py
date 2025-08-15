# import random

# score = 0
# lives = 5  # Kitne chances dene hain

# print("🎯 Welcome to the Guessing Game!")
# print("Number guess karo (1 se 10 ke beech), ya 'stop' likh ke exit karo.")

# while lives > 0:
#     secret_num = random.randint(1, 10)  # Random number generate
#     guess = input("\nYour guess: ").lower()

#     if guess == "stop" or guess == "exit":
#         print("Game over! 🎮")
#         print("Your final score:", score)
#         break

#     if guess.isdigit():
#         guess = int(guess)

#         if guess == secret_num:
#             print(f"✅ Sahi jawab! Number {secret_num} tha.")
#             score += 2
#         else:
#             print(f"❌ Galat! Number {secret_num} tha.")
#             score -= 1
#             lives -= 1
#             print(f"Lives bachi: {lives}")
#     else:
#         print("❌ Sirf number ya 'stop' likho!")

# if lives == 0:
#     print("\n💀 No lives left! Game Khatam.")
#     print("Final score:", score)



import as tkinter tk 
import random

# --- Game Variables ---
score = 0
lives = 5
secret_num = random.randint(1, 10)

# --- Functions ---
def check_guess():
    global score, lives, secret_num

    guess = guess_entry.get().strip().lower()
    output_label.config(fg="black")

    if guess in ["stop", "exit"]:
        root.destroy()
        return

    if guess.isdigit():
        guess = int(guess)
        if guess == secret_num:
            score += 2
            output_label.config(text=f"✅ Sahi jawab! Number {secret_num} tha.", fg="green")
            secret_num = random.randint(1, 10)
        else:
            score -= 1
            lives -= 1
            output_label.config(text=f"❌ Galat! Number {secret_num} tha.", fg="red")
            secret_num = random.randint(1, 10)
    else:
        output_label.config(text="❌ Sirf number ya 'stop' likho!", fg="orange")

    score_label.config(text=f"Score: {score}")
    lives_label.config(text=f"Lives: {lives}")

    if lives <= 0:
        output_label.config(text=f"💀 Game Over! Final Score: {score}", fg="purple")
        submit_btn.config(state="disabled")

    guess_entry.delete(0, tk.END)

# --- GUI Setup ---
root = tk.Tk()
root.title("Number Guessing Game 🎯")
root.geometry("400x300")
root.resizable(False, False)

# Labels
title_label = tk.Label(root, text="🎯 Number Guessing Game", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

score_label = tk.Label(root, text=f"Score: {score}", font=("Arial", 12))
score_label.pack()

lives_label = tk.Label(root, text=f"Lives: {lives}", font=("Arial", 12))
lives_label.pack()

# Entry
guess_entry = tk.Entry(root, font=("Arial", 14), justify="center")
guess_entry.pack(pady=10)

# Submit Button
submit_btn = tk.Button(root, text="Submit Guess", font=("Arial", 12), command=check_guess)
submit_btn.pack(pady=5)

# Output Label
output_label = tk.Label(root, text="", font=("Arial", 12))
output_label.pack(pady=10)

# Exit Button
exit_btn = tk.Button(root, text="Exit Game", font=("Arial", 12), command=root.destroy)
exit_btn.pack(pady=5)

root.mainloop()

