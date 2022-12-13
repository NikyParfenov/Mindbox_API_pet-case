# Mindbox API pet-cases


## **Part №1**

There is a Pandas DataFrame with columns [“customer_id”, “product_id”, “timestamp”], which contains data on product views on the site. There is a problem – the views of one customer_id are not split into sessions (appearances on the site). We want to place sessions so that all adjacent views with no more than 3 minutes between them are considered a session. Write a method that will create a session_id column in Pandas DataFrame and put a unique int id in it for each session. Each user can have several sessions. The original DataFrame can be large – up to 100 million rows.


**NOTE**: 
See the file 
```
Sessions_separation.ipynb
```

## **Part №2**

There are products and categories in the SQL database. One product can correspond to many categories, one category can have many products.
Write an HTTP API through which you can get:
- a list of all products with their categories,
- a list of categories with products,
- a list of all pairs "Product Name – Category Name".
If the product has no categories, then it should still be displayed.
If the category has no products, then it should still be displayed.
The project must contain docker-compose.yml file through which you can start the service and check its operation.


**NOTE**:
For run use the next command in terminal and open http://localhost:8000/
```
~/mindbox> docker-compose up
```
It builds postgres with dummy data and django server with required by task lists from DB in web-browser:

![Screenshot from 2022-11-03 12-06-35](https://user-images.githubusercontent.com/63195531/199705954-76219910-e107-4397-8118-a9d85375965d.png)
