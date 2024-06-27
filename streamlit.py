import streamlit as st

st.write("Displaying an image:")
st.image("path/to/image.png", caption="Image caption", use_column_width=True)

st.write("Choose a number:")
number = st.slider("Number", min_value=1, max_value=100, value=50)
st.write(f"You chose: {number}")

if st.button("Click me!"):
    st.write("You clicked the button!")

slider_value = st.slider("Select a value:", min_value=0, max_value=100, value=50)
st.write(f"Selected value: {slider_value}")

checkbox_value = st.checkbox("Show content")
if checkbox_value:
    st.write("Content displayed.")
name = st.text_input("Enter your name:", "Type here")
st.write(f"Hello, {name}!")

options = ["Option 1", "Option 2", "Option 3"]
selections = st.multiselect("Choose multiple options:", options)
st.write(f"You chose: {', '.join(selections)}")

uploaded_file = st.file_uploader("Choose a file to upload:", type=["csv", "txt", "xlsx"])
if uploaded_file is not None:
    st.write(f"File uploaded: {uploaded_file.name}")



import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt




########## upload the dataset using uploader ###############
# uploaded_file = st.file_uploader("Upload your dataset (CSV file):")

# if uploaded_file:
#     column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
#     data = pd.read_csv(uploaded_file, header=None, names=column_names)
#     st.write("### Raw Data")
#     st.dataframe(data)



def load_iris_data():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
    data = pd.read_csv(url, header=None, names=column_names)
    return data

data = load_iris_data()

st.title("Iris Dataset Explorer")
st.write("Explore the Iris dataset by answering the following questions:")

# Display the raw data
if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.dataframe(data)

# Question 1: Show the average sepal length for each species
if st.checkbox("Show the average sepal length for each species"):
    st.subheader("Average Sepal Length per Species")
    avg_sepal_length = data.groupby("species")["sepal_length"].mean()
    st.write(avg_sepal_length)

# Question 2: Display a scatter plot comparing two features
st.subheader("Compare two features using a scatter plot")
feature_1 = st.selectbox("Select the first feature:", data.columns[:-1])
feature_2 = st.selectbox("Select the second feature:", data.columns[:-1])

scatter_plot = px.scatter(data, x=feature_1, y=feature_2, color="species", hover_name="species")
st.plotly_chart(scatter_plot)

# Question 3: Filter data based on species
st.subheader("Filter data based on species")
selected_species = st.multiselect("Select species to display:", data["species"].unique())

if selected_species:
    filtered_data = data[data["species"].isin(selected_species)]
    st.dataframe(filtered_data)
else:
    st.write("No species selected.")

# Question 4: Display a pairplot for the selected species
if st.checkbox("Show pairplot for the selected species"):
    st.subheader("Pairplot for the Selected Species")

    if selected_species:
        sns.pairplot(filtered_data, hue="species")
    else:
        sns.pairplot(data, hue="species")
        
    st.pyplot()

# Question 5: Show the distribution of a selected feature
st.subheader("Distribution of a Selected Feature")
selected_feature = st.selectbox("Select a feature to display its distribution:", data.columns[:-1])

hist_plot = px.histogram(data, x=selected_feature, color="species", nbins=30, marginal="box", hover_data=data.columns)
st.plotly_chart(hist_plot)