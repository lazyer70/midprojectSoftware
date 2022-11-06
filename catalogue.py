#連線DB
from itertools import product
from dbConfig import conn, cur
def getList():
    #查詢
    sql="select id,product,nums from catalogue order by id ;"
    cur.execute(sql)
    records = cur.fetchall()
    return records
catalogueL=getList()

def delProduct(id):
    sql="delete from catalogue where id=%s;"#%s 讓你=前面的東西以他的數字或字串取代掉=24行的id
    cur.execute(sql,(id,))
    conn.commit()#寫入
    return True

def addNums(id,Nums):
    if Nums>0:
        sql="update catalogue set nums=nums+%d where id=%s;"%(Nums,id)
    cur.execute(sql)
    conn.commit()
    return True

def addProduct(product,nums):
    sql="insert into catalogue (product,nums) values (%s,%s);"
    cur.execute(sql,(product,nums))
    conn.commit()
    return True
def reviseProduct(id,name,Nums):
    if Nums>0:
        sql="update catalogue set nums=%d , product='%s' where id=%s;"%(Nums,name,id)
    cur.execute(sql)
    conn.commit()
    return True
