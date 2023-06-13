from flask import Flask, render_template,request
import pickle
import numpy as np

model = pickle.load(open('Model1.pkl','rb'))

app = Flask(__name__)
