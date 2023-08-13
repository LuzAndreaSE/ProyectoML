# Importar librerias
import streamlit as st
import pandas as pd
from urllib.error import URLError
import matplotlib.pyplot as plt

# Importamos los datasets que vamos a utilizar
folder ='data'
archivo_data = 'diabetes.csv'
data = pd.read_csv(folder+'/'+archivo_data, sep=',')

# Definimos las clases que vamos a utilizar y reemplazamos su
nombre_clases = {0:"No diabético",1:"Diabético"}

d = data.copy()
d['Outcome'] = d['Outcome'].replace(nombre_clases)
caracteristicas = d.drop(['Outcome'], axis=1)
etiquetas = d['Outcome'] 


st.set_page_config(page_title="DataFrame demo", page_icon=":ballot_box_with_check:")

st.markdown("# DataFrame Demo")
st.sidebar.header("DataFrame Demo")
st.write(
    """
Vamos a visualizar los datos de la base de datos 
"""
)
# Mostrar el data frame en streamlit
st.dataframe(d.head())
st.markdown("<hr style='margin-top: 2px; margin-bottom: 15px;'>", unsafe_allow_html=True)

# Realizar el conteo de las clases de la 
conteo = d['Outcome'].value_counts()
st.dataframe(conteo)

indices = conteo.index.tolist() # Estas son las clases

#Graficar el conteo de las clases en un gfrafico de torta
fig, ax = plt.subplots()
ax.pie(list(conteo.values), labels=indices, autopct='%1.1f%%')
ax.axis('equal') # Para asegurar que el gráfico sea circular

# Mostrar el gráfico en Streamlit
st.pyplot(fig)

