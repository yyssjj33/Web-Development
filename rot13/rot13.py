import webapp2
import cgi
form="""
	<html>
	  <head>
	    <title>Unit 2 Rot 13</title>
	  </head>

	  <body>
	    <h2>Enter some text to ROT13:</h2>
	    <form method="post">
	      <textarea name="text"
	                style="height: 100px; width: 400px;">%(text)s</textarea>
	      <br>
	      <input type="submit">
	    </form>
	  </body>

	</html>
"""

def rot13(s):
	res=[]
	for c in s:

		if c <='z' and c >= 'A':
			if c <='z' and c >= 'a':
				if ord('z')-ord(c) >= 13:
					c = chr(ord(c)+ 13)
				else:
					c = chr(ord(c)- 13)
				res.append(c)
				continue
			if c <= 'Z' and c >= 'A':
				if ord('Z')-ord(c) >= 13:
					c = chr(ord(c)+ 13)
				else:
					c = chr(ord(c)- 13)
				res.append(c)

		else:
			res.append(c)
	return "".join(res)

def escape_html(s):
	return cgi.escape(s, quote=True)

class MainPage(webapp2.RequestHandler):
	def write_form(self, text=""):
		self.response.out.write(form%{'text':escape_html(text)})
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.write_form()
	def post(self):
		text = self.request.get('text')
		newText = rot13(text)
		self.write_form(newText)





app = webapp2.WSGIApplication([('/', MainPage),], debug=True)