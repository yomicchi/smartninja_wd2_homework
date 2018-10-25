import sqlite3
import os

def create_members_table():
    query = """     CREATE TABLE member
                        (                       
                            member_id integer primary key autoincrement,
                            first_name text,
                            last_name text,
                            username text
                        )
                    """
    return query


def create_movies_table():
    query = """     CREATE TABLE movie
                        (                       
                            movie_id integer primary key autoincrement,
                            title text,
                            genre text,
                            studio_id integer
                        )
                    """
    return query


def create_membermovies_table():
    query = """     CREATE TABLE member_movie
                        (                       
                            seen text,
                            member_id integer,
                            movie_id integer
                        )
                    """
    return query


def create_filmstudios_table():
    query = """     CREATE TABLE filmstudio
                        (                       
                            studio_id integer primary key autoincrement,
                            studio_name text,
                            studio_address text
                        )
                    """
    return query


def create_actors_table():
    query = """     CREATE TABLE actor
                        (                       
                            actor_id integer primary key autoincrement,
                            first_name text,
                            last_name text,
                            gender text,
                            country text
                        )
                    """
    return query


def create_directors_table():
    query = """     CREATE TABLE director
                        (                       
                            director_id integer primary key autoincrement,
                            first_name text,
                            last_name text,
                            gender text,
                            country text
                        )
                    """
    return query


def create_movieactors_table():
    query = """     CREATE TABLE movie_actor
                        (                       
                            movie_id integer,
                            actor_id text
                        )
                    """
    return query


def create_moviedirectors_table():
    query = """     CREATE TABLE movie_director
                        (                       
                            movie_id integer,
                            director_id text
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

    query = create_movies_table()
    print query
    cursor.execute(query)

    query = create_membermovies_table()
    cursor.execute(query)

    query = create_filmstudios_table()
    print query
    cursor.execute(query)

    query = create_actors_table()
    print query
    cursor.execute(query)

    query = create_directors_table()
    print query
    cursor.execute(query)

    query = create_movieactors_table()
    print query
    cursor.execute(query)

    query = create_moviedirectors_table()
    print query
    cursor.execute(query)

    conn.commit()
    # os.remove(database_name) --> if db should be removed
