from pprint import pprint
from random import randint
import psycopg2


def generate_product():
    product_id = randint(0, 50)
    product = f'product_{product_id}' if product_id > 0 else ''
    return product


def generate_category():
    category_id = randint(0, 10)
    category = f'category_{category_id}' if category_id > 0 else ''
    return category


if __name__ == "__main__":
    conn = psycopg2.connect(
        host='db',
        port='5432',
        database='mindbox_app',
        user='admin',
        password='admin'
    )
    cursor = conn.cursor()
    cursor.execute(
        """
        DROP TABLE IF EXISTS mindbox_app;
        CREATE TABLE mindbox_app (
            id int not null,
            product text not null,
            category text not null
        );
        """
    )

    for i in range(1, 101):
        cursor.execute(
            f"INSERT INTO mindbox_app (id, product, category) "
            f"VALUES ('{i}', '{generate_product()}', '{generate_category()}');"
        )

    cursor.execute("SELECT * FROM mindbox_app;")
    sql_data = cursor.fetchall()

    pprint(sql_data)

    conn.commit()
    cursor.close()
    conn.close()
