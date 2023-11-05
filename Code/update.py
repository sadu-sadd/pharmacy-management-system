import pandas as pd
import streamlit as st

from database import view_table
from database import view_eids,get_emp,edit_emp_data
from database import view_cids,get_cust,edit_cust_data
from database import view_sids,get_sup,edit_sup_data
from database import view_mids,get_med,edit_med_data
from database import view_sa_ids,get_sales,edit_sales_data
from database import view_sa_i_ids,get_sales_items,edit_sales_items_data
from database import view_pids,get_pur,edit_pur_data


def update():
    list_of_tables=['EMPLOYEE','CUSTOMER','SUPPLIERS','MEDICINES','SALES','SALES ITEMS','PURCHASE']
    choice=st.selectbox("Select Table to Update Data", list_of_tables)

    if choice == "EMPLOYEE":
        result = view_table('employee')
        df = pd.DataFrame(result, columns=['Employee ID','E Fname','E Lname','Birth Date','E Age','E Sex','E Type','E Join Date','E Salary','E Phone No','E Mail','E Address'])
        with st.expander("Current data in Employee Table"):
            st.dataframe(df)

        E_ids = [i[0] for i in view_eids()]
        selected_eid = st.selectbox("Select Employee ID", E_ids)
        selected_result = get_emp(selected_eid)
        if selected_result:
            e_id = selected_result[0][0]
            e_fname = selected_result[0][1]
            e_lname = selected_result[0][2]
            bdate = selected_result[0][3]
            e_age = selected_result[0][4]
            e_sex = selected_result[0][5]
            e_type = selected_result[0][6]
            e_jdate = selected_result[0][7]
            e_sal = selected_result[0][8]
            e_phno = selected_result[0][9]
            e_mail = selected_result[0][10]
            e_addr = selected_result[0][11]

        ecol1,ecol2,ecol3 = st.columns(3)
        with ecol1:
            new_e_id = st.text_input("Employee ID",e_id)
            new_bdate = st.text_input("Birth Date",bdate)
            new_e_type = st.text_input("Employee Type",e_type)
            new_e_phno = st.text_input("Phone Number",e_phno)
        
        with ecol2:
            new_e_fname = st.text_input("Employee First Name",e_fname)
            new_e_age = st.text_input("Age",e_age)
            new_e_jdate = st.text_input("Join Date",e_jdate)
            new_e_mail = st.text_input("Mail",e_mail)

        with ecol3:
            new_e_lname = st.text_input("Employee Last Name",e_lname)
            new_e_sex = st.text_input("Sex",e_sex)
            new_e_sal = st.text_input("Salary",e_sal)
            new_e_addr = st.text_input("Address",e_addr)
        
        if st.button("Update Employee"):
            edit_emp_data(new_e_id, new_e_fname, new_e_lname, new_bdate, new_e_age, new_e_sex, new_e_type, new_e_jdate, new_e_sal, new_e_phno, new_e_mail, new_e_addr,e_id, e_fname, e_lname, bdate, e_age, e_sex, e_type, e_jdate, e_sal, e_phno, e_mail, e_addr)
            st.success("Successfully Updated Employee with ID : {} ".format(new_e_id))

        result2 = view_table('employee')
        df2 = pd.DataFrame(result2, columns=['Employee ID','E Fname','E Lname','Birth Date','E Age','E Sex','E Type','E Join Date','E Salary','E Phone No','E Mail','E Address'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif choice == "CUSTOMER":
        result = view_table('customer')
        df = pd.DataFrame(result, columns=['Customer ID','C Fname','C Lname','C Age','C Sex','C Phone No','C Mail'])
        with st.expander("Current data in Customer Table"):
            st.dataframe(df)

        C_ids = [i[0] for i in view_cids()]
        selected_cid = st.selectbox("Select Customer ID", C_ids)
        selected_result = get_cust(selected_cid)
        if selected_result:
            c_id = selected_result[0][0]
            c_fname = selected_result[0][1]
            c_lname = selected_result[0][2]
            c_age = selected_result[0][3]
            c_sex = selected_result[0][4]
            c_phno = selected_result[0][5]
            c_mail = selected_result[0][6]

        ccol1,ccol2,ccol3 = st.columns(3)
        with ccol1:
            new_c_id = st.text_input("Customer ID",c_id)
            new_c_age = st.text_input("Age",c_age)
            new_c_mail = st.text_input("Mail",c_mail)

        with ccol2:
            new_c_fname = st.text_input("Customer First Name",c_fname)
            new_c_sex = st.text_input("Sex",c_sex)

        with ccol3:
            new_c_lname = st.text_input("Customer Last Name",c_lname)
            new_c_phno = st.text_input("Phone Number",c_phno)
        
        if st.button("Update Customer"):
            edit_cust_data(new_c_id, new_c_fname, new_c_lname, new_c_age, new_c_sex, new_c_phno, new_c_mail,c_id, c_fname, c_lname, c_age, c_sex, c_phno, c_mail)
            st.success("Successfully Updated Customer with ID : {} ".format(new_c_id))

        result2 = view_table('customer')
        df2 = pd.DataFrame(result2, columns=['Customer ID','C Fname','C Lname','C Age','C Sex','C Phone No','C Mail'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif choice == "SUPPLIERS":
        result = view_table('suppliers')
        df = pd.DataFrame(result, columns=['Supplier ID','Sup Name','Sup Address','Sup Phone No','Sup Mail'])
        with st.expander("Current data in Suppliers Table"):
            st.dataframe(df)

        S_ids = [i[0] for i in view_sids()]
        selected_sid = st.selectbox("Select Supplier ID", S_ids)
        selected_result = get_sup(selected_sid)
        if selected_result:
            sup_id = selected_result[0][0]
            sup_name = selected_result[0][1]
            sup_addr = selected_result[0][2]
            sup_phno = selected_result[0][3]
            sup_mail = selected_result[0][4]

        scol1,scol2 = st.columns(2)
        with scol1:
            new_sup_id = st.text_input("Supplier ID",sup_id)
            new_sup_addr = st.text_input("Supplier Address",sup_addr)
            new_sup_mail = st.text_input("Supplier Mail",sup_mail)

        with scol2:
            new_sup_name = st.text_input("Supplier Name",sup_name)
            new_sup_phno = st.text_input("Supplier Phone",sup_phno)
        
        if st.button("Update Supplier"):
            edit_sup_data(new_sup_id, new_sup_name, new_sup_addr, new_sup_phno, new_sup_mail,sup_id, sup_name, sup_addr, sup_phno, sup_mail)
            st.success("Successfully Updated Supplier with ID : {} ".format(new_sup_id))

        result2 = view_table('suppliers')
        df2 = pd.DataFrame(result2, columns=['Supplier ID','Sup Name','Sup Address','Sup Phone No','Sup Mail'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif choice == "MEDICINES":
        result = view_table('meds')
        df = pd.DataFrame(result, columns=['Medicine ID','Med Name','Med Quantity','Category','Med Price','Location Rack'])
        with st.expander("Current data in Medicine Table"):
            st.dataframe(df)

        M_ids = [i[0] for i in view_mids()]
        selected_mid = st.selectbox("Select Medicine ID", M_ids)
        selected_result = get_med(selected_mid)
        if selected_result:
            med_id = selected_result[0][0]
            med_name = selected_result[0][1]
            med_qty = selected_result[0][2]
            category = selected_result[0][3]
            med_price = selected_result[0][4]
            location_rack = selected_result[0][5]

        mcol1,mcol2 = st.columns(2)
        with mcol1:
            new_med_id = st.text_input("Medicine ID",med_id)
            new_med_qty = st.text_input("Quantity",med_qty)
            new_med_price = st.text_input("Price",med_price)

        with mcol2:
            new_med_name = st.text_input("Medicine Name",med_name)
            new_category = st.text_input("Category",category)
            new_location_rack = st.text_input("Location Rack",location_rack)

        if st.button("Update Medicine"):
            edit_med_data(new_med_id, new_med_name, new_med_qty, new_category, new_med_price, new_location_rack,med_id, med_name, med_qty, category, med_price, location_rack)
            st.success("Successfully Updated Medicine with ID : {} ".format(new_med_id))

        result2 = view_table('meds')
        df2 = pd.DataFrame(result2, columns=['Medicine ID','Med Name','Med Quantity','Category','Med Price','Location Rack'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif choice == "SALES":
        result = view_table('sales')
        df = pd.DataFrame(result, columns=['Sale ID','C ID','S Date','S Time','Total Amount','E ID'])
        with st.expander("Current data in Sales Table"):
            st.dataframe(df)

        Sa_ids = [i[0] for i in view_sa_ids()]
        selected_sa_id = st.selectbox("Select Sales ID", Sa_ids)
        selected_result = get_sales(selected_sa_id)
        if selected_result:
            sale_id = selected_result[0][0]
            c_id = selected_result[0][1]
            s_date = selected_result[0][2]
            s_time = selected_result[0][3]
            total_amt = selected_result[0][4]
            e_id = selected_result[0][5]

        scol1,scol2 = st.columns(2)
        with scol1:
            new_sale_id = st.text_input("Sale ID",sale_id)
            new_s_date = st.text_input("Sale Date",s_date)
            new_total_amt = st.text_input("Total Amount",total_amt)

        with scol2:
            new_c_id = st.text_input("Customer ID",c_id)
            new_s_time = st.text_input("Sale Time",s_time)
            new_e_id = st.text_input("Employee ID",e_id)

        if st.button("Update Sales"):
            edit_sales_data(new_sale_id, new_c_id, new_s_date, new_s_time, new_total_amt, new_e_id,sale_id, c_id, s_date, s_time, total_amt, e_id)
            st.success("Successfully Updated Sales with ID : {} ".format(new_sale_id))

        result2 = view_table('sales')
        df2 = pd.DataFrame(result2, columns=['Sale ID','C ID','S Date','S Time','Total Amount','E ID'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif choice == "SALES ITEMS":
        result = view_table('sales_items')
        df = pd.DataFrame(result, columns=['Sale ID','Med ID','Sale Quantity','Total Price'])
        with st.expander("Current data in Sales Items Table"):
            st.dataframe(df)

        Sa_i_ids = [i[0] for i in view_sa_i_ids()]
        selected_sa_i_id = st.selectbox("Select Sales ID", Sa_i_ids)
        selected_result = get_sales_items(selected_sa_i_id)
        if selected_result:
            sale_id = selected_result[0][0]
            med_id = selected_result[0][1]
            sale_qty = selected_result[0][2]
            tot_price = selected_result[0][3]

        sicol1,sicol2 = st.columns(2)
        with sicol1:
            new_sale_id = st.text_input("Sale ID",sale_id)
            new_sale_qty = st.text_input("Sale Quantity",sale_qty)

        with sicol2:
            new_med_id = st.text_input("Medicine ID",med_id)
            new_tot_price = st.text_input("Total Price",tot_price)

        if st.button("Update Sales Items"):
            edit_sales_items_data(new_sale_id, new_med_id, new_sale_qty, new_tot_price,sale_id, med_id, sale_qty, tot_price)
            st.success("Successfully Updated Sales Items with ID : {} ".format(new_sale_id))

        result2 = view_table('sales_items')
        df2 = pd.DataFrame(result2, columns=['Sale ID','Med ID','Sale Quantity','Total Price'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif choice == "PURCHASE":
        result = view_table('purchase')
        df = pd.DataFrame(result, columns=['Purchase ID','Sup ID','Med ID','P Quantity','P Cost','P Date','MFG','EXP'])
        with st.expander("Current data in Purchase Table"):
            st.dataframe(df)

        P_ids = [i[0] for i in view_pids()]
        selected_p_id = st.selectbox("Select Sales ID", P_ids)
        selected_result = get_pur(selected_p_id)
        if selected_result:
            p_id = selected_result[0][0]
            sup_id = selected_result[0][1]
            med_id = selected_result[0][2]
            p_qty = selected_result[0][3]
            p_cost = selected_result[0][4]
            pur_date = selected_result[0][5]
            mfg_date = selected_result[0][6]
            exp_date = selected_result[0][7]

        pcol1,pcol2 = st.columns(2)
        with pcol1:
            new_p_id = st.text_input("Purchase ID",p_id)
            new_med_id = st.text_input("Medicine ID",med_id)
            new_p_cost = st.text_input("Cost",p_cost)
            new_mfg_date = st.text_input("Mfg Date",mfg_date)

        with pcol2:
            new_sup_id = st.text_input("Supplier ID",sup_id)
            new_p_qty = st.text_input("Quantity",p_qty)
            new_pur_date = st.text_input("Purchase Date",pur_date)
            new_exp_date = st.text_input("Expiry Date",exp_date)

        if st.button("Update Purchase"):
            edit_pur_data(new_p_id, new_sup_id, new_med_id, new_p_qty, new_p_cost, new_pur_date, new_mfg_date, new_exp_date,p_id, sup_id, med_id, p_qty, p_cost, pur_date, mfg_date, exp_date)
            st.success("Successfully Updated Purchase with ID : {} ".format(new_p_id))

        result2 = view_table('purchase')
        df2 = pd.DataFrame(result2, columns=['Purchase ID','Sup ID','Med ID','P Quantity','P Cost','P Date','MFG','EXP'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    else:
        st.subheader("Select Table")


