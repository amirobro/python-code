from typing import List, Any, Dict

import mysql.connector


def save_person(name, family, national_code):
    # connect
    db = mysql.connector.connect(host='localhost', user='root', password='root123', port=3306, database="persondb")
    cursor = db.cursor()
    cursor.execute("insert into person_tbl(NAME,FAMILY,NATIONAL_CODE) values(%s,%s,%s)", (name, family, national_code))
    db.commit()
    cursor.close()
    db.close()


def edit_person(id, name, family, national_code):
    db = mysql.connector.connect(host='localhost', user='root', password='root123', port=3306, database="persondb")
    cursor = db.cursor()
    cursor.execute('update person_tbl set NAME = %s,FAMILY = %s,NATIONAL_CODE = %s where id= %s',
                   [name, family, national_code, id])
    db.commit()
    cursor.close()
    db.close()


def remove_person(id):
    db = mysql.connector.connect(host='localhost', user='root', password='root123', port=3306, database='persondb')
    cursor = db.cursor()
    cursor.execute("delete from person_tbl where id=%s", [id])
    db.commit()
    cursor.close()
    db.close()


def find_all_person():
    db = mysql.connector.connect(host='localhost', user='root', password='root123', port=3306, database="persondb")
    cursor = db.cursor()
    cursor.execute("select * from person_tbl ")
    person_list = cursor.fetchall()
    cursor.close()
    db.close()
    return person_list


def find_by_family_person(family):
    db = mysql.connector.connect(host='localhost', user='root', password='root123', port=3306, database="persondb")
    cursor = db.cursor()
    cursor.execute("select * from person_tbl where family=%s", [family])
    person_list: cursor.fetchall()
    cursor.close()
    db.close()
    return person_list
