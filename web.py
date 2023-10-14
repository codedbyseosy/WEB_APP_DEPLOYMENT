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

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo) #this will get the strings from todos.txt and turn them into lists
                      #note: all checkboxes have the same key, hence, to allow each todo 
                      #to have a separate key, we call the key arg as "todo"
                      #values will be equal to false when unchecked and true when checked
    
    if checkbox: #default value is "true"
        todos.pop(index)
        functions.write_todos(todos) #after removing todo, rewrite todos.txt with the new list
        del st.session_state[todo] #using the key of the widget which is todo, delete the completed
                                   #todo from the session state
        st.rerun() #used to rerun the code, this is needed for checkboxes
   
st.text_input(label="Enter a todo:", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo") #first arg "label" is always required
                                                  #add_todo is the callback function

st.session_state #session state is like a dictionary that contains pairs of data that the user enters
                 #it cintains the information of the widgets, i.e. the checkboxes and inoutbox
                 #new_todo is the key