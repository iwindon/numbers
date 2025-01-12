# Math Quiz Web Application

This is a simple web application built with Flask and Jinja2 that presents a math quiz to the user. The quiz consists of 25 multiplication questions, with operands ranging from 1 to 10.

## Project Structure

The project has the following structure:


- `app.py`: This is the main Python script that runs the Flask application.
- `quiz.html`: This is the template for the quiz page. It displays the multiplication question and a form for the user to enter their answer.
- `end.html`: This is the template for the end page. It displays the user's final score.

## How to Run

1. Install the required Python packages if you haven't already:

    ```
    pip install flask
    ```

2. Run the `app.py` script:

    ```
    python3 app.py
    ```

3. Open a web browser and navigate to `http://localhost:5000` to start the quiz.

## How it Works

When you navigate to the main page, the application generates a multiplication question with two random numbers between 1 and 10. After you submit your answer, the application checks if it's correct and updates your score. This process repeats until you've answered 25 questions, at which point your final score is displayed.