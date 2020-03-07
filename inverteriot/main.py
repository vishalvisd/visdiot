from flask import *

app = Flask(__name__)

currentInstructions = []

@app.route('/getinstruction', methods=['GET'])
def getCurrentInstruction():
    global currentInstructions
    nextInstruction = currentInstructions.pop() if currentInstructions else None
    return jsonify(nextInstruction)

@app.route('/setinstruction')
def setCurrentInstruction():
    instruction = request.args.get('ins', type=str)
    global currentInstructions
    currentInstructions.append(instruction)

    return jsonify(instruction)

if __name__ == '__main__':
    app.run()