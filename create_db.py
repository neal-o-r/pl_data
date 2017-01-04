import MySQLdb
import os

fs = os.listdir('seasons/')

schema = "(years VARCHAR(5), division VARCHAR(2), date VARCHAR(10), home_team VARCHAR(25), away_team VARCHAR(25), fthg INT, ftag INT)"


db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="",     # your password
                     db="pl_matches",     # name of the data base
                     local_infile=1)

cur = db.cursor()

for i, f in enumerate(fs):

        print(str(i) + " of " + str(len(fs)))

        name = "season" + f.split('.')[0].replace('-','')
        make_table = "CREATE TABLE IF NOT EXISTS " + name + " " + schema + ";" 
        
        cur.execute(make_table)

        load_file = "LOAD DATA LOCAL INFILE 'seasons/"+ f +"' INTO TABLE " + name + " COLUMNS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES;"

        cur.execute(load_file)

