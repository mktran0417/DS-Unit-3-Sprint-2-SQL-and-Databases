'''
Michael Tran
11/5/21

Using `sqlite3`, connect to the given `northwind_small.sqlite3` database.
Answer the following questions (each is from a single table) and then
save each query under the following variable name:

- `expensive_items`: What are the ten most expensive items (per unit price) in
    the database? Please return all columns in the table, not just the price
    and name but all columns.
- `avg_hire_age`: What is the average age of an employee at the time of their
    hiring? (Hint: a lot of arithmetic works with dates.)
- (*Stretch*) `avg_age_by_city`: How does the average age
    of employee at hire vary by city?
'''
# ten most expensive with cote de blaye at the top
expensive_items = '''
                    SELECT * FROM Product
                    ORDER BY UnitPrice DESC
                    LIMIT 10;
                  '''

# avg age = 37.22
avg_hire_age = '''SELECT AVG(HireDate - BirthDate) FROM Employee;'''

# avg date kirk = 29, london = 32.5, redmond = 56, seattle = 40, tacoma = 40
avg_age_by_city = '''
                    SELECT City, AVG(HireDate - BirthDate) FROM Employee
                     GROUP BY City;
                  '''

# ten most expensive with cote de blaye at the top and Aux joyeux
# ecclésiastiques as the company name
ten_most_expensive = '''
                        SELECT Product.ProductName, UnitPrice,
                        Supplier.CompanyName FROM Product
                        INNER JOIN Supplier
                        ON Supplier.Id = Product.SupplierId
                        ORDER BY UnitPrice DESC
                        LIMIT 10;
                     '''

# Count = 13
largest_category = '''
                        SELECT CategoryName, COUNT(Product.Id) FROM Category
                        INNER JOIN Product
                        ON Category.Id = Product.CategoryId
                        GROUP BY CategoryName
                        ORDER BY COUNT(*) DESC
                        LIMIT 1;
                    '''


# Count = 10
most_territories = '''
                        SELECT EmployeeId, Employee.FirstName,
                        Employee.LastName, COUNT(*)
                        FROM EmployeeTerritory
                        INNER JOIN Employee
                        ON Employee.Id = EmployeeTerritory.EmployeeId
                        INNER JOIN Territory
                        On Territory.Id = EmployeeTerritory.TerritoryId
                        GROUP BY EmployeeId
                        ORDER BY COUNT(*) DESC
                        LIMIT 1;
                    '''
