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
    maxid="SELECT MAX(id) FROM catalogue;;"
    cur.execute(maxid)
    maxid=cur.fetchall()
    maxID=maxid[0][0]#從sql提取的資料會轉成list因此得提出來
    if id>(maxID):
        print(f"<p>{maxID}</p>")
        return False
    for i in range(len(cartList)):
        if id == cartList[i][0]:
            sql="update cart set nums=nums+%d where id=%d;"%(nums,id)
            cur.execute(sql)
            conn.commit()
            return True
    for j in range(len((ProductList))):
        if id == ProductList[j][0]:
            product=ProductList[j][1]
        else:
            continue
        sql="insert into cart (id,product,nums) values (%d,'%s',%d);"%(id,product,nums)
        cur.execute(sql)
        conn.commit()
    return True
def checkoutcart():
    cartL=ListCart()
    for i in range(len(cartL)):
        for j in range(len(ProductList)):
            if cartL[i][0]==ProductList[j][0]:
                id=cartL[i][0]
                cartNums=cartL[i][2]
                sql="update catalogue set nums=nums-%d where id=%d;"%(cartNums,id)
                cur.execute(sql)
                conn.commit()
                sql="delete from cart where id=%d;"%(id)
                cur.execute(sql)
                conn.commit()#寫入
    return True
