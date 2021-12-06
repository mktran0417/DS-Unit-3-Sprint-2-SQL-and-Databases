create_titanic = '''
CREATE TABLE IF NOT EXISTS titanic_method_one(
    ID SERIAL PRIMARY KEY,
    SURVIVED INT NOT NULL,
    PCLASS INT NOT NULL,
    NAME VARCHAR NOT NULL,
    SEX VARCHAR NOT NULL,
    AGE INT NOT NULL,
    Siblings_Spouses_Aboard INT NOT NULL,
    Parents_Children_Aboard INT NOT NULL,
    Fare FLOAT NOT NULL
);
'''
