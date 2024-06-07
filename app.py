from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    session['score'] = 0
    session['count'] = 0
    return redirect(url_for('quiz'))

@app.route('/quiz')
def quiz():
    if session['count'] == 25:
        return redirect(url_for('end'))

    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    session['answer'] = num1 * num2
    session['count'] += 1
    return render_template('quiz.html', num1=num1, num2=num2, count=session['count'])

@app.route('/result', methods=['POST'])
def result():
    answer = request.form.get('answer')
    if int(answer) == session['answer']:
        session['score'] += 1
    return redirect(url_for('quiz'))

@app.route('/end')
def end():
    return render_template('end.html', score=session['score'])

if __name__ == '__main__':
    app.run(debug=True)