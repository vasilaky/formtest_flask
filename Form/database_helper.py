# Adding a User
import psycopg2
import StringIO


def dict_cursor(cnn):
    return cnn.cursor()

#cnn=psycopg2.connect(database="flask", user="postgres", password="mishi", host="127.0.0.1", port="5432")
DB_URL="host=localhost user=postgres password=mishi dbname=flask port=5432"
#cur = cnn.cursor()
def add_url(url_entry):
    with psycopg2.connect(DB_URL) as cnn:
        with dict_cursor(cnn) as db:
            q = '''INSERT INTO test (url) VALUES ( %(url)s )'''
            # Insert a row of data
            db.execute(q, {"url": url_entry['url']})

def get_all_urls():
    with psycopg2.connect(DB_URL) as cnn:
        with dict_cursor(cnn) as db:
            q = '''SELECT url FROM test'''
            db.execute(q)
            user_list = db.fetchall()
    return user_list

def upload(f):
    with psycopg2.connect(DB_URL) as cnn:
        with dict_cursor(cnn) as db:
            #sqlstr = "COPY users (cell_phone, name, region , village) FROM STDIN DELIMITER ',' CSV"
            #f = StringIO.StringIO(f)
            with open(f) as f:
              db.copy_from(f, 'test', sep=',' , columns=('url' , 'name'))
            #with open(f) as f: 
            #db.copy_expert(sqlstr, f)
            #f = open(f)
            #db.copy_from(f, 'users', sep=',' , columns=('cell_phone' , 'name' , 'region' , 'village'))
            #with open(f) as f:
              #db.copy_from(f, 'test', sep=',' , columns=('r','u'))
            
           
