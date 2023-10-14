import streamlit as st #library used to create webapps
import functions

todos = functions.get_todos() #this will return a list

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is for increasing your productivity.")

for todo in todos:
    st.checkbox(todo) #this will get the strings from todos.txt and turn them into lists
   
st.text_input(label="Enter a todo:", placeholder="Add a new todo...") #first arg "label" is always required