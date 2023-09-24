from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    try:
        # Run the script using subprocess
        subprocess.run(['python', 'generate_excel.py'], check=True)
        return "Script executed successfully"
    except Exception as e:
        return f"An error occurred: {str(e)}"

""" @app.route('/process_form', methods=['POST'])
def process_form():
    field1 = request.form.get('field1')
    field2 = request.form.get('field2')
    field3 = request.form.get('field3')
    field4 = request.form.get('field4')

    # Create a list with the values
    input_values = [field1, field2, field3, field4]

    # Do something with the input_values list
    # ...

    return render_template('result.html', input_values=input_values) """
    

if __name__ == '__main__':
    app.run(debug=True, port=8000)
