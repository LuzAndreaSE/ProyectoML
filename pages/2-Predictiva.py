import pickle
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import sklearn
import requests

def solicitud_API(muestra: list):
    #URL de la API
    urlApi = 'http://127.0.0.1:8000/predict'
    
    # Datos de entrada
    data = {
        "data": muestra
    }
    
    #Realizar la solicitud POST a la API
    response = requests.post(urlApi, json=data)
    
    # Verificar el código de estado de la respuesta
    if response.status_code == 200:
        # Obtener la respuesta en formato JSON
        result = response.json()
        
        # Obtener la predicción
        prediction = result["prediction"]
        
        # Imprimir la predicción
        print("Predicción:", prediction)
        return prediction
    else:
        print("Error en la solicitud", response.status_code)
        return None
    

with open('models/modeloD_GR.pkl', 'rb') as gb:
    modelo = pickle.load(gb)

# Agregamos CSS personalizado para cambiar el color del recuadro a naranja
st.markdown(
    """
    <style>
    div[data-baseweb="select"]>div:first-child {border-color: orange !important;}
    </style>
    """, unsafe_allow_html=True
)

st.subheader("Machine learning modelo seleccionado")

st.write("Definición del algoritmo implementado para predecir si una persona sufre de diabetes")

st.subheader("caracteristicas de entrada")
features = ['Número de embarazos (Pregnancies)', 'Concentración de glucosa (Glucose)', 'Presión diastólica (BloodPressure)', 
            'Espesor pliegue tríceps (SkinThickness)', 'Insulina sérica  (Insulin)', 'IMC (BMI)', 
            'Función de pedigrí (DPF)', 'Edad (Age)']
st.write("A continuación, ingrese los valores de las características que serán utilizadas para la clasificación de diabétes con los modelos de Machine Learning:")        


def user_input_parameters():
    inputs = {}
    for i, feature in enumerate(features):
        row, col = i // 3, i % 3
        with st.container():
            if i % 3 == 0:
                cols = st.columns(3)
            inputs[feature] = cols[col].text_input(feature)
    data_features = {
        'Pregnancies' : inputs[features[0]],
        'Glucose' : inputs[features[1]],
        'BloodPressure' : inputs[features[2]],
        'SkinThickness' : inputs[features[3]],
        'Insulin': inputs[features[4]],
        'BMI' : inputs[features[5]],
        'DPF' : inputs[features[6]],
        'Age' : inputs[features[7]],
         }
    features_df = pd.DataFrame(data_features, index = [0])
    return features_df

df = user_input_parameters()


st.subheader("Modelo para detectar diabetes")

# Crear un nuevo DataFrame con una fila adicional 'Valor'
df = df.T.reset_index()
df.columns = ['Característica', 'Valor']
df = df.set_index('Característica').T

st.table(df)
    

# Crear dos botones 'PREDECIR' y 'LIMPIAR' en la misma fila
predict_button, clear_button = st.columns(2)
predict_clicked = predict_button.button('PREDECIR')
prediction = ''
if predict_clicked:
    inputs_validos = True
    
# Validar que todos los campos contengan valores numéricos
    for value in df.values.flatten():
        if not value or not value.isdigit():
            st.warning("Por favor, complete todos los datos con valores numéricos antes de hacer la predicción")
            break
        else:
            prediction = modelo.predict(df)[0]
    
    # Crear un diccionario para asociar las predicciones con 
    prediction_descriptions = {
        '0': 'No diabético',
        '1': 'Es diabético'
    }
            
    # Mostrar la descripción completa de la predicción
    if prediction == 1:
        st.warning("Alerta: Presta atención posibls Diabetes")
    else:
        st.success("No se detectó enfermedad diabética")