import sqlite3
import os


def create_students_table():
    query = """     CREATE TABLE students
                    (                       
                        student_id integer primary key autoincrement,
                        first_name text, 
                        last_name text, 
                        birthday date,
                        gender text
                    )
                """
    return query


def create_courses_table():
    query = """     CREATE TABLE courses
                    (                       
                        course_id integer primary key autoincrement,
                        course_title text, 
                        location_id integer, 
                        trainer_id integer
                    )
                """
    return query


def create_location_table():
    query = """     CREATE TABLE location
                    (                       
                        location_id integer primary key autoincrement,
                        location_address text, 
                        location_ZIP integer
                    )
                """
    return query


def create_trainer_table():
    query = """     CREATE TABLE trainer
                    (                       
                        trainer_id integer primary key autoincrement,
                        first_name text, 
                        last_name text
                    )
                """
    return query


def create_coursesstudents_table():
    query = """     CREATE TABLE course_students
                    (                       
                        course_students_id integer primary key autoincrement,
                        course_id integer,
                        student_id integer
                    )
                """
    return query


if __name__ == '__main__':
    database_name = "newdb.sqlite"
    conn = sqlite3.connect(database_name)
    # conn = sqlite3.connect(":memory:") --> if db should only be run in memory
    cursor = conn.cursor()

    query = create_students_table()
    print query
    cursor.execute(query)

    query = create_trainer_table()
    print query
    cursor.execute(query)

    query = create_courses_table()
    print query
    cursor.execute(query)

    query = create_coursesstudents_table()
    print query
    cursor.execute(query)

    conn.commit()
    # os.remove(database_name) --> if db should be removed
