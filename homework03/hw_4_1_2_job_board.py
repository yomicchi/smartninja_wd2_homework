import sqlite3
import os


def create_users_table():
    query = """     CREATE TABLE user
                        (                       
                            member_id integer primary key autoincrement,
                            first_name text,
                            last_name text,
                            username text
                        )
                    """
    return query


def create_jobs_table():
    query = """     CREATE TABLE job
                        (                       
                            job_id integer primary key autoincrement,
                            title text,
                            tags text,
                            location_id integer,
                            description text
                        )
                    """
    return query


def create_locations_table():
    query = """     CREATE TABLE location
                        (                       
                            location_id integer primary key autoincrement,
                            zip integer,
                            country text,
                            state text,
                            city text
                        )
                    """
    return query


def create_memberjobs_table():
    query = """     CREATE TABLE member_job
                        (                       
                            applied text,
                            member_id integer,
                            job_id integer
                        )
                    """
    return query


def create_companies_table():
    query = """     CREATE TABLE company
                        (                       
                            company_id integer primary key autoincrement,
                            company_name text,
                            company_address text
                        )
                    """
    return query


def create_contact_table():
    query = """     CREATE TABLE contact
                        (                       
                            contact_id integer primary key autoincrement,
                            first_name text,
                            last_name text,
                            email text,
                            gender text
                        )
                    """
    return query


def create_jobcontacts_table():
    query = """     CREATE TABLE job_contact
                        (                       
                            job_id integer,
                            contact_id text
                        )
                    """
    return query


if __name__ == '__main__':
    database_name = "newdb.sqlite"
    conn = sqlite3.connect(database_name)
    # conn = sqlite3.connect(":memory:") --> if db should only be run in memory
    cursor = conn.cursor()

    query = create_members_table()
    print query
    cursor.execute(query)

    query = create_jobs_table()
    print query
    cursor.execute(query)

    query = create_locations_table()
    print query
    cursor.execute(query)

    query = create_memberjobs_table()
    print query
    cursor.execute(query)

    query = create_companies_table()
    print query
    cursor.execute(query)

    query = create_contact_table()
    print query
    cursor.execute(query)

    query = create_jobcontacts_table()
    print query
    cursor.execute(query)

    conn.commit()
    # os.remove(database_name) --> if db should be removed
