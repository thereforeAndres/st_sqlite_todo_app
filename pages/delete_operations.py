import streamlit as st
import db_fxns as db
import pandas as pd



st.subheader("Delete Items")



tasks = db.read_data()
tasks_df = pd.DataFrame(
  tasks,
  columns=[
    "Task ID", 
    "Task Name", 
    "Task Status", 
    "Task Due Date"]
)


with st.expander(label="Data prior to deletion"):
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

    if id:
      selected_task = db.get_task_by_id(id)
      s_task_name = selected_task[0][1]
      s_task_status = selected_task[0][2]
      s_task_due_date = selected_task[0][3]


      ######################## #View JSON by ID

      if st.button(label="View Task JSON"):
        single_task = db.get_task_by_id(id)
        st.write(single_task)


      
      ######################## #Update by ID
      st.warning(f"🚨WARNING🚨  \nThe following button will delete the task: {task_selected} from the database  \nTHIS ACTION CANNOT BE UNDONE")
      if st.button(label="Delete Task"):
        db.delete_data(id)
        st.warning(f"Task deleted successfully  \n{s_task_status} {s_task_name} DUE {s_task_due_date} has been deleted")
        link = st.page_link("pages/read_operations.py", label="View Updated Data", icon="📖")


    ################## Bulk Delete Funcitonality:
    with st.expander(label="Bulk Delete Tasks"):
        selected_for_deletion = []
        for task_name in db.read_tasknames():
            if st.checkbox(task_name[0]):
                task_data = db.get_tasks_by_name(task_name[0])
                selected_for_deletion.append(task_data)
                ##### Just some sanity checks if needeD:
                # st.write("Selected Tasks:", selected_for_deletion)
                # for task in selected_for_deletion:
                #   st.write("Selected Task:", task[0])
                #   st.write("Selected Task ID:", task[0][0])

        # it seems this wasn't needed either?
        # if st.session_state.get("review_btn", True):
        #   st.session_state.disabled = False
        # elif st.session_state.get("review_btn", False):
        #   st.session_state.disabled = True
      
        if st.button(label="Review Selected Tasks for Deletion",key="review_btn"):
          st.warning("This will delete the following tasks:")
          for task in selected_for_deletion:
              task_id = task[0][0]
              st.write(task[0],task[0][0])

        if st.button(label="Confirm Deletion of Selected Tasks", key="confirm_btn", disabled=not st.session_state.get("review_btn", True)): #doesn't seem to matter if it is t/f here
            if selected_for_deletion:
                for task in selected_for_deletion:
                    task_id = task[0][0]
                    db.delete_data(task_id)
                    st.write("Deleted Task ID:", task_id)
                    st.write("Deleted Task:", task[0])
                link = st.page_link("pages/read_operations.py", label="View Updated Data", icon="📖")
            else:
                st.write("No tasks selected for deletion.")
else:
    st.write("There are no tasks yet.")
    link = st.page_link("pages/create_operations.py", label="Create Some Tasks", icon="➕")