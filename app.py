from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/run_script', methods=['POST'])
# def run_script():
#     try:
#         # Run the script using subprocess
#         subprocess.run(['python', 'generate_excel.py'], check=True)
#         return "Script executed successfully"
#     except Exception as e:
#         return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True, port=8000)
