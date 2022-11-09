#!C:\Users\User\AppData\Local\Programs\Python\Python37-32\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
#連線DB
from dbConfig import conn, cur
import catalogue as cat
#先印出http 表頭
print("Content-Type: text/html; charset=utf-8\n")
#連續3個"""表多行字串
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>商品列表</title>
</head>

<body>
商品列表 
<a href='addproduct.html'> 新增商品 </a><hr>

 
""")
proList=cat.getList()
for (id,product,nums,price) in proList:
	print(f"""<p>編號{id}: 商品:{product} 數量:{nums} 價格:{price}<a href='addProductNums.html'>補貨增加</a> </p>""")
print("""<form method="delProduct" action="delectProduct.py"> 輸入想刪除商品編號<input type="text" name='id'><input type="submit">""")
print("<hr><a href='reviseproduct.html'> 修改商品細節 </a>")
print("<hr></body></html>")