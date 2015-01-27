#!/usr/bin/env python

import cgi

form = cgi.FieldStorage()

first = form.getvalue("first")
last  = form.getvalue("family")

print """Content-type: text/html

<!DOCTYPE html>
<html>
<head> 
    <meta charset="utf-8" />
    <title>Page 2</title>
</head>
<body> """

if first and last:
    print " <p> Hello %s %s <p>\n" % (first, last)

print """
    <form method="post" action="page1.py">
        Birthdate: <input type="text" name="birthdate" />
        <br/>
        Main Hobby: <input type="text" name="hobby" />
        <br />
        <input type="submit" value="Submit">
    </form>
</body>
</html>"""
