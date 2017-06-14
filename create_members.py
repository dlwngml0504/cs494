import MySQLdb as mdb
import warnings

con = mdb.connect('localhost', 'root', 'wngml5436');

with con:
    
    cur = con.cursor()
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        cur.execute("CREATE DATABASE IF NOT EXISTS oss")
    cur.execute("use oss")

    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        cur.execute("DROP TABLE IF EXISTS Members")
    cur.execute("CREATE TABLE Members(No INT NOT NULL, StudentId INT NOT NULL, PhoneNumber INT NOT NULL, LastName VARCHAR(25) NOT NULL, FirstName VARCHAR(25) NOT NULL, Password VARCHAR(25) NOT NULL)")
    cur.execute("INSERT INTO Members(No, StudentId, PhoneNumber, LastName, FirstName, Password) VALUES(0, 20130000, 0123, 'Jack', 'London', 'pw_london')")
    cur.execute("INSERT INTO Members(No, StudentId, PhoneNumber, LastName, FirstName, Password) VALUES(0 ,20140449, 01059188572, 'juhee', 'lee', '1234')")
#    cur.execute("INSERT INTO Writers(Name) VALUES('Honore de Balzac')")
#    cur.execute("INSERT INTO Writers(Name) VALUES('Lion Feuchtwanger')")
#    cur.execute("INSERT INTO Writers(Name) VALUES('Emile Zola')")
#    cur.execute("INSERT INTO Writers(Name) VALUES('Truman Capote')")
