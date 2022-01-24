import sqlite3
from sqlite3 import Error
import os
import pandas as pd

def print_columns(df):
    """
    Prints all column labels to a string
    :param df: object
        a pandas dataframe object
    :return all_columns: str
        A string of column labels (including data types) for use in SQL queries
    """
    all_columns=''
    for i in range(len(df.columns)):
        if df.dtypes[i]==int:
            a= """ INT, """#number type
        elif df.dtypes[i]=='O':
            a= """ TEXT, """#string type
        elif df.dtypes[i]==float:
            a= """REAL, """

        all_columns+=str(df.columns[i]) + " " + a + ' '
    all_columns=all_columns[:-3]
    return all_columns

def execute_string(df):
    """
    Defines an SQL query to create a table within the database from the pandas dataframe

    :param df: object
        a pandas dataframe object
    :return execute_string:
        The full SQL command
    """
    #for i in range(len(df.dtypes)):
    execute_string="""CREATE TABLE IF NOT EXISTS exoplanet_archive (%s)""" % print_columns(df)
    return execute_string

    # c.execute("""
    #             CREATE TABLE IF NOT EXISTS exoplanet_archive (%s)""" % print_columns(df))
    # conn.commit()

def connect_to_db(filename):
    """
    Creates a connection to a database
    :param:
        filename: string
            the name of the database
    :return:
        conn: object
            an sqlite3 database connection
        c:
            an sqlite3 cursor
    """
    conn = sqlite3.connect(db_path+filename)
    c = conn.cursor()
    return conn, c

def create_table(conn, create_table_sql):  # create_table_sql = execute_string(db)
    """ create a table from the create_table_sql statement
    :param:
        conn: obj
            sqlite3 connection object
    :param
        create_table_sql:
            a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        # print any errors and explicitly note function failure
        print(e)

def data_entry():
    """
    Insert the data into the the database
    :return:

    """
    def list_data():
        data=[]
        for index, row in df.iterrows():
            row_temp=[]
            for i in range(len(df.columns)):
                row_temp.append(row[i])
            data.append(row_temp)
        return data
    data=list_data()
    for i in range(len(data)):
        c.execute("INSERT INTO exoplanet_archive VALUES(%s)" %str(data[i])[1:-1])

    conn.commit()
    return

def show_all():
    c.execute('SELECT * from exoplanet_archive')
    c.fetchall()

# Read the CSV File to be imported into an .db database
filename='cumulative_2022.01.20_12.32.06.csv'
df=pd.read_csv(filename, comment='#')
df.fillna('',inplace=True) # Ensure that "NaN" values are properly processed

# Establish the path to the to-be-created database
db_path=str(os.path.abspath(os.getcwd()) + "/db/")

# Define the connection and cursor
conn, c = connect_to_db('exoplanet_archive.db')

# Create the table within the database
create_table(conn, execute_string(df))

# Enter the data from the exoplanet archive into the newly created table
data_entry()

# Finally, display the entire table to verify that the import was successful with the following query
c.execute('SELECT * from exoplanet_archive')
print(c.fetchall())

# To delete the table (only if it exists), uncomment the following line
# c.execute("DROP TABLE IF EXISTS exoplanet_archive ")

# SQL queries to insert new record into the database.
# c.execute('''INSERT INTO exoplanet_archive(Column_1, Column_2, ..., Column_N)
#                                         VALUES ('Value_1', 'Value_2', ..., Value_n)''')
# c.commit()

# note that c.commit() is necessary to write the queries to the table