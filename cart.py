#連線DB
from itertools import product
from dbConfig import conn, cur
import catalogue as cat
ProductList=cat.getList()
def ListCart():
    #查詢
    sql="select id,product,nums from cart order by id ;"
    cur.execute(sql)
    records = cur.fetchall()
    return records

def delCartProduct(id):
    sql="delete from cart where id=%s;"#%s 讓你=前面的東西以他的數字或字串取代掉=24行的id
    cur.execute(sql,(id,))
    conn.commit()#寫入
    return True

def addCart(id,nums):
    cartList=ListCart()
    for i in range(len(cartList)):
        if id == cartList[i][0]:
            sql="update cart set nums=nums+%d where id=%d;"%(nums,id)
            cur.execute(sql)
            conn.commit()
        return True
    else:
        for i in range(len((ProductList))):
            if id == ProductList[i][0]:
                product=ProductList[i][1]
            else:
                continue
        sql="insert into cart (id,product,nums) values (%d,'%s',%d);"%(id,product,nums)
        cur.execute(sql)
        conn.commit()
        return True
    