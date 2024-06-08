"""Flask module for a simple multiplication quiz game."""
import random
from flask import Flask, render_template, request, session, redirect, url_for


app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    """
    Display the home page.
    """
    session['score'] = 0
    session['count'] = 0
    return redirect(url_for('quiz'))

@app.route('/quiz')
def quiz():
    """
    Display the quiz page.
    """
    if session['count'] == 25:
        return redirect(url_for('end'))

    # Reset the count and clear the wrong questions at the start of a new game
    if session['count'] == 0:
        session['wrong_questions'] = []

    session['num1'] = random.randint(1, 10)
    session['num2'] = random.randint(1, 10)
    session['answer'] = session['num1'] * session['num2']
    session['count'] += 1
    return render_template('quiz.html', num1=session['num1'], num2=session['num2'], count=session['count'], score=session['score'], wrong_answer=session.get('wrong_answer', False), correct_answer=session.get('correct_answer', 0))
@app.route('/result', methods=['POST'])
def result():
    """
    Process the quiz result.
    """
    answer = request.form.get('answer')
    if int(answer) == session['answer']:
        session['score'] += 1
        session['wrong_answer'] = False
    else:
        session['wrong_answer'] = True
        # Store the question and correct answer in the session
        question = f"{session.get('num1')} * {session.get('num2')}"
        correct_answer = session['answer']
        if 'wrong_questions' not in session:
            session['wrong_questions'] = []
        session['wrong_questions'].append((question, correct_answer))
    return redirect(url_for('quiz'))

@app.route('/end')
def end():
    """
    Display the end page with the score and wrong answers.
    """
    wrong_questions = session.get('wrong_questions', [])
    return render_template('end.html', score=session['score'], wrong_questions=wrong_questions)

if __name__ == '__main__':
    app.run(debug=True)
