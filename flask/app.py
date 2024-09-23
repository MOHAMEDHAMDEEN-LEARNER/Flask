from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')  # Use the correct 'templates' folder

@app.route('/math', methods=['POST'])
def math_ops():
    if request.method == 'POST':  # Fix request.method check
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        
        # Perform operations
        if ops == 'add':
            r = num1 + num2
            result = f"The sum of {num1} and {num2} is {r}"
        elif ops == 'subtract':
            r = num1 - num2
            result = f"The subtraction of {num1} from {num2} is {r}"
        elif ops == 'multiply':
            r = num1 * num2
            result = f"The multiplication of {num1} and {num2} is {r}"
        elif ops == 'divide':
            if num2 == 0:
                result = "Error: Division by zero is not allowed"
            else:
                r = num1 / num2
                result = f"The division of {num1} by {num2} is {r}"
        else:
            result = "Invalid operation selected"

        return render_template('result.html', result=result)  # Correct file path

if __name__ == "__main__":
    app.run(debug=True)