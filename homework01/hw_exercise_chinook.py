import sqlite3



def get_number_of_artists_in_chinook(cursor):
    """Count artists"""
    query = """SELECT COUNT(ArtistId) FROM Artist;"""
    print query
    return cursor.execute(query)


def get_most_expensive_invoice_script(cursor):
    """What order (Invoice) was the most expensive?"""
    query = """SELECT MAX(Invoice.Total), * FROM Invoice;"""
    print query
    return cursor.execute(query)


def get_cheapest_invoice_script(cursor):
    """What order (Invoice) was the cheapest?"""
    query = """SELECT MIN(Invoice.Total), * FROM Invoice;"""
    print query
    return cursor.execute(query)


def get_city_with_most_orders_script(cursor):
    """Which city (BillingCity) has the most orders?"""
    query = """SELECT Invoice.BillingCity, COUNT(Invoice.BillingCity) AS MostOrders 
                FROM Invoice GROUP BY Invoice.BillingCity ORDER BY MostOrders DESC LIMIT 1;"""
    print query
    return cursor.execute(query)


def get_count_aac_tracks_script(cursor):
    """Calculate (or count) how many tracks have this MediaType: Protected AAC audio file."""
    query = """SELECT COUNT(Track.MediaTypeId) FROM Track INNER JOIN MediaType 
                ON Track.MediaTypeId=MediaType.MediaTypeId WHERE MediaType.Name='Protected AAC audio file' LIMIT 1;"""
    print query
    return cursor.execute(query)


def get_artist_most_albums_script(cursor):
    """Find out what Artist has the most albums?"""
    query = """SELECT Artist.Name, COUNT(Artist.Name) AS AlbumNum FROM Artist INNER JOIN Album 
                ON Album.ArtistId=Artist.ArtistId GROUP BY Album.ArtistId ORDER BY AlbumNum DESC LIMIT 1;"""
    print query
    return cursor.execute(query)


def get_genre_most_tracks_script(cursor):
    """What genre has the most tracks?"""
    query = """SELECT Genre.Name, COUNT(Genre.Name) AS TrackCount FROM Genre INNER JOIN Track
                ON Track.GenreId=Genre.GenreId GROUP BY Track.GenreId ORDER BY TrackCount DESC;"""
    print query
    return cursor.execute(query)


def get_customer_most_money_spent_script(cursor):
    """Which customer spent the most money so far?"""
    query = """SELECT Customer.FirstName, Customer.LastName, SUM(Invoice.Total) AS InvoiceSum 
                FROM Customer INNER JOIN Invoice ON Invoice.CustomerId=Customer.CustomerId 
                GROUP BY Invoice.CustomerId ORDER BY InvoiceSum DESC LIMIT 1;"""
    print query
    return cursor.execute(query)


def get_songs_bought_with_each_order_script(cursor):
    """What songs were bought with each order?"""
    query = """SELECT Invoice.InvoiceId, Track.Name FROM Invoice INNER JOIN InvoiceLine 
                ON InvoiceLine.InvoiceId=Invoice.InvoiceId INNER JOIN Track ON InvoiceLine.TrackId=Track.TrackId;"""
    print query
    return cursor.execute(query)


if __name__ == '__main__':
    conn = sqlite3.connect("Chinook_Sqlite.sqlite")
    cursor = conn.cursor()

    for r in get_number_of_artists_in_chinook(cursor):
        print(r)

    for r in get_most_expensive_invoice_script(cursor):
        print(r)

    for r in get_cheapest_invoice_script(cursor):
        print(r)

    for r in get_city_with_most_orders_script(cursor):
        print(r)

    for r in get_count_aac_tracks_script(cursor):
        print(r)

    for r in get_artist_most_albums_script(cursor):
        print(r)

    for r in get_genre_most_tracks_script(cursor):
        print(r)

    for r in get_customer_most_money_spent_script(cursor):
        print(r)

    for r in get_songs_bought_with_each_order_script(cursor):
        print(r)