import pandas as pd
import streamlit as st

from database import view_table
from database import view_eids,delete_emp_data
from database import view_cids,delete_cust_data
from database import view_sids,delete_sup_data
from database import view_mids,delete_med_data
from database import view_sa_ids,delete_sale_data
from database import view_sa_i_ids,delete_sale_items_data
from database import view_pids,delete_pur_data


def delete():
    list_of_tables=['EMPLOYEE','CUSTOMER','SUPPLIERS','MEDICINES','SALES','SALES ITEMS','PURCHASE']
    choice=st.selectbox("Select Table to DELETE Data", list_of_tables)

    if choice == "EMPLOYEE":
        result = view_table('employee')
        df = pd.DataFrame(result, columns=['Employee ID','E Fname','E Lname','Birth Date','E Age','E Sex','E Type','E Join Date','E Salary','E Phone No','E Mail','E Address'])
        with st.expander("Current data in Employee Table"):
            st.dataframe(df)
        
        E_ids = [i[0] for i in view_eids()]
        selected_eid = st.selectbox("Select Employee ID", E_ids)
        st.warning("Do you want to Delete Employee with ID:: {} ".format(selected_eid))
        if st.button("Delete Employee"):
            delete_emp_data(selected_eid)
            st.success("Employee has been deleted successfully")
        
        new_result = view_table('employee')
        df2 = pd.DataFrame(new_result, columns=['Employee ID','E Fname','E Lname','Birth Date','E Age','E Sex','E Type','E Join Date','E Salary','E Phone No','E Mail','E Address'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif choice == "CUSTOMER":
        result = view_table('customer')
        df = pd.DataFrame(result, columns=['Customer ID','C Fname','C Lname','C Age','C Sex','C Phone No','C Mail'])
        with st.expander("Current data in Customer Table"):
            st.dataframe(df)
        
        C_ids = [i[0] for i in view_cids()]
        selected_cid = st.selectbox("Select Customer ID", C_ids)
        st.warning("Do you want to Delete Customer with ID:: {} ".format(selected_cid))
        if st.button("Delete Customer"):
            delete_cust_data(selected_cid)
            st.success("Customer has been deleted successfully")
        
        new_result = view_table('customer')
        df2 = pd.DataFrame(new_result, columns=['Customer ID','C Fname','C Lname','C Age','C Sex','C Phone No','C Mail'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif choice == "SUPPLIERS":
        result = view_table('suppliers')
        df = pd.DataFrame(result, columns=['Supplier ID','Sup Name','Sup Address','Sup Phone No','Sup Mail'])
        with st.expander("Current data in Suppliers Table"):
            st.dataframe(df)
        
        S_ids = [i[0] for i in view_sids()]
        selected_sid = st.selectbox("Select Supplier ID", S_ids)
        st.warning("Do you want to Delete Supplier with ID:: {} ".format(selected_sid))
        if st.button("Delete Supplier"):
            delete_sup_data(selected_sid)
            st.success("Supplier has been deleted successfully")
        
        new_result = view_table('suppliers')
        df2 = pd.DataFrame(new_result, columns=['Supplier ID','Sup Name','Sup Address','Sup Phone No','Sup Mail'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif choice == "MEDICINES":
        result = view_table('meds')
        df = pd.DataFrame(result, columns=['Medicine ID','Med Name','Med Quantity','Category','Med Price','Location Rack'])
        with st.expander("Current data in Medicines Table"):
            st.dataframe(df)
        
        M_ids = [i[0] for i in view_mids()]
        selected_mid = st.selectbox("Select Medicine ID", M_ids)
        st.warning("Do you want to Delete Medicine with ID:: {} ".format(selected_mid))
        if st.button("Delete Medicine"):
            delete_med_data(selected_mid)
            st.success("Medicine has been deleted successfully")
        
        new_result = view_table('meds')
        df2 = pd.DataFrame(new_result, columns=['Medicine ID','Med Name','Med Quantity','Category','Med Price','Location Rack'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif choice == "SALES":
        result = view_table('sales')
        df = pd.DataFrame(result, columns=['Sale ID','C ID','S Date','S Time','Total Amount','E ID'])
        with st.expander("Current data in Sales Table"):
            st.dataframe(df)
        
        Sa_ids = [i[0] for i in view_sa_ids()]
        selected_sa_id = st.selectbox("Select Sale ID", Sa_ids)
        st.warning("Do you want to Delete Sales with ID:: {} ".format(selected_sa_id))
        if st.button("Delete Sale"):
            delete_sale_data(selected_sa_id)
            st.success("Sale has been deleted successfully")
        
        new_result = view_table('sales')
        df2 = pd.DataFrame(new_result, columns=['Sale ID','C ID','S Date','S Time','Total Amount','E ID'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif choice == "SALES ITEMS":
        result = view_table('sales_items')
        df = pd.DataFrame(result, columns=['Sale ID','Med ID','Sale Quantity','Total Price'])
        with st.expander("Current data in Sales Items Table"):
            st.dataframe(df)
        
        Sa_i_ids = [i[0] for i in view_sa_i_ids()]
        selected_sa_i_id = st.selectbox("Select Sale ID", Sa_i_ids)
        st.warning("Do you want to Delete Sales Items with Sale ID:: {} ".format(selected_sa_i_id))
        if st.button("Delete Sale Items"):
            delete_sale_items_data(selected_sa_i_id)
            st.success("Sale Items has been deleted successfully")
        
        new_result = view_table('sales_items')
        df2 = pd.DataFrame(new_result, columns=['Sale ID','Med ID','Sale Quantity','Total Price'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif choice == "PURCHASE":
        result = view_table('purchase')
        df = pd.DataFrame(result, columns=['Purchase ID','Sup ID','Med ID','P Quantity','P Cost','P Date','MFG','EXP'])
        with st.expander("Current data in Purchase Table"):
            st.dataframe(df)
        
        P_ids = [i[0] for i in view_pids()]
        selected_pid = st.selectbox("Select Purchase ID", P_ids)
        st.warning("Do you want to Delete Purchase with ID:: {} ".format(selected_pid))
        if st.button("Delete Purchase"):
            delete_pur_data(selected_pid)
            st.success("Purchase has been deleted successfully")
        
        new_result = view_table('purchase')
        df2 = pd.DataFrame(new_result, columns=['Purchase ID','Sup ID','Med ID','P Quantity','P Cost','P Date','MFG','EXP'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    else:
        st.subheader("Select Table")
