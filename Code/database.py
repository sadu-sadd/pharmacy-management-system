import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="PES1UG20CS454_PHARMACY"
)
c = mydb.cursor()


# view tables
def view_table(table):
    c.execute('SELECT * FROM {}'.format(table))
    data = c.fetchall()
    return data


#--------------------------------------------------------------------------------------


# add employee data
def add_emp_data(e_id, e_fname, e_lname, bdate, e_age, e_sex, e_type, e_jdate, e_sal, e_phno, e_mail, e_addr):
    c.execute('INSERT INTO employee(e_id, e_fname, e_lname, bdate, e_age, e_sex, e_type, e_jdate, e_sal, e_phno, e_mail, e_addr) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(e_id, e_fname, e_lname, bdate, e_age, e_sex, e_type, e_jdate, e_sal, e_phno, e_mail, e_addr))
    mydb.commit()

# add customer data
def add_cust_data(c_id, c_fname, c_lname, c_age, c_sex, c_phno, c_mail):
    c.execute('INSERT INTO customer(c_id, c_fname, c_lname, c_age, c_sex, c_phno, c_mail) VALUES (%s,%s,%s,%s,%s,%s,%s)',(c_id, c_fname, c_lname, c_age, c_sex, c_phno, c_mail))
    mydb.commit()

# add suppliers data
def add_sup_data(sup_id, sup_name, sup_addr, sup_phno, sup_mail):
    c.execute('INSERT INTO suppliers(sup_id, sup_name, sup_addr, sup_phno, sup_mail) VALUES (%s,%s,%s,%s,%s)',(sup_id, sup_name, sup_addr, sup_phno, sup_mail))
    mydb.commit()

# add meds data
def add_med_data(med_id, med_name, med_qty, category, med_price, location_rack):
    c.execute('INSERT INTO meds(med_id, med_name, med_qty, category, med_price, location_rack) VALUES (%s,%s,%s,%s,%s,%s)',(med_id, med_name, med_qty, category, med_price, location_rack))
    mydb.commit()

# add sales data
def add_sales_data(sale_id, c_id, s_date, s_time, total_amt, e_id):
    c.execute('INSERT INTO sales(sale_id, c_id, s_date, s_time, total_amt, e_id) VALUES (%s,%s,%s,%s,%s,%s)',(sale_id, c_id, s_date, s_time, total_amt, e_id))
    mydb.commit()

# add sales items data
def add_sales_items_data(sale_id, med_id, sale_qty, tot_price):
    c.execute('INSERT INTO sales_items(sale_id, med_id, sale_qty, tot_price) VALUES (%s,%s,%s,%s)',(sale_id, med_id, sale_qty, tot_price))
    mydb.commit()

# add purchase data
def add_pur_data(p_id, sup_id, med_id, p_qty, p_cost, pur_date, mfg_date, exp_date):
    c.execute('INSERT INTO purchase(p_id, sup_id, med_id, p_qty, p_cost, pur_date, mfg_date, exp_date) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',(p_id, sup_id, med_id, p_qty, p_cost, pur_date, mfg_date, exp_date))
    mydb.commit()


#---------------------------------------------------------------------------------------

# view emp details
def get_emp(eid):
    c.execute('SELECT * FROM employee WHERE e_id="{}"'.format(eid))
    data = c.fetchall()
    return data

# update emp
def edit_emp_data(new_e_id, new_e_fname, new_e_lname, new_bdate, new_e_age, new_e_sex, new_e_type, new_e_jdate, new_e_sal, new_e_phno, new_e_mail, new_e_addr,e_id, e_fname, e_lname, bdate, e_age, e_sex, e_type, e_jdate, e_sal, e_phno, e_mail, e_addr):
    c.execute("UPDATE employee SET e_id=%s, e_fname=%s, e_lname=%s, bdate=%s, e_age=%s, e_sex=%s, e_type=%s, e_jdate=%s, e_sal=%s, e_phno=%s, e_mail=%s, e_addr=%s  WHERE e_id=%s and e_fname=%s and e_lname=%s and bdate=%s and e_age=%s and e_sex=%s and e_type=%s and e_jdate=%s and e_sal=%s and e_phno=%s and e_mail=%s and e_addr=%s", (new_e_id, new_e_fname, new_e_lname, new_bdate, new_e_age, new_e_sex, new_e_type, new_e_jdate, new_e_sal, new_e_phno, new_e_mail, new_e_addr,e_id, e_fname, e_lname, bdate, e_age, e_sex, e_type, e_jdate, e_sal, e_phno, e_mail, e_addr))
    mydb.commit()

# view cid details
def get_cust(cid):
    c.execute('SELECT * FROM customer WHERE c_id="{}"'.format(cid))
    data = c.fetchall()
    return data

# update cust
def edit_cust_data(new_c_id, new_c_fname, new_c_lname, new_c_age, new_c_sex, new_c_phno, new_c_mail,c_id, c_fname, c_lname, c_age, c_sex, c_phno, c_mail):
    c.execute("UPDATE customer SET c_id=%s, c_fname=%s, c_lname=%s, c_age=%s, c_sex=%s, c_phno=%s, c_mail=%s WHERE c_id=%s and c_fname=%s and c_lname=%s and c_age=%s and c_sex=%s and c_phno=%s and c_mail=%s", (new_c_id, new_c_fname, new_c_lname, new_c_age, new_c_sex, new_c_phno, new_c_mail,c_id, c_fname, c_lname, c_age, c_sex, c_phno, c_mail))
    mydb.commit()

# view sid details
def get_sup(sid):
    c.execute('SELECT * FROM suppliers WHERE sup_id="{}"'.format(sid))
    data = c.fetchall()
    return data

# update sup
def edit_sup_data(new_sup_id, new_sup_name, new_sup_addr, new_sup_phno, new_sup_mail,sup_id, sup_name, sup_addr, sup_phno, sup_mail):
    c.execute("UPDATE suppliers SET sup_id=%s, sup_name=%s, sup_addr=%s, sup_phno=%s, sup_mail=%s WHERE sup_id=%s and sup_name=%s and sup_addr=%s and sup_phno=%s and sup_mail=%s", (new_sup_id, new_sup_name, new_sup_addr, new_sup_phno, new_sup_mail,sup_id, sup_name, sup_addr, sup_phno, sup_mail))
    mydb.commit()

# view mid details
def get_med(mid):
    c.execute('SELECT * FROM meds WHERE med_id="{}"'.format(mid))
    data = c.fetchall()
    return data

# update meds
def edit_med_data(new_med_id, new_med_name, new_med_qty, new_category, new_med_price, new_location_rack,med_id, med_name, med_qty, category, med_price, location_rack):
    c.execute("UPDATE meds SET med_id=%s, med_name=%s, med_qty=%s, category=%s, med_price=%s, location_rack=%s WHERE med_id=%s and med_name=%s and med_qty=%s and category=%s and med_price=%s and location_rack=%s", (new_med_id, new_med_name, new_med_qty, new_category, new_med_price, new_location_rack,med_id, med_name, med_qty, category, med_price, location_rack))
    mydb.commit()

# view sale details
def get_sales(sa_id):
    c.execute('SELECT * FROM sales WHERE sale_id="{}"'.format(sa_id))
    data = c.fetchall()
    return data

# update sales
def edit_sales_data(new_sale_id, new_c_id, new_s_date, new_s_time, new_total_amt, new_e_id,sale_id, c_id, s_date, s_time, total_amt, e_id):
    c.execute("UPDATE sales SET sale_id=%s, c_id=%s, s_date=%s, s_time=%s, total_amt=%s, e_id=%s WHERE sale_id=%s and c_id=%s and s_date=%s and s_time=%s and total_amt=%s and e_id=%s", (new_sale_id, new_c_id, new_s_date, new_s_time, new_total_amt, new_e_id,sale_id, c_id, s_date, s_time, total_amt, e_id))
    mydb.commit()

# view sale item details
def get_sales_items(sa_i_id):
    c.execute('SELECT * FROM sales_items WHERE sale_id="{}"'.format(sa_i_id))
    data = c.fetchall()
    return data

# update sales
def edit_sales_items_data(new_sale_id, new_med_id, new_sale_qty, new_tot_price,sale_id, med_id, sale_qty, tot_price):
    c.execute("UPDATE sales_items SET sale_id=%s, med_id=%s, sale_qty=%s, tot_price=%s WHERE sale_id=%s and med_id=%s and sale_qty=%s and tot_price=%s", (new_sale_id, new_med_id, new_sale_qty, new_tot_price,sale_id, med_id, sale_qty, tot_price))
    mydb.commit()

# view pur details
def get_pur(pid):
    c.execute('SELECT * FROM purchase WHERE p_id="{}"'.format(pid))
    data = c.fetchall()
    return data

# update sales
def edit_pur_data(new_p_id, new_sup_id, new_med_id, new_p_qty, new_p_cost, new_pur_date, new_mfg_date, new_exp_date,p_id, sup_id, med_id, p_qty, p_cost, pur_date, mfg_date, exp_date):
    c.execute("UPDATE purchase SET p_id=%s, sup_id=%s, med_id=%s, p_qty=%s, p_cost=%s, pur_date=%s, mfg_date=%s, exp_date=%s WHERE p_id=%s and sup_id=%s and med_id=%s and p_qty=%s and p_cost=%s and pur_date=%s and mfg_date=%s and exp_date=%s", (new_p_id, new_sup_id, new_med_id, new_p_qty, new_p_cost, new_pur_date, new_mfg_date, new_exp_date,p_id, sup_id, med_id, p_qty, p_cost, pur_date, mfg_date, exp_date))
    mydb.commit()


#---------------------------------------------------------------------------------------


# view only e_id
def view_eids():
    c.execute('SELECT e_id FROM employee')
    data = c.fetchall()
    return data

# delete employee
def delete_emp_data(eid):
    c.execute('DELETE FROM employee WHERE e_id="{}"'.format(eid))
    mydb.commit()

# view only c_id
def view_cids():
    c.execute('SELECT c_id FROM customer')
    data = c.fetchall()
    return data

# delete customer
def delete_cust_data(cid):
    c.execute('DELETE FROM customer WHERE c_id="{}"'.format(cid))
    mydb.commit()

# view only s_id
def view_sids():
    c.execute('SELECT sup_id FROM suppliers')
    data = c.fetchall()
    return data

# delete suppliers
def delete_sup_data(sid):
    c.execute('DELETE FROM suppliers WHERE sup_id="{}"'.format(sid))
    mydb.commit()

# view only m_id
def view_mids():
    c.execute('SELECT med_id FROM meds')
    data = c.fetchall()
    return data

# delete meds
def delete_med_data(mid):
    c.execute('DELETE FROM meds WHERE med_id="{}"'.format(mid))
    mydb.commit()

# view only sale_id
def view_sa_ids():
    c.execute('SELECT sale_id FROM sales')
    data = c.fetchall()
    return data

# delete sales
def delete_sale_data(sa_id):
    c.execute('DELETE FROM sales WHERE sale_id="{}"'.format(sa_id))
    mydb.commit()

# view only sale_id
def view_sa_i_ids():
    c.execute('SELECT sale_id FROM sales_items')
    data = c.fetchall()
    return data

# delete sales items
def delete_sale_items_data(sa_i_id):
    c.execute('DELETE FROM sales_items WHERE sale_id="{}"'.format(sa_i_id))
    mydb.commit()

# view only pids
def view_pids():
    c.execute('SELECT p_id FROM purchase')
    data = c.fetchall()
    return data

# delete purchase
def delete_pur_data(pid):
    c.execute('DELETE FROM purchase WHERE p_id="{}"'.format(pid))
    mydb.commit()


#---------------------------------------------------------------------------------------
