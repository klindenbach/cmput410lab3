#!/usr/bin/env python
 
import cgi

form = cgi.FieldStorage()

bday   = form.getvalue("birthdate")
hobby  = form.getvalue("hobby")

print """Content-type: text/html

<!DOCTYPE html>
<html>
<head> 
    <meta charset="utf-8" />
    <title>Page 1</title>
</head>
<body> """

if bday:
    print "<p> Your birthday is %s</p>\n" % bday
if hobby:
    print "<p> Your hobby is %s</p>\n" % hobby

print """
    <form method="post" action="page2.py">
        First Name: <input type="text" name="first" />
        <br/>
        Family Name: <input type="text" name="family" />
        <br />
        <input type="submit" value="Submit">
    </form>
</body>
</html>"""
