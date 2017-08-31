import webapp2

class MainPage(webapp2.RequestHandler):
    def write_form(error="", month="", day="", year=""):
    	self.response.out.write(form % {"error":error,
                                        "month":month,
                                        "day": day,
                                        "year": year})

    def get(self):
        self.write.form()

    def post(self):
    	user_month = valid_month(self.request.get('month'))
    	user_day = valid_day(self.request.get('day'))
    	user_year = valid_year(self.request.get('year'))

    	if not (user_month and user_day and user_year):
    		self.write.form("That doesn't look valid to me, friend.")
    	else:
    		self.response.out.write("Thanks That's a totally valid day!")

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

