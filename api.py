import enchant
from itertools import permutations
from flask_cors import CORS
from flask import Flask,jsonify,request

app = Flask(__name__)
CORS(app)
language = enchant.Dict("en_US")

@app.route('/', methods=['GET', 'POST'])
def get_inputs():
    if request.method == 'GET':
        return "Hi! Thank you for hitting me. Please try hitting using POST method with args letters and size."

    letters = request.json['letters'].strip()
    size = request.json['size']
    if not size:
        size = len(letters)
    else:
        size = int(size)
    return get_permutation(letters, size)


def get_permutation(letter_list, length=None):
    permutation = permutations(letter_list, length)
    return permutation_processor(permutation)

def permutation_processor(permutation):
    word_list = []
    for i in list(permutation):
        joined_word = "".join(i)
        check_words(joined_word, word_list)
    response = {
        "msg": "Here are the results. Bingo!",
        "result": word_list
    }
    return jsonify(response)

def check_words(word, word_list):
    if (language.check(word)):
        word_list.append(word)

if __name__ == "__main__":
    app.run()