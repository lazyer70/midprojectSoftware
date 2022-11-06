#!C:\Users\User\AppData\Local\Programs\Python\Python37-32\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
#連線DB
from dbConfig import conn, cur
import catalogue as cat
import cart 
#先印出http 表頭
print("Content-Type: text/html; charset=utf-8\n")
#連續3個"""表多行字串
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>商品目錄</title>
</head>

<body>
商品目錄 
<a href='seecart.py'> 觀看購物車 </a><hr>

 
""")
proList=cat.getList()
cartList=cart.ListCart()
if 1 in proList[0]:
    print(f"<p>{proList}</p>")
for (id,product,nums) in proList:
	print(f"""<p>編號{id}: 商品:{product} 數量:{nums} <a href='addcart.html'>新增購物車</a> </p>""")
print("<hr></body></html>")


