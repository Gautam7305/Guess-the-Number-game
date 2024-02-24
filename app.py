from flask import Flask, render_template, request

import random

app = Flask(__name__)

secret_number = random.randint(1, 100)
attempts = 0
message = ""

@app.route('/')
def home():
    return render_template("index.html", message=message)

@app.route('/', methods=['POST'])
def check_guess():
    global secret_number, attempts, message

    try:
        guess = int(request.form['guess'])
    except ValueError:
        message = "Please enter a valid number."
        return render_template('index.html', message=message)

    attempts += 1

    if guess == secret_number:
        message = f"Congratulations! You've guessed the number in {attempts} attempts."
        secret_number = random.randint(1, 100)
        attempts = 0
    elif guess < secret_number:
        message = "Your guess is too low. Try again."
    else:
        message = "Your guess is too high. Try again."

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)