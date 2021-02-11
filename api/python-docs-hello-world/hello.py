import matplotlib
matplotlib.use('Agg')
from flask import Flask, render_template, request
from flask import flash, request, redirect, url_for
from input_data import customfunct
from shutil import copy
import string
import random
import os

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'GET':
        dirs = os.listdir()
        if 'tesla.txt' in dirs:
            os.remove("tesla.txt")
        if 'final.png' in dirs:
            os.remove('final.png')
        
        return render_template('index.html', output=False)
    else:
        file = request.files['file']
        # filename = secure_filename(file.filename)
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file.save(os.path.join(dir_path, 'tesla.txt'))
        customfunct('tesla.txt')
        letters = string.ascii_lowercase
        name = ''.join(random.choice(letters) for i in range(10))+'.png'
        os.rename('final.png', name)
        #print(os.path.dirname(os.path.realpath(__file__))+'\\static')
        copy(name, os.path.dirname(os.path.realpath(__file__))+'/static')
        print(os.path.dirname(os.path.realpath(__file__)))
        # return render_template('index.html', output=True)
        return render_template('index.html', output=True, img = name)

@app.route('/output', methods=['GET'])
def output():
    return render_template('index.html', output=True)

if __name__ == '__main__':
    app.run(debug=True)
