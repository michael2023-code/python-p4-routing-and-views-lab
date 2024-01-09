#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/') # The / route for the index view, which returns an HTML header.
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>') # The /print/<param> route for the print_string view, which takes a string parameter and prints it to the console and displays it in the browser.
def print_string(param):
    print(param)
    return f'<h2>Printed: {param}</h2>'

@app.route('/count/<int:param>') # The /count/<param> route for the count view, takes an integer parameter and displays numbers in the range of that parameter on separate lines.
def count(param):
    numbers = '<br>'.join(str(i) for i in range(param))
    return f'<h2>Counting:</h2><p>{numbers}</p>'

@app.route('/math/<float:num1><operation><float:num2>') # The /math/<num1><operation><num2> route for the math view,takes three parameters: two numbers and an operation. It performs the mathematical operation and displays the result.
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Cannot divide by zero!"
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation"
    
    return f'<h2>Result: {result}</h2>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
