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
    print("Form Data:", data)
    required_fields = ['Time', 'v1','v2','v3','v4','v5','v6','v7','v8','v9','v10','v11','v12','v13','v14','v15','v16','v17','v18','v19','v20','v21','v22','v23','v24','v25','v26','v27','v28','v29','Amount']


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
    
    # Check if any required field is empty
    for field in required_fields:
        if field not in data or data[field] == "":
            return "Error: Please fill out all required fields."

    # Convert fields to float
    for field in required_fields:
        data[field] = float(data[field])

    arr = np.array([list(data.values())])
    pred = model.predict(arr)
    return render_template('result.html', data=pred)

    


if __name__ == "__main__":
    app.run(debug = True)

