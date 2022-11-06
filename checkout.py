#!C:\Users\User\AppData\Local\Programs\Python\Python37-32\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import cart as ca
#連線DB
from dbConfig import conn, cur
#先印出http 表頭
print("Content-Type: text/html; charset=utf-8\n")
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>購物車結帳</title>
</head>
<body>
""")


if ca.checkoutcart():
    print("已結帳")
else:
    print("結帳失敗")
print("<br><a href='listproduct.py'>回商品目錄</a>")
print("</body></html>")