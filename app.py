from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
# load the model
model = pickle.load(open('Loan.pkl', 'rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html', **locals())


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    Gender = float(request.form['Gender'])
    Married = float(request.form['Married'])
    Dependents = float(request.form['Dependents'])
    Education = float(request.form['Education'])
    Self_Employed = float(request.form['Self_Employed'])
    Credit_History = float(request.form['Credit_History'])
    Property_Area = float(request.form['Property_Area'])

    result = model.predict([[Gender	,Married,	Dependents,	Education,	Self_Employed,	Credit_History,	Property_Area]])[0]
    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)


    							