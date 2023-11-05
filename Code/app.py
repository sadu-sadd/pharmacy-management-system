import streamlit as st
from streamlit_option_menu import option_menu

from read import read
from create import create
from delete import delete
from update import update


def main():
    st.set_page_config(page_title="Pharmacy", page_icon="💊", layout="centered", initial_sidebar_state="auto", menu_items=None)
    st.title("PHARMACY MANAGEMENT SYSTEM")
    with st.sidebar:
        choice = option_menu("Main Menu", ['CREATE', 'READ', 'UPDATE', 'DELETE'], icons=['write','read','update','delete'], menu_icon="cast", default_index=0)


    if choice == "CREATE":
        st.subheader("Add Entries To Tables")
        create()

    elif choice == "READ":
        st.subheader("Read Entries From Tables")
        read()

    elif choice == "UPDATE":
        st.subheader("Update Entries In Tables")
        update()

    elif choice == "DELETE":
        st.subheader("Delete Entries In Tables")
        delete()

    else:
        st.subheader("About")


if __name__ == '__main__':
    main()
