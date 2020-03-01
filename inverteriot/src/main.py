from flask import *

app = Flask(__name__)

possibleInstructions = ('off', 'on')
currentInstructions = []

@app.route('/getinstruction', methods=['GET'])
def getCurrentInstruction():
    global currentInstructions
    nextInstruction = currentInstructions.pop() if currentInstructions else None
    return jsonify(nextInstruction)

@app.route('/setinstruction')
def setCurrentInstruction():
    isInstructionSet = False
    instruction = request.args.get('ins', type=str)
    if instruction in possibleInstructions:
        global currentInstructions
        currentInstructions.append(instruction)
        isInstructionSet = True
    else:
        isInstructionSet = "Unknown Instruction"

    return jsonify(isInstructionSet)

if __name__ == '__main__':
    app.run()