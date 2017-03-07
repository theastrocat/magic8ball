import numpy as np
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('eight_ball.html')


@app.route('/solve', methods = ['POST'])
def solve():
    user_data = request.json
    name, question = user_data['name'], user_data['question']
    answer = _get_answer(name,question)
    return jsonify({'answer': answer})

def _get_answer(name, question):
    if name == '' or question == '':
        answer = 'Please enter name and question.'
    else:
        answers = ['Yes', 'No', 'Maybe', 'Ask again later']
        np.random.seed(int(str(hash(name+question))[:3]))
        choice = np.random.choice(answers)
        answer = str(choice) + ', ' + str(name)
    return answer

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
