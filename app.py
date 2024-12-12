import streamlit as st
import pandas as pd
import db_fxns as db



# import create_operations as create
# import read_operations as read
# import update_operations as update
# import delete_operations as delete


db.create_table()

def home_page():
  st.title("Welcome to the To-Do App")




#Streamlit Homepage
home = st.Page(home_page,title="Home",icon="🏠")
create_page = st.Page("pages/create_operations.py", title="Create", icon="➕")
read_page = st.Page("pages/read_operations.py", title="Read", icon="📖")
update_page = st.Page("pages/update_operations.py", title="Update", icon="✏️")
delete_page = st.Page("pages/delete_operations.py", title="Delete", icon="🗑️")


#:material/home:

#Navigation
menu = [create_page, read_page, update_page, delete_page]
pg = st.navigation({
  "Home" : [home],
  "CRUD Operations" : menu
})

pg.run()

# pg = st.navigation([st.Page("page_1.py"), st.Page(page_2)])
# pg.run()















# def main():
#   st.title("The ToDo App Built w/ Streamlit") 
#   st.caption("This is a simple ToDo app built with Streamlit")
  
#   menu = ["Create", "Read", "Update", "Delete"]
#   choice = None
  
#   create_btn = st.sidebar.button('Create')
#   read_btn = st.sidebar.button('Read')
#   update_btn = st.sidebar.button('Update')
#   delete_btn = st.sidebar.button('Delete')
  
#   if create_btn:
#       choice = 'Create'
#       st.caption(choice)
#       create.screen()
    
#   elif read_btn:
#       choice = 'Read'
#       st.write(choice)
#       read.screen()

#   elif update_btn:
#       choice = 'Update'
#       st.write(choice)
#       update.screen()
    
#   elif delete_btn:
#       choice = 'Delete'
#       st.write(choice)
#       delete.screen()
    
    
# if __name__ == "__main__":
#   main()
