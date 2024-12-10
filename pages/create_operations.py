import streamlit as st
import db_fxns as db



task_statuses = ['Not Started', 'In Progress', 'Completed']
st.subheader("Add Items")

col1, col2 = st.columns(2)

with col1:
  task = st.text_area(label="Task to Do", placeholder="Enter task here")
with col2:
  status = st.selectbox(label="Status", options=task_statuses)  
  
  due_date = st.date_input(label="Due Date", format="MM/DD/YYYY")
  if st.button(label="Add Task"):
    db.insert_data(task, status, due_date)
    # st.success('Task added successfully', icon="✅")

    link = st.page_link("pages/read_operations.py", label="View Data", icon="📖")
