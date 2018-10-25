import sqlite3
import os


def create_posts_table():
    query = """     CREATE TABLE post
                        (                       
                            post_id integer primary key autoincrement,
                            post_title text,
                            post_content text, 
                            username text
                        )
                    """
    return query


def create_members_table():
    query = """     CREATE TABLE member
                        (                       
                            username integer primary key autoincrement,
                            first_name text, 
                            last_name text, 
                            country text,
                            gender text,
                            author_permission text
                        )
                    """
    return query


def create_comments_table():
    query = """     CREATE TABLE comment
                            (                       
                                comment_text text,
                                username text,
                                post_id text
                            )
                        """
    return query


if __name__ == '__main__':
    database_name = "newdb.sqlite"
    conn = sqlite3.connect(database_name)
    # conn = sqlite3.connect(":memory:") --> if db should only be run in memory
    cursor = conn.cursor()

    query = create_posts_table()
    print query
    cursor.execute(query)

    query = create_members_table()
    print query
    cursor.execute(query)

    query = create_comments_table()
    print query
    cursor.execute(query)

    conn.commit()
    # os.remove(database_name) --> if db should be removed
