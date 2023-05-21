import sys
print(sys.executable)


from flask import Flask, render_template, request
from gptUpdaterUi import process_command

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    response = ''
    if request.method == 'POST':
        command = request.form['command']
        response = process_command(command)
    return render_template('index.html', response=response)

if __name__ == "__main__":
    app.run(debug=True)



