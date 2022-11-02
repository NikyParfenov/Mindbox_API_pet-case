from django.db import models
from django.db import connection


class Products(models.Model):
    product = models.TextField(blank=True)
    category = models.TextField(blank=True)

    class Meta:
        db_table = 'mindbox_app'
        managed = False

    def get_full(self):
        with connection.cursor() as cursor:
            cursor.execute(
                """
                select product, category
                from mindbox_app;
                """
            )
            full_dataset = cursor.fetchall()

        return full_dataset

    def products_agg(self):
        with connection.cursor() as cursor:
            cursor.execute(
                """
                select product, array_agg(category)
                from mindbox_app
                group by product;
                """
            )
            products_all = cursor.fetchall()

        return products_all

    def categories_agg(self):
        with connection.cursor() as cursor:
            cursor.execute(
                """
                select category, array_agg(product)
                from mindbox_app
                group by category;
                """
            )
            categories_all = cursor.fetchall()

        return categories_all
