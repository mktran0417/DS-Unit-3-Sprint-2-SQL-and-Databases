# Data Science Unit 3 Sprint Challenge 2
**IMPORTANT: Use the same name for files and variables that we use within this markdown** :)

## Databases and SQL

A SQL Query walks into a bar. In one corner of the bar are two tables. The Query
walks up to the tables and asks:

...

*"Mind if I join you?"*

---

In this sprint challenge you will write code and answer questions related to databases, with a focus on SQL but an acknowledgment of the broader ecosystem. You may use any tools and references you wish, but your final code should reflect *your* work and be saved in `.py` files (*not* notebooks), and (along with this file including your written answers) uploaded in the Sprint Challenge Submission in Canvas.

For all your code, you may only import/use the following:
- other modules you write
- `sqlite3` (from the standard library)

As always, make sure to manage your time - get a section/question to "good enough" and then move on to make sure you do everything. You can always revisit and polish at the end if time allows.

This file is Markdown, so it may be helpful to open with VS Code or another tool that allows you to view it nicely rendered.

Good luck!

### Part 1 - Making and populating a Database

Consider the following data:

| s   | x | y |
|-----|---|---|
| 'g' | 3 | 9 |
| 'v' | 5 | 7 |
| 'f' | 8 | 7 |

Using the standard `sqlite3` module:

- Open a connection to a new (blank) database file `demo_data.sqlite3`
- Make a cursor, and execute an appropriate `CREATE TABLE` statement to accept
  the above data (name the table `demo`)
- Write and execute appropriate `INSERT INTO` statements to add the data (as
  shown above) to the database

Make sure to `commit()` so your data is saved! The file size should be non-zero.

Then write the following queries (also with `sqlite3`) to test the demo database and
save them under the following variables names:

- `row_count`: Count how many rows you have - it should be 3!
- `xy_at_least_5`: How many rows are there where both `x` and `y` are at least 5?
- `unique_y`: How many unique values of `y` are there (hint - `COUNT()` can accept a keyword
  `DISTINCT`)?

Your code (to reproduce all above steps) should be saved in `demo_data.py` and
turned in along with the generated SQLite database.

### Part 2 - The Northwind Database

Using `sqlite3`, connect to the given `northwind_small.sqlite3` database.

![Northwind Entity-Relationship Diagram](./northwind_erd.png)

Above is an entity-relationship diagram - a picture summarizing the schema and relationships in the database. Note that it was generated using Microsoft
Access, and some of the specific table/field names are different in the provided data. You can see all the tables available to SQLite as follows:

```python
>>> curs.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY
name;").fetchall()
[('Category',), ('Customer',), ('CustomerCustomerDemo',),
('CustomerDemographic',), ('Employee',), ('EmployeeTerritory',), ('Order',),
('OrderDetail',), ('Product',), ('Region',), ('Shipper',), ('Supplier',),
('Territory',)]
```

*Warning*: unlike the diagram, the tables in SQLite are singular and not plural (do not end in `s`). And you can see the schema (`CREATE TABLE` statement) behind any given table with:
```python
>>> curs.execute('SELECT sql FROM sqlite_master WHERE name="Customer";').fetchall()
[('CREATE TABLE "Customer" \n(\n  "Id" VARCHAR(8000) PRIMARY KEY, \n
"CompanyName" VARCHAR(8000) NULL, \n  "ContactName" VARCHAR(8000) NULL, \n
"ContactTitle" VARCHAR(8000) NULL, \n  "Address" VARCHAR(8000) NULL, \n  "City"
VARCHAR(8000) NULL, \n  "Region" VARCHAR(8000) NULL, \n  "PostalCode"
VARCHAR(8000) NULL, \n  "Country" VARCHAR(8000) NULL, \n  "Phone" VARCHAR(8000)
NULL, \n  "Fax" VARCHAR(8000) NULL \n)',)]
```

In particular note that the *primary* key is `Id`, and not `CustomerId`. On other tables (where it is a *foreign* key) it will be `CustomerId`. Also note - the `Order` table conflicts with the `ORDER` keyword! We'll just avoid that particular table, but it's a good lesson in the danger of keyword conflicts.

Answer the following questions (each is from a single table) and then save each query under the following variable name:

- `expensive_items`: What are the ten most expensive items (per unit price) in the database? Please return all columns in the table, not just the price and name but all columns.
- `avg_hire_age`: What is the average age of an employee at the time of their hiring? (Hint: a
  lot of arithmetic works with dates.)
- (*Stretch*) `avg_age_by_city`: How does the average age of employee at hire vary by city?

Your code (to load and query the data) should be saved in `northwind.py`, and added to the repository. Do your best to answer in purely SQL, but if necessary use Python/other logic to help.

### Part 3 - Sailing the Northwind Seas

You've answered some basic questions from the Northwind database, looking at individual tables - now it's time to put things together, and `JOIN`!

Using `sqlite3` in `northwind.py`, answer the following:

- `ten_most_expensive`: What are the ten most expensive items (per unit price) in the database *and* their suppliers? Please return all columns in the table, not just the price and name but all columns. The supplier should be the last column.
- `largest_category`: What is the largest category (by number of unique products in it)?
- (*Stretch*) `most_territories`: Who's the employee with the most territories? Use `TerritoryId` (not name, region, or other fields) as the unique identifier for territories. You should be sure to include the employee id in the select statement and return all columns.

### Part 4 - Questions (and your Answers)

Answer the following questions, baseline ~3-5 sentences each, as if they were interview screening questions (a form you fill when applying for a job):

- In the Northwind database, what is the type of relationship between the `Employee` and `Territory` tables?
  The relationship between Employee and Territory is a one to many relationship. Employees can have access to multiple territories but not vice versa.
  This can be seen in action when we take the count of most_territories in northwind.py.
- What is a situation where a document store (like MongoDB) is appropriate, and what is a situation where it is not appropriate?
  I believe an example where it would likely be best to not use MongoDB is when it comes to handling banking information. The requisites for the data are very structured and ACID is very much a must for transactions because if things mess up either the bank or the customer is going end up very unhappy. In terms of where its appropiate to use MongoDB I feel like
  it makes a lot of sense to use it in say smaller projects or projects that don't have a lot of structure to their data. An example of this would be a small game. You likely don't need
  the data to be strictly structured.
- What is "NewSQL", and what is it trying to achieve?
  NewSQL is another variant of database management. NOSQL has some issues in the sense that there isn't any consistency or structure in terms of the data. SQL has issues in the sense that it can only scale vertically and has issues working with big data. NewSQL essentially is trying to obtain the best of both worlds between NoSQL and SQL databases and remove these issues.

Provide all the files you wrote (`demo_data.py`, `northwind.py`, `demo_data.sqlite3`), as well as this file with your answers to part 4. You're also encouraged to include the output from your queries as docstring comments, to facilitate grading and feedback. Thanks for your hard work!

If you got this far, check out the [larger Northwind database](https://github.com/jpwhite3/northwind-SQLite3/blob/master/Northwind_large.sqlite.zip) -
your queries should run on it as well, with richer results.
