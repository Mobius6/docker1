from flask import Flask
import random as rd
app = Flask(__name__)
@app.route("/")
def test():
    loto = []
    while len(loto) < 6:
        number = rd.randint(1,49)
        if number not in loto:
            loto.append(number)
    result=f'Lottery Winning Numbers: {loto}'
    return "<h1>Flask Server is Working!</h1>"+result
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("8080"), debug=True)
