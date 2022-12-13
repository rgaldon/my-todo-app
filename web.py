import streamlit as st
import functions

def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state['new_todo'] = ''
    return


todos = functions.get_todos()

st.title('My To Do App')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='Add To DO', placeholder='Add new To Do.',
              on_change=add_todo, key='new_todo')

st.session_state