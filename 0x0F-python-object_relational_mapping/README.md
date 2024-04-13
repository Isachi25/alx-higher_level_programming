### 0x0F. Python - Object-relational mapping

Concepts;
Why Python programming is awesome
How to connect to a MySQL database from a Python script
How to SELECT rows in a MySQL table from a Python script
How to INSERT rows in a MySQL table from a Python script
What ORM means
How to map a Python Class to a MySQL table
How to create a Python Virtual Environment

overview;
Python's Object-Relational Mapping (ORM) is a programming technique that facilitates the interaction between a relational database and Python objects. It abstracts away the complexities of SQL queries, allowing developers to work with database records using Python syntax and objects.
Key components of Python ORM:
* Models: ORM frameworks define models as Python classes that represent database tables. Each model class typically corresponds to a table in the database, with attributes mapping to columns.
* Mappings: ORM frameworks establish mappings between Python objects and database tables. This mapping defines how data is transferred between the application and the database.
* Queries: ORM frameworks provide methods and query language for retrieving, inserting, updating, and deleting records in the database. Developers can use Python syntax or a domain-specific language provided by the ORM framework to interact with the database.
* Relationships: ORM frameworks support defining relationships between different models, such as one-to-one, one-to-many, and many-to-many relationships. These relationships simplify querying and navigating related data.

Popular Python ORM frameworks include:
* SQLAlchemy: A powerful and flexible ORM library that supports multiple database backends and provides high-level abstractions for database operations.
* Django ORM: Built into the Django web framework, Django ORM offers a straightforward and easy-to-use interface for database operations. It automatically generates models based on database schema and provides a rich set of features for querying and managing data.
* Peewee: A lightweight ORM library with a simple and expressive syntax. Peewee is designed to be easy to learn and use, making it suitable for small to medium-sized projects.

Python ORM simplifies database interactions, improves code maintainability, and enhances productivity by allowing developers to focus on business logic rather than database management tasks. However, developers should be mindful of ORM performance overhead and ensure proper optimization for high-performance applications.
