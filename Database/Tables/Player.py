import sqlite3
import json

class DataBase():
    def __init__(self):
        with sqlite3.connect("player.db") as self.connection:
            self.cursor = self.connection.cursor()
            try:
                self.cursor.execute("CREATE TABLE main (token text, lowID integer, trophies integer, data json)")
            except sqlite3.OperationalError:
                pass


    def createPlayerAccount(self, token, lowID, trophies, data):
        check = "SELECT * FROM main WHERE token = ?"
        value = [token]
        self.cursor.execute(check, value)

        all = self.cursor.fetchall()

        if len(all) == 0:
            sql = "INSERT INTO main (token, lowID, trophies, data) VALUES (?, ?, ?, ?)"
            values = (token, lowID, trophies, data)
            self.cursor.execute(sql, values)
        else:
            print(f"Account with token {token} already exists!")
            return
        self.connection.commit()


    def getPlayerAccount(self, token):
        sql = "SELECT * from main where token=?"
        value = [token]
        self.cursor.execute(sql, value)
        return self.cursor.fetchall()


    def updatePlayerAccount(self, var, value, token):
        sql = f"UPDATE main SET {var} = ? WHERE token = ?"
        values = (value, token)
        self.cursor.execute(sql , values)
        self.connection.commit()


    def deletePlayerAccount(self, token):
        sql = "DELETE FROM main WHERE token = ?"
        value = [token]
        self.cursor.execute(sql, value)
        self.connection.commit()


    def orderPlayersByTrophies(self):
        sql = "SELECT * FROM main ORDER BY trophies"
        self.cursor.execute(sql)
        return self.cursor.fetchall()


