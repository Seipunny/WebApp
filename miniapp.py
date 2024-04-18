from flask import Flask, request, render_template_string

app = Flask(__name__)

# Генерируем случайное число, которое пользователь должен угадать
import random
target_number = random.randint(1, 100)

@app.route('/')
def index():
    return render_template_string("""
        <h1>Угадай число!</h1>
        <p>Я загадал число между 1 и 100, попробуй угадать его.</p>
        <form action="/guess" method="post">
            <input type="number" name="number" min="1" max="100" required>
            <input type="submit" value="Угадать">
        </form>
    """)

@app.route('/guess', methods=['POST'])
def guess():
    user_guess = int(request.form['number'])
    if user_guess < target_number:
        message = "Нет, загаданное число больше. Попробуйте еще раз!"
    elif user_guess > target_number:
        message = "Нет, загаданное число меньше. Попробуйте еще раз!"
    else:
        message = "Поздравляем, вы угадали число!"
    return render_template_string(f"""
        <h1>{message}</h1>
        <p>Если хотите играть еще раз, <a href="/">нажмите сюда</a> чтобы загадать новое число.</p>
    """)

if __name__ == "__main__":
    app.run(debug=True)
