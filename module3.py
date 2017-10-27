import cx_Oracle

SQL="select *from users"
con = cx_Oracle.connect('infy/1234')
c = con.cursor()
c.execute(SQL)
for row in c:
    print(row)
c.close()
con.close()
