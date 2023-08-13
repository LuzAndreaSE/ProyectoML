# Importar librerias
import streamlit as st


st.set_page_config(
    page_title="Hiperparametros para clasificación de diabetes",
    page_icon=":microscope:",
)

st.write("# ¡Bienvenidos clasificador de hiperparámetros de diabetes! :syringe:")

st.sidebar.success("Seleccione un demo")
st.markdown("""
Este proyecto tiene como objetivo diagnosticar la diabetes utilizando 8 características proporcionadas en el conjunto de datos PIMA.

# Análisis de datos y revisión de la información estadística y descriptiva.

    **Qué es la diabetes?**

La diabetes es una enfermedad crónica que afecta a la capacidad del organismo para transformar los alimentos en energía. El proceso consiste en descomponer los alimentos en azúcar y liberarlo en el torrente sanguíneo, regulado por la insulina. En la diabetes, el organismo no produce suficiente insulina o se vuelve resistente a sus efectos, lo que provoca niveles elevados de azúcar en sangre y posibles complicaciones de salud. Los tres tipos principales de diabetes son la de tipo 1, la de tipo 2 y la gestacional, cada una con características distintas.

**Diabetes tipo 1** Es el resultado de una reacción autoinmune que afecta a la producción de insulina y suele diagnosticarse en niños y adultos jóvenes..

**Diabetes tipo 2** implica resistencia a la insulina y se diagnostica comúnmente en adultos, pero cada vez en poblaciones más jóvenes.

**La diabetes gestacional** se produce durante el embarazo y puede elevar el riesgo de problemas de salud tanto para la madre como para el bebé. Aunque la diabetes no tiene cura, los cambios en el estilo de vida, como el control del peso, la alimentación sana y la actividad física, pueden mejorar mucho su control y prevención.


* **Pregnancies:** Número de embarazos  
* **Glucose:**  Concentración plasmática de glucosa a las 2 horas   
* **BloodPressure:** Presión arterial diastólica (mm Hg)
* **SkinThickness:** Espesor del pliegue cutáneo del tríceps (mm) 
* **Insulin:**  Insulina sérica a las 2 horas (mu U/ml)        
* **BMI:** IMC (peso en kg/(altura en m)^2)
* **DiabetesPedigreeFunction:** Función de pedigrí de la diabetes       
* **BAge:** Edad (años)



"""
)



# Pie de página
st.markdown("Creado por Luz Andrea")
