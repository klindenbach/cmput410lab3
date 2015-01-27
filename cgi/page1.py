#!/usr/bin/env python
 
import cgi

form = cgi.FieldStorage()

bday   = form.getvalue("birthdate")
hobby  = form.getvalue("hobby")
home  = form.getvalue("home")
form1 = form.getvalue("form1")
form2 = form.getvalue("form2")

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
if form1:
    print '<a href="/cgi/page1.py">Form 1</a>\n'
if form2:
    print '<a href="/cgi/page2.py">Form 1</a>\n'
if home:
    print '<a href="/">Home</a>\n'

print """ <br /><br />
    <marquee>Arbitrary feature</marquee>
    <form method="post" action="page2.py">
        First Name: <input type="text" name="first" /> <br />
        Family Name: <input type="text" name="family" /> <br />
        <input type="checkbox" name="form1" /> Show Form 1<br />
        <input type="checkbox" name="form2" /> Show Form 2<br />
        <input type="checkbox" name="home" /> Show Home<br />
        <input type="submit" value="Submit">
    </form>
</body>
</html>"""
