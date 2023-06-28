from flask import Flask, render_template,request
import pickle
import numpy as np

model = pickle.load(open('Model1.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def fraud():
    return render_template('index.html')


@app.route('/predict', methods = ['POST'])
def home():