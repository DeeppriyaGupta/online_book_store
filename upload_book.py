import psycopg2
from psycopg2 import sql

# Replace [YOUR-PASSWORD] with your actual password
connection_params = {
    'user': 'postgres',
    'password': '8raKYTFh.xXm$-5',
    'host': 'db.zchtrhpejhzjzmclvkel.supabase.co',
    'port': 5432,
    'database': 'postgres'
}

# Sample book data
books_data =[
  {
    "book_name": "Sapiens: A Brief History of Humankind",
    "book_description": "A captivating exploration of human history.",
    "book_author": "Yuval Noah Harari",
    "book_image": "https://images1.penguinrandomhouse.com/cover/9780593133552",
    "rating": 4.5
  },
  {
    "book_name": "The Great Gatsby",
    "book_description": "A classic novel depicting the Roaring Twenties.",
    "book_author": "F. Scott Fitzgerald",
    "book_image": "https://images1.penguinrandomhouse.com/cover/9780743273565",
    "rating": 4.2
  },
  {
    "book_name": "To Kill a Mockingbird",
    "book_description": "A powerful story addressing racial injustice.",
    "book_author": "Harper Lee",
    "book_image": "https://images1.penguinrandomhouse.com/cover/9780061120084",
    "rating": 4.8
  },
  {
    "book_name": "The Catcher in the Rye",
    "book_description": "A coming-of-age novel with a unique narrative.",
    "book_author": "J.D. Salinger",
    "book_image": "https://images1.penguinrandomhouse.com/cover/9780241950425",
    "rating": 4.0
  },
  {
    "book_name": "1984",
    "book_description": "A dystopian masterpiece warning of totalitarianism.",
    "book_author": "George Orwell",
    "book_image": "https://images1.penguinrandomhouse.com/cover/9780451524935",
    "rating": 4.6
  },
  {
    "book_name": "The Hobbit",
    "book_description": "An adventurous journey in a fantasy world.",
    "book_author": "J.R.R. Tolkien",
    "book_image": "https://images1.penguinrandomhouse.com/cover/9780345534835",
    "rating": 4.7
  },
  {
    "book_name": "The Da Vinci Code",
    "book_description": "A gripping mystery involving art and history.",
    "book_author": "Dan Brown",
    "book_image": "https://images1.penguinrandomhouse.com/cover/9780307474278",
    "rating": 4.1
  },
  {
    "book_name": "Harry Potter and the Sorcerer's Stone",
    "book_description": "The start of a magical journey at Hogwarts.",
    "book_author": "J.K. Rowling",
    "book_image": "https://images1.penguinrandomhouse.com/cover/9780590353427",
    "rating": 4.9
  },
  {
    "book_name": "The Lord of the Rings",
    "book_description": "An epic fantasy trilogy of the One Ring.",
    "book_author": "J.R.R. Tolkien",
    "book_image": "https://images1.penguinrandomhouse.com/cover/9780544003415",
    "rating": 4.8
  },
  {
    "book_name": "The Alchemist",
    "book_description": "A philosophical novel about pursuing dreams.",
    "book_author": "Paulo Coelho",
    "book_image": "https://images1.penguinrandomhouse.com/cover/9780061122415",
    "rating": 4.5
  }
]


def create_books_table(conn):
    with conn.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS minorapi_book (
                book_id SERIAL PRIMARY KEY,
                book_name VARCHAR(255),
                book_description TEXT,
                book_author VARCHAR(255),
                book_image VARCHAR(255),
                rating FLOAT
            )
        """)
        conn.commit()

def insert_books(conn, minorapi_book):
    with conn.cursor() as cursor:
        for book in minorapi_book:
            insert_query = sql.SQL("""
                INSERT INTO minorapi_book (book_name, book_description, book_author, book_image, rating )
                VALUES (%s, %s, %s, %s, %s)
            """)
            cursor.execute(insert_query, (book["book_name"], book["book_description"], book["book_author"], book["book_image"], book["rating"], ))
        conn.commit()

if __name__ == "__main__":
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(**connection_params)

        # Create the books table if it doesn't exist
        create_books_table(connection)

        # Insert the books data into the table
        insert_books(connection, books_data)

    except psycopg2.Error as e:
        print("Error: Unable to connect or execute queries.")
        print(e)

    finally:
        # Close the database connection
        if connection:
            connection.close()
            print("Connection closed.")