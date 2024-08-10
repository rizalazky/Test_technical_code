from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

app= Flask(__name__)


@app.route("/", methods=["GET","POST"])
def hello_world():
    if request.method == 'POST' :
        data = request.get_json()
        inputText = data.get("input")
        type = data.get("type")
        if type == 'generate-ganjil' :
            return jsonify({
                "status" : 'oke',
                "data" : generateGanjil(inputText)
            })
        if type == 'generate-prima' :
            return jsonify({
                "status" : 'oke',
                "data" : generatePrima(inputText)
            })
        if type == 'generate-segitiga' :
            return jsonify({
                "status" : 'oke',
                "data" : generateSegitiga(inputText)
            })
        
    else:
        return render_template("hello.html")
    
def generatePrima(value):
    result = []
    for index in range(2, int(value) + 1):
        check = True
        for o in range(2, index + 1):
            if index % o == 0 and o != index:
                check = False
                break
        if check:
            result.append(index)
    return result

def generateSegitiga(value):
    result = []
    for i in range(len(value)):
        # if i % 2 != 0 :
        suffix = '0' * (i + 1)
        result.append(value[i] + suffix)
    return result

def generateGanjil(value):
    result = []
    for i in range(int(value)) :
        if i % 2 != 0 :
            result.append(i)
    return result
