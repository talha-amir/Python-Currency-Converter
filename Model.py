import sqlite3
from sqlite3 import Error
import requests
import cryptography
from datetime import date as d
from urllib.request import urlopen
from itertools import permutations 
class Connection:
    @staticmethod
    def check():
        """static method can be called without object
        Conection.check()
         """
        try:
            urlopen("https://www.google.com")
        except Exception:
            return False
        else:
            return True
            

class Database:

    def __init__(self):
        self.connect = sqlite3.connect("rates.db")
        self.cursor = self.connect.cursor()
        # For dropping the table
        query = """drop table if exists rates"""
        self.cursor.execute(query)
        query = """create table  if not exists codes        
        (
        name text not null,
        code text not null)
        
        """
        try:
            self.cursor.execute(query)
        except Error as p:
            print(p)
            
        else:
            self.connect.commit()
      

              
    def search_codes(self,name):
        """
        used for wild card searching
        """
        query = """select * from codes where name like ?
        """
        self.cursor.execute(query, (f"{name}%", ))
        data = self.cursor.fetchall()
        data.sort(key=lambda x: x[1])
        temp = [i[1] for i in data]
        temp = sorted(set(temp))
        for i in range(len(data)):
            temp_lst = list(data[i])
            temp_lst.insert(0,str(i+1))
            temp_lst[1],temp_lst[2] = temp_lst[2],temp_lst[1]
            temp_lst = tuple(temp_lst)
            data[i] = temp_lst

        return data
        # for i in data:
        #     print(i)

    def set_codes(self,data):
        """
        used for inserting currency codes in the database 
        only used once for filling database
        """
        query = """insert into codes(name,code) values(?,?)"""
        for i in data:
            self.cursor.execute(query,(i[1],i[0]))
            self.connect.commit()
    
    def get_codes(self):
        """
        used for getting currency codes from the data base
        will be called every time for displating the data
        
        """
        query = """select * from codes"""
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        for i in range(len(data)):
            temp_lst = list(data[i])
            temp_lst.insert(0,str(i+1))
            temp_lst[1],temp_lst[2] = temp_lst[2],temp_lst[1]
            temp_lst = tuple(temp_lst)
            data[i] = temp_lst

        return data
        # for i in data:
        #     print(i)

    def __del__(self):
        self.connect.close()




class API:

    def __init__(self):
        
        self.__apikey = "ff0ff8b8fa69d4fa532b"
        self.db = Database()

    def convert_currecy(self,from1,to,amount):
        """
        This method returns the converted amount
        """
        query = f"{from1}_{to}&compact=ultra&apiKey="
        url = f'https://free.currconv.com/api/v7/convert?q={query}{self.__apikey}'
        req = requests.get(url)

        rate = dict(req.json())[f"{from1}_{to}"]

        amount = float(rate)*float(amount)
        amount =  eval("{0:.3f}".format(amount))
        return amount




if __name__ == "__main__":
    obj = Database()
    obj.get_codes()
    # obj.fill_all()
    
    # obj = Database()
    # obj.search_codes("P")
    # print(Connection.check())
    # total =  ob.get_rate("USD","PKR",10)
    # print(total)
    # obj.get_codes()
    # objec = API()
    # objec.set_rate("USD","PKR",5)
    # objec.set_currencies()
    # objec.get_all()

    