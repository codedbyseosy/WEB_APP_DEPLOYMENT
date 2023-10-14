import streamlit as st #library used to create webapps
import functions

todos = functions.get_todos() #this will return a list

def add_todo(): #when user presses enter, this is called and the updated todo is written in todos.txt
    todo = st.session_state["new_todo"] + "\n" #to get the string typed into the input box
                                        #this allows us to extract the values for the key "new_todo"
    todos.append(todo)
    functions.write_todos(todos)
    

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is for increasing your productivity.")

for todo in todos:
    st.checkbox(todo) #this will get the strings from todos.txt and turn them into lists
   
st.text_input(label="Enter a todo:", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo") #first arg "label" is always required
                                                  #add_todo is the callback function

st.session_state #session state is like a dictionary that contains pairs of data that the user enters
                        #new_todo is the key