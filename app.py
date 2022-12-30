from flask import Flask,request,app,jsonify,url_for,render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))
scalar = pickle.load(open('scaling.pkl','rb'))