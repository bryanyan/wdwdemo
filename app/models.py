from app import db

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(140))
	title = db.Column(db.String(140))
	timestamp = db.Column(db.String(140))

	def __repr__(self):
		return '<Post %r>' %(self.body)