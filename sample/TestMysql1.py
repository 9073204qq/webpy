import web
import mysql.connector

urls = (
    '/(.*)', 'hello'
)

app = web.application(urls, globals())
db = web.database(dbn='mysql', host='127.0.0.1', port=3308,
                  db='forum', user='root', pw='12345678',
                  driver = 'mysql.connector')

users = list(db.select('mintest', where="id>0"))
print(users)


