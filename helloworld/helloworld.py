import webapp2
import cgi
form = """
	<form method="post" >
		What is yout birthday?
		<br>
		<label> Month
		<input type="text" name="month" value="%(month)s">
		</label>
		<label> Day
		<input type="text" name="day" value="%(day)s">
		</label>
		<label> Year
		<input type="text" name="year" value="%(year)s">
		</label>
		<div style="color:red">%(error)s</div>	
		<input type="submit">

	</form>
"""

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
month_abbvs = dict((m[:3].lower(), m) for m in months)

def valid_month(month):
  	if month:
  		short_month = month[:3].lower()
  		return month_abbvs.get(short_month)
def valid_day(day):
  	if day:
  		if day.isdigit():
  			if int(day) <=31 and int(day)>=1:
  				return int(day);
def valid_year(year):
	if year and year.isdigit():
		if int(year)>1900 and int(year)<2020:
			return int(year)

def escape_html(s):
	return cgi.escape(s, quote=True)

class MainPage(webapp2.RequestHandler):
	def write_form(self, error="", month="", day="", year=""):
		self.response.out.write(form % {"error":error, 
										"month":escape_html(month),
										"day":escape_html(day),
										"year":escape_html(year)})


	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.response.write('<h1>Hello, Udacity!</h1>')
		self.write_form()
	def post(self):
		user_month = self.request.get('month');
		user_day = self.request.get('day');
		user_year = self.request.get('year');

		month = valid_month(user_month);
		day = valid_day(user_day);
		year = valid_year(user_year);

		if ( month and day and year ):
			self.redirect("/thanks")
			# self.response.out.write("Thanks! That's all valid.")
			
		else:
			
			self.response.write('<h1>Hello, Udacity!</h1>')
			self.write_form("That doesn't look valid for me!", user_month, user_day,user_year)
			

class ThanksHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write("thanks! That's all valid.")


# class TestHandler(webapp2.RequestHandler):
# 	def post(self):
# 		q = self.request.get("q");
# 		self.response.out.write(q)
# 		self.response.headers['Content-Type'] = 'text/plain'
# 		self.response.out.write(self.request);

app = webapp2.WSGIApplication([('/', MainPage),
								('/thanks', ThanksHandler)],debug=True)
