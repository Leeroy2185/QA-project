#!/usr/bin/python3
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, ValidationError, Length

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new.db"
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'
db = SQLAlchemy(app)


#~~~~~~~~~~~~~~~~~~~~~~~~ Owner Table ~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    car = db.relationship('Car', backref='user')
#~~~~~~~~~~~~~~~~~~~~~~~~ Business Table ~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reg = db.Column(db.String(30), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self, name):
        self.name = name
        return '[Reg {}]'.format(self.reg)
db.create_all()
#~~~~~~~~~~~~~~~~~~~~~~~~ Add Form ~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
class AddForm(FlaskForm):
    username = StringField('User Name', validators=[
        DataRequired(),
        ])
    carreg = StringField('Car Registration', validators=[
        DataRequired(),
        ])
    submit = SubmitField('Add Car')
#~~~~~~~~~~~~~~~ Drop Down List ~~~~~~~~~~~~~~# < Needed to populate the list with
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#   business names in the database
def carlist():
    return Car.query
#~~~~~~~~~~~~~~~~~~~~~~~~ Update Form ~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
class EditForm(FlaskForm):
    carreg = QuerySelectField(
            'Select reg to edit',
            query_factory=carlist,
            allow_blank=True,
            get_label='reg'
    )
    newreg = StringField(
            'Correct registration number',
            validators=[DataRequired()]
    )
    submit = SubmitField("Update Reg")
#~~~~~~~~~~~~~~~~~~~~~~~~ Delete Form ~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
class RemoveForm(FlaskForm):
    carreg = QuerySelectField(
            'Select Car to Delete',
            query_factory=carlist,
            allow_blank=True,
            get_label='reg'
    )
    submit = SubmitField("Remove Car")
#~~~~~~~~~~~~~~~~~~~~~~~~ Home Page ~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')
#~~~~~~~~~~~~~~~~~~~~~~~~ View Listings ~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

@app.route('/list', methods=['GET'])
def list():
    carlist = Car.query.with_entities(Car.reg)
    return render_template('list.html', carlist = carlist)


#~~~~~~~~~~~~~~~~~~~~~~~~ Add Listings ~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

@app.route('/add', methods=['GET', 'POST'])
def add():
    error = ""
    form = AddForm()

    if request.method == 'POST':
        username = form.username.data
        carreg = form.carreg.data
        user = User(name = username)
        db.session.add(user)
        db.session.commit()
        car = Car(reg = carreg, user = User.query.filter_by(name=username).first())
        db.session.add(car)
        db.session.commit()

        return "Added"

    return render_template('add.html', form=form, message=error)


#~~~~~~~~~~~~~~~~~~~~~~~~ Update Listing ~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

@app.route('/update', methods=['GET', 'POST'])
def update():
    error = ""
    form = EditForm()

    if request.method == 'POST':
        carreg = form.carreg.data
        newreg = form.newreg.data
        carreg.reg = newreg
        db.session.commit()
        return 'updated'

    return render_template('update.html', form=form, message=error)


#~~~~~~~~~~~~~~~~~~~~~~~~ Delete Listing ~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    error = ""
    form = RemoveForm()

    if request.method == 'POST':
        car = form.carreg.data
        db.session.delete(car)
        db.session.commit()
        return 'deleted'

    return render_template('delete.html', form=form, message=error)



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
