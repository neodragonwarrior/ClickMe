import webbrowser
import sys
f = open('clickjacktest.html','w')
testurl= input("Enter test url : ")
message = """<html>
<body>
<h1>Clickjack Test Page</h1>
<iframe src="{testurl}" width="800" height="500"></iframe>
<p><a href="https://www.owasp.org/index.php/OWASP_Click_Me_Project">OWASP reference page </a> </p>
<!-- OWASP Click Me_Clickjack Test Page @Arun Kumar -->
</body>
</html>
""".format(testurl=testurl)
f.write(message)
f.close()
webbrowser.open_new_tab('clickjacktest.html')
 
