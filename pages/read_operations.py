import streamlit as st
import pandas as pd
import db_fxns as db
import plotly.express as px
st.subheader("View Items")

tasks = db.read_data()
tasks_df = pd.DataFrame(
  tasks,
  columns=[
    "Task ID", 
    "Task Name", 
    "Task Status", 
    "Task Due Date"]
)

# fig = px.line(last_df, y=var_plotting, x =last_df.index)


############# #Status Counts
st.caption("Status Counts:")
task_count = tasks_df[
  'Task Status'
].value_counts().to_frame()  #.drop_duplicates()'
task_count = task_count.reset_index() #adds an index col
st.write(task_count)

############### #PLOT FOR THE FUTURE:
# plot = px.pie(task_count,
#               names= ['Status','Count'],
#               values=['Task Status','count'])
# st.plotly_chart(plot)

############# #More Data
with st.expander(label="View All Data"):

  viewoption = st.selectbox(
    label="Select a format to view",
    options=["JSON", "DataFrame"], 
    index=1)
  

  
  if viewoption == "JSON":
    st.json(tasks)
  elif viewoption == "DataFrame":
    st.dataframe(tasks_df, width=600)


########### #Buttons for Update and Delete
col1, col2, col3 = st.columns(3)

with col1:
    link_update = st.page_link("pages/update_operations.py", label="Update Existing Tasks", icon="✏️")

with col2:
    link = st.page_link("pages/create_operations.py", label="Create More Tasks", icon="➕")

with col3:
    link_delete = st.page_link("pages/delete_operations.py", label="Delete Some Tasks", icon="🗑️")

#with st.expander(label="View Data by ID"):
with st.expander(label="View Not Started Tasks"):
  tasks = db.read_not_started()
  tasks_df = pd.DataFrame(
    tasks,
    columns=[
      # "Task ID", 
      "Task Name", 
      "Task Status"]
  )
  st.write(tasks_df)

