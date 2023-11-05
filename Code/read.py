import pandas as pd
import streamlit as st
from database import view_table


def read():
    list_of_tables=['EMPLOYEE','CUSTOMER','SUPPLIERS','MEDICINES','SALES','SALES ITEMS','PURCHASE']
    choice=st.selectbox("Select Table to View Data", list_of_tables)

    if choice == "EMPLOYEE":
        st.text("Displaying Employee table")
        res=view_table('employee')
        df = pd.DataFrame(res, columns=['Employee ID','E Fname','E Lname','Birth Date','E Age','E Sex','E Type','E Join Date','E Salary','E Phone No','E Mail','E Address'])
        st.dataframe(df)
        st.success("Successfully fetched Employee table")

    elif choice == "CUSTOMER":
        st.text("Displaying Customer table")
        res=view_table('customer')
        df = pd.DataFrame(res, columns=['Customer ID','C Fname','C Lname','C Age','C Sex','C Phone No','C Mail'])
        st.dataframe(df)
        st.success("Successfully fetched Customer table")

    elif choice == "SUPPLIERS":
        st.text("Displaying Suppliers table")
        res=view_table('suppliers')
        df = pd.DataFrame(res, columns=['Supplier ID','Sup Name','Sup Address','Sup Phone No','Sup Mail'])
        st.dataframe(df)
        st.success("Successfully fetched Suppliers table")

    elif choice == "MEDICINES":
        st.text("Displaying Medicines table")
        res=view_table('meds')
        df = pd.DataFrame(res, columns=['Medicine ID','Med Name','Med Quantity','Category','Med Price','Location Rack'])
        st.dataframe(df)
        st.success("Successfully fetched Medicines table")

    elif choice == "SALES":
        st.text("Displaying Sales table")
        res=view_table('sales')
        df = pd.DataFrame(res, columns=['Sale ID','C ID','S Date','S Time','Total Amount','E ID'])
        st.dataframe(df)
        st.success("Successfully fetched Sales table")

    elif choice == "SALES ITEMS":
        st.text("Displaying Sales Items table")
        res=view_table('sales_items')
        df = pd.DataFrame(res, columns=['Sale ID','Med ID','Sale Quantity','Total Price'])
        st.dataframe(df)
        st.success("Successfully fetched Sales Items table")

    elif choice == "PURCHASE":
        st.text("Displaying Purchase table")
        res=view_table('purchase')
        df = pd.DataFrame(res, columns=['Purchase ID','Sup ID','Med ID','P Quantity','P Cost','P Date','MFG','EXP'])
        st.dataframe(df)
        st.success("Successfully fetched Purchase table")

    else:
        st.subheader("Select Tables")
