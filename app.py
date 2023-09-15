from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('Model1.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def fraud():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def home():
    try:
        # Validate and convert form data to float
        data1 = float(request.form.get('Time')) if request.form.get('Time') else 0.0
        data2 = float(request.form.get('v1')) if request.form.get('v1') else 0.0
        data3 = float(request.form.get('v2')) if request.form.get('v2') else 0.0
        data4 = float(request.form.get('v3')) if request.form.get('v3') else 0.0
        data5 = float(request.form.get('v4')) if request.form.get('v4') else 0.0
        data6 = float(request.form.get('v5')) if request.form.get('v5') else 0.0
        data7 = float(request.form.get('v6')) if request.form.get('v6') else 0.0
        data8 = float(request.form.get('v7')) if request.form.get('v7') else 0.0
        data9 = float(request.form.get('v8')) if request.form.get('v8') else 0.0
        data10 = float(request.form.get('v9')) if request.form.get('v9') else 0.0
        data11 = float(request.form.get('v10')) if request.form.get('v10') else 0.0
        data12 = float(request.form.get('v11')) if request.form.get('v11') else 0.0
        data13 = float(request.form.get('v12')) if request.form.get('v12') else 0.0
        data14 = float(request.form.get('v13')) if request.form.get('v13') else 0.0
        data15 = float(request.form.get('v14')) if request.form.get('v14') else 0.0
        data16 = float(request.form.get('v15')) if request.form.get('v15') else 0.0
        data17 = float(request.form.get('v16')) if request.form.get('v16') else 0.0
        data18 = float(request.form.get('v17')) if request.form.get('v17') else 0.0
        data19 = float(request.form.get('v18')) if request.form.get('v18') else 0.0
        data20 = float(request.form.get('v19')) if request.form.get('v19') else 0.0
        data21 = float(request.form.get('v20')) if request.form.get('v20') else 0.0
        data22 = float(request.form.get('v21')) if request.form.get('v21') else 0.0
        data23 = float(request.form.get('v22')) if request.form.get('v22') else 0.0
        data24 = float(request.form.get('v23')) if request.form.get('v23') else 0.0
        data25 = float(request.form.get('v24')) if request.form.get('v24') else 0.0
        data26 = float(request.form.get('v25')) if request.form.get('v25') else 0.0
        data27 = float(request.form.get('v26')) if request.form.get('v26') else 0.0
        data28 = float(request.form.get('v27')) if request.form.get('v27') else 0.0
        data29 = float(request.form.get('v28')) if request.form.get('v28') else 0.0
        data30 = float(request.form.get('Amount')) if request.form.get('Amount') else 0.0

        arr = np.array([[data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14,
                         data15, data16, data17, data18, data19, data20, data21, data22, data23, data24, data25, data26,
                         data27, data28, data29, data30]])
        
        predict = model.predict(arr)
        return render_template('result.html', data=predict)

    except ValueError as e:
        # Handle the case where the input is not a valid number
        error_message = "Error: Invalid input. Please make sure all fields are filled with valid numbers."
        return render_template('error.html', error=error_message)

if __name__ == "__main__":
    app.run(debug=True)
