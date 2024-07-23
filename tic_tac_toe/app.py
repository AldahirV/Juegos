from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_winner', methods=['POST'])
def check_winner():
    board = request.json['board']
    currentPlayer = request.json['currentPlayer']
    winning_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in winning_conditions:
        if all(board[i] == currentPlayer for i in condition):
            return jsonify(winner=True)
    if all(cell != '' for cell in board):
        return jsonify(draw=True)
    return jsonify(winner=False)

if __name__ == '__main__':
    app.run(debug=True, port=8080)