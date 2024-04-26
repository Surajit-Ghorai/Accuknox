"""reads data from csv and stores it in database"""
import pandas as pd

from data_store import (
    connect_to_database,
    create_table,
    insert_data,
    retrieve_data,
    close_connection,
)

def get_user_data(file_path):
    # reads data from csv file 
    df = pd.read_csv(file_path)
    return df


def store_data2(df):
    """store data in sqlite database directly from pandas dataframe"""
    conn = connect_to_database("users.db")
    df.to_sql("Users", conn, if_exists="replace", index=False)
    close_connection(conn)


def get_data():
    """retrieve data from sqlite database"""
    conn = connect_to_database("users.db")
    rows = retrieve_data(conn, "Users")
    for row in rows:
        print(row)

    close_connection(conn)


if __name__ == "__main__":
    file_path = "./data/user_info.csv"
    df = get_user_data(file_path)

    # approach 1 to store csv
    conn = connect_to_database("users.db")
    create_table(conn)

    for index, row in df.iterrows():
        insert_data(conn, (row['name'], row['email']))
    
    close_connection(conn)

    # approach 2 to store csv
    #store_data2(df)

    get_data()
