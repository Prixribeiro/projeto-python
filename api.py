#!/usr/local/bin/python3
import os, sys
from flask import Flask, render_template, request
import emoji

app = Flask(__name__, template_folder="./src/views")

@app.route("/", methods=["GET", "POST"])
def home():
    if (request.method == "GET"):
        return render_template("index.html")
    else : 
        if (request.form["num1"] != "" and request.form["num2"] != ""):
            num1 = request.form["num1"]
            num2 = request.form["num2"]

            if (request.form["opc"] == "soma"):
                soma = int(num1) + int(num2)
                return "A soma dos valores é: " + str(soma) + (' ✅')

            elif (request.form["opc"] == "subt"):
                subt = int(num1) - int(num2)
                return "A subtração dos valores é: " + str(subt) + (' ✅')

            elif (request.form["opc"] == "mult"):
                mult = int(num1) * int(num2)
                return "A multiplicação dos valores é: " + str(mult) + (' ✅')

            else:
                divi = int(num1) // int(num2)
                return "A divisão dos valores é: " + str(divi) + (' ✅')

        else:
            return "Informe um valor válido!"

@app.errorhandler(404)
def not_found(error):
    return ("Essa página não existe! Sorry!")

app.run(debug=True)
