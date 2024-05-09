from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from calorie import Calorie
from temperature import Temperature

app = Flask(__name__)


class HomePage(MethodView):
    """Class to create a webpage instance when a user
    visits the webpage
    """
    def get(self):
        return render_template('index.html')


class CaloriePage(MethodView):

    def get(self):
        calorie_form = CalorieForm()
        return render_template('calorie_page.html',
                               calorie_form=calorie_form)

    def post(self):
        calorie_form = CalorieForm(request.form)
        temperature = Temperature(calorie_form.country.data,
                                  calorie_form.city.data).get()
        calorie = Calorie(float(calorie_form.weight.data),
                          float(calorie_form.height.data),
                          float(calorie_form.age.data),
                          float(temperature))
        calories = calorie.calc()

        return render_template('calorie_page.html',
                               result=True,
                               calorie_form=calorie_form,
                               calories=calories)


class CalorieForm(Form):

    weight = StringField('Weight: ', default=120)
    height = StringField('Height: ', default=168)
    age = StringField('Age: ', default=25)
    country = StringField('Country: ',default='Italy')
    city = StringField('City: ', default='Rome')
    button = SubmitField('Calculate')


app.add_url_rule('/',
                 view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calorie_page',
                 view_func=CaloriePage.as_view('calorie_page'))

app.run(port=5001)