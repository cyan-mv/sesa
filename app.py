from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

""" @app.route('/')
def index():
    return render_template('result.html') """

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    fields = ["comunidad", "primer nivel", "segundo nivel", "centros"]
    #if request.method == 'POST': 
    user_input = request.form.get('field1')
    result = user_input
    return render_template('index.html', result=result)


@app.route('/generate_excel', methods=['POST'])
def generate_excel():
    try:
        # Run the script using subprocess
        subprocess.run(['python', 'generate_excel.py'], check=True)
        return "Script executed successfully"
    except Exception as e:
        return f"An error occurred: {str(e)}"


if __name__ == '__main__':
    app.run(debug=True, port=8000)
