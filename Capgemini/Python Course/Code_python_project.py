# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 16:31:37 2021

@author: anshu
"""

# HR Management system

# build a database - sqlite
# employees

# =============================================================================
# E_ID
# Name
# city
# salary
# email
# age
# gender
# ===============================================
# =============================================================================
# build a module
# which can be used to create an object - hr
# =============================================================================
# An hr should have following capabilities - 
# 1. add a new employee
# 2. remove an existing employee based on EID
# 3. fetch data of all employees
# 4. fetch data of specific employee based on EID
# 5. promote an employee
# 
# 
# =============================================================================

#[17:26] Maguluru, Dhanalakshmi
import sqlite3
# write code to create a database and table
# with eid as a primary key



conn = sqlite3.connect("Employeedatabase.db")

query = "create table if not exists employees(E_ID numeric primary key,Name text,city text,salary numeric,email text,age numeric,gender text)"
conn.execute(query)

class HR:
    def check_employee(self,eid):
        # your code goes here
        # this should check whether the employee exists or not
        # return True or false
        data = conn.execute(f"select * from employees where E_ID={eid}")
        if len(data.fetchall()) > 0:
            return True
        else:
            return False

    def add_employee(self):
        # use input function to get eid
        # use check_employee to check whether employee exists or not
        # if not existing, ask other details using input function,
        # add employee to the database
        empId = input("Enter Employee ID to Add: ")
        chkEmp = self.check_employee(empId)
        if chkEmp == False:
            empDet = input("Enter Employee Name,city,salary,email,age and Gender to Add: ").split(",")
            query = "insert into employees values(?,?,?,?,?,?,?);"
            conn.execute(query,(empId,empDet[0],empDet[1],empDet[2],empDet[3],empDet[4],empDet[5]))
        else:
            print("Employee already exists")
            
            
    def show_all(self):
        # show data of all employees
        data = conn.execute("select * from employees;")
        for d in data:
            print(d)

    def get_employee(self):
        # ask for eid, check whether exists or not
        # if exists, show details
        empId = input("Enter Employee ID to fetch details: ")
        chkEmp = self.check_employee(empId)
        if chkEmp:
            data = conn.execute(f"select * from employees where E_ID={empId}")
            for d in data:
                print(d)
        else:
            print("Employee does not exist")
hr = HR()
hr.add_employee()
hr.get_employee()
hr.show_all()
hr.check_employee(123)
    
