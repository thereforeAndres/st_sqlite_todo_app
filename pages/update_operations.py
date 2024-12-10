import streamlit as st
import db_fxns as db
import pandas as pd



st.subheader("Update Data")
tasks = db.read_data()
tasks_df = pd.DataFrame(
  tasks,
  columns=[
    "Task ID", 
    "Task Name", 
    "Task Status", 
    "Task Due Date"]
)

with st.expander(label="Current  Data"):
  st.write(tasks_df)

#this should be GLOBAL and imported:
task_statuses = ['Not Started', 'In Progress', 'Completed']



if not tasks_df.empty:
  
  
  ######################## #Task LIKE Match by NAME
  
  with st.expander(label="View Task IDs"):
  
    # st.write(db.read_tasknames()) #sanity check
    list_of_tasks = [
      i[0] for i in db.read_tasknames()
    ]
    # st.write(list_of_tasks) #another sanity check
    selected_task = st.selectbox(
      label="Select a Task to Update",
      options=list_of_tasks
    )
    # if selected_task:
    st.write(selected_task)
    selected_result = db.get_tasks_by_name(selected_task)
    st.write(selected_result)
  
  
  
  
  
  
  
  ######################## #Task by ID
  
  task_selected = st.selectbox(
    label="Task ID & Name",
    options=[(f"{row['Task ID']} - {row['Task Name']}", row['Task ID']) for index, row in tasks_df.iterrows()],
    format_func=lambda x: x[0]
  )
  id = task_selected[1]
  
  st.subheader("Current Task Data:")
  
  if id:
    selected_task = db.get_task_by_id(id)
    s_task_name = selected_task[0][1]
    s_task_status = selected_task[0][2]
    s_task_due_date = selected_task[0][3]
  
    
    
    
  
    task = st.text_area(label="Task to Do", value=s_task_name)
    
    status = st.selectbox(
      label="Status", 
      index=task_statuses.index(s_task_status), 
      options=task_statuses
    )  
    st.write(s_task_due_date)
    due_date = st.date_input(
      label="Due Date", 
      value=pd.to_datetime(s_task_due_date).date(),
      format="MM/DD/YYYY")
    if st.button(label="Update Task"):
      # db.insert_data(task, status, due_date)
      db.update_data(id, task, status, due_date)
      # message = ("Task updated successfully")
      # st.success(message)
      # st.success=("Task updated successfully from ::{} to ::{}".format(s_task_name,task))
      st.write(f"Task updated successfully  \nFROM: {s_task_status} {s_task_name} DUE {s_task_due_date}  \nTO: {status} {task} DUE {due_date}")
      link = st.page_link("pages/read_operations.py", label="View All Data", icon="📖")
  
  if st.button(label="View Task JSON"):
    single_task = db.get_task_by_id(id)
    st.write(single_task)
  
else:
  st.write("There are no tasks yet.")
  link = st.page_link("pages/create_operations.py", label="Create Some Tasks", icon="➕")
    
    
  
      # if st.button(label="Update Task"):
      #     single_task = db.get_task_by_id(id)
      #     st.write(f"Update Task: {single_task}")
  
  