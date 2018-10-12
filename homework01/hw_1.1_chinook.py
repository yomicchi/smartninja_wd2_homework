import sqlite3


def get_names_in_artist_table(cursor):
    """Name from the table Artist (for all the database entries)"""
    query = """SELECT Name FROM Artist;"""
    print query
    return cursor.execute(query)


def get_invoices_where_billingcountry_is_germany(cursor):
    """Invoice where BillingCountry is Germany"""
    query = """SELECT * FROM Invoice WHERE Invoice.BillingCountry='Germany';"""
    print query
    return cursor.execute(query)


def get_count_of_albums(cursor):
    """Count how many albums are in the database"""
    query = """SELECT COUNT(AlbumId) FROM Album;"""
    print query
    return cursor.execute(query)


def get_number_of_customers_in_france(cursor):
    """How many customers are from France?"""
    query = """SELECT COUNT(*) FROM Customer WHERE Customer.Country='France';"""
    print query
    return cursor.execute(query)


if __name__ == '__main__':
    conn = sqlite3.connect("Chinook_Sqlite.sqlite")
    cursor = conn.cursor()

    for r in get_names_in_artist_table(cursor):
        print(r)

    for r in get_invoices_where_billingcountry_is_germany(cursor):
        print(r)

    for r in get_count_of_albums(cursor):
        print(r)

    for r in get_number_of_customers_in_france(cursor):
        print(r)
