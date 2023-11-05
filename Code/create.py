import streamlit as st
from database import add_emp_data, add_cust_data, add_sup_data, add_med_data, add_sales_data, add_sales_items_data, add_pur_data


def create():
    list_of_tables=['EMPLOYEE','CUSTOMER','SUPPLIERS','MEDICINES','SALES','SALES ITEMS','PURCHASE']
    choice=st.selectbox("Select Table to INSERT Data", list_of_tables)

    if choice == "EMPLOYEE":
        st.text("Fill the details of Employee")
        ecol1,ecol2,ecol3 = st.columns(3)
        with ecol1:
            e_id = st.text_input("Employee ID")
            bdate = st.date_input("Birth Date")
            e_type = st.selectbox("Employee Type", ["Admin","Manager","Pharmacist"])
            e_phno = st.text_input("Phone Number")
        
        with ecol2:
            e_fname = st.text_input("Employee First Name")
            e_age = st.text_input("Age")
            e_jdate = st.date_input("Join Date")
            e_mail = st.text_input("Mail")

        with ecol3:
            e_lname = st.text_input("Employee Last Name")
            e_sex = st.selectbox("Sex", ["Male","Female"])
            e_sal = st.text_input("Salary")
            e_addr = st.text_input("Address")
        
        if st.button("Add Employee"):
            add_emp_data(e_id, e_fname, e_lname, bdate, e_age, e_sex, e_type, e_jdate, e_sal, e_phno, e_mail, e_addr)
            st.success("Successfully added Employee : {} {}".format(e_fname,e_lname))


    elif choice == "CUSTOMER":
        st.text("Fill the details of Customer")
        ccol1,ccol2,ccol3 = st.columns(3)
        with ccol1:
            c_id = st.text_input("Customer ID")
            c_age = st.text_input("Age")
            c_mail = st.text_input("Mail")

        with ccol2:
            c_fname = st.text_input("Customer First Name")
            c_sex = st.selectbox("Sex", ["Male","Female"])

        with ccol3:
            c_lname = st.text_input("Customer Last Name")
            c_phno = st.text_input("Phone Number")
        
        if st.button("Add Customer"):
            add_cust_data(c_id, c_fname, c_lname, c_age, c_sex, c_phno, c_mail)
            st.success("Successfully added Customer : {} {}".format(c_fname,c_lname))

    
    elif choice == "SUPPLIERS":
        st.text("Fill the details of Suppliers")
        scol1,scol2 = st.columns(2)
        with scol1:
            sup_id = st.text_input("Supplier ID")
            sup_addr = st.text_input("Supplier Address")
            sup_mail = st.text_input("Supplier Mail")

        with scol2:
            sup_name = st.text_input("Supplier Name")
            sup_phno = st.text_input("Supplier Phone")
        
        if st.button("Add Supplier"):
            add_sup_data(sup_id, sup_name, sup_addr, sup_phno, sup_mail)
            st.success("Successfully added Supplier : {}".format(sup_name))


    elif choice == "MEDICINES":
        st.text("Fill the details of Medicines")
        mcol1,mcol2 = st.columns(2)
        with mcol1:
            med_id = st.text_input("Medicine ID")
            med_qty = st.text_input("Quantity")
            med_price = st.text_input("Price")

        with mcol2:
            med_name = st.text_input("Medicine Name")
            category = st.selectbox("Category", ["Tablet","Capsule","Syrup"])
            location_rack = st.selectbox("Location Rack", ["rack 1","rack 2","rack 3","rack 4","rack 5","rack 6","rack 7","rack 8","rack 9","rack 10"])

        if st.button("Add Medicine"):
            add_med_data(med_id, med_name, med_qty, category, med_price, location_rack)
            st.success("Successfully added Medicine : {}".format(med_name))


    elif choice == "SALES":
        st.text("Fill the details of Sales")
        scol1,scol2 = st.columns(2)
        with scol1:
            sale_id = st.text_input("Sale ID")
            s_date = st.date_input("Sale Date")
            total_amt = st.text_input("Total Amount")

        with scol2:
            c_id = st.text_input("Customer ID")
            s_time = st.time_input("Sale Time")
            e_id = st.text_input("Employee ID")

        if st.button("Add Sales"):
            add_sales_data(sale_id, c_id, s_date, s_time, total_amt, e_id)
            st.success("Successfully added Sales with ID : {}".format(sale_id))


    elif choice == "SALES ITEMS":
        st.text("Fill the details of Sales Items")
        sicol1,sicol2 = st.columns(2)
        with sicol1:
            sale_id = st.text_input("Sale ID")
            sale_qty = st.text_input("Sale Quantity")

        with sicol2:
            med_id = st.text_input("Medicine ID")
            tot_price = st.text_input("Total Price")

        if st.button("Add Sales Items"):
            add_sales_items_data(sale_id, med_id, sale_qty, tot_price)
            st.success("Successfully added Sales Items with Sales ID : {}".format(sale_id))


    elif choice == "PURCHASE":
        st.text("Fill the details of Purchase")
        pcol1,pcol2 = st.columns(2)
        with pcol1:
            p_id = st.text_input("Purchase ID")
            med_id = st.text_input("Medicine ID")
            p_cost = st.text_input("Cost")
            mfg_date = st.date_input("Mfg Date")

        with pcol2:
            sup_id = st.text_input("Supplier ID")
            p_qty = st.text_input("Quantity")
            pur_date = st.date_input("Purchase Date")
            exp_date = st.date_input("Expiry Date")

        if st.button("Add Purchase"):
            add_pur_data(p_id, sup_id, med_id, p_qty, p_cost, pur_date, mfg_date, exp_date)
            st.success("Successfully added Purchase with ID : {}".format(p_id))

    else:
        st.subheader("Select Table")
