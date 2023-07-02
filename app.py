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
    data = request.form.to_dict()
    data['Time'] = float(request.form.get('Time'))
    data['v1'] = float(request.form.get('v1'))
    data['v2'] = float(request.form.get('v2'))
    data['v3'] = float(request.form.get('v3'))
    data['v4'] = float(request.form.get('v4'))
    data['v5'] = float(request.form.get('v5'))
    data['v6'] = float(request.form.get('v6'))
    data['v7'] = float(request.form.get('v7'))
    data['v8'] = float(request.form.get('v8'))
    data['v9'] = float(request.form.get('v9'))
    data['v10'] = float(request.form.get('v10'))
    data['v11'] = float(request.form.get('v11'))
    data['v12'] = float(request.form.get('v12'))
    data['v13'] = float(request.form.get('v13'))
    data['v14'] = float(request.form.get('v14'))
    data['v15'] = float(request.form.get('v15'))
    data['v16'] = float(request.form.get('v16'))
    data['v17'] = float(request.form.get('v17'))
    data['v18'] = float(request.form.get('v18'))
    data['v19'] = float(request.form.get('v19'))
    data['v20'] = float(request.form.get('v20'))
    data['v21'] = float(request.form.get('v21'))
    data['v22'] = float(request.form.get('v22'))
    data['v23'] = float(request.form.get('v23'))
    data['v24'] = float(request.form.get('v24'))
    data['v25'] = float(request.form.get('v25'))
    data['v26'] = float(request.form.get('v26'))
    data['v27'] = float(request.form.get('v27'))
    data['v28'] = float(request.form.get('v28'))
    data['Amount'] = float(request.form.get('Amount'))
    
    

    arr = np.array([list(data.values())])
    pred = model.predict(arr)
    return render_template('result.html', data=pred)

    


if __name__ == "__main__":
    app.run(debug = True)

