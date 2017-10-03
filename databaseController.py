import os, sys, sqlite3


def createDb():
    connection = sqlite3.connect("./tempData.db")
    print("Opened database successfully")

    cursor = connection.cursor()
    cursor.execute("CREATE TABLE temp(date TEXT, temperature FLOAT, humidity FLOAT)")
    print("Table created successfully")

    connection.commit()
    connection.close()


if __name__ == "__main__":
    createDb()
