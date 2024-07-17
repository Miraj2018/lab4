#!/usr/bin/env python
# coding: utf-8

# In[8]:


from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)


model = joblib.load('fish_model.pkl')  # Adjust filename and path as needed

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        
        input_data = request.form.to_dict()
        
       
        prediction = model.predict(input_data)

        
        result = {'prediction': prediction}

        
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




