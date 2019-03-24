from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from fun import se

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
        global departure
        global depart_id
        global destination
        global dest_id
        global date123
        global quantity
    id = db.Column(db.Integer, primary_key=True)
    departure = db.Column(db.String(120), unique=True, nullable=False, default='Washington, DC')
    depart_id = db.Column(db.String(120), unique=True, nullable=False, default='WAS')
    image_fi = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    
    #Dunder method & Magic method
    def __repr__(self):
        return "User('{self.depart_id}')"

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/web", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Start Web Scraping for Amtrak!!!', 'success')
        global` departure
        global depart_id
        global destination
        global dest_id
        global date123
        global quantity
        departure = form.departure.data
        depart_id = form.depart_id.data
        destination = form.destination.data
        dest_id = form.dest_id.data
        date123 = form.date123.data
        quantity = form.quantity.data
        return redirect(url_for('home'))
    return render_template('web_scraping.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

#============================================
class buy_ticket():
    def __init__(self, departure, depart_id, destination, dest_id, date, quantity, email, password):
        driver.get("https://www.amtrak.com/home")
        self.departure = departure
        self.depart_id = depart_id
        self.destination = destination
        self.dest_id = dest_id
        #MM/DD/YY
        self.date = date
        self.quantity = quantity
        self.email = email
        self.password = password
    def input_information(self):

        se.send_keys_by_xpath(driver, '//*[@id="page-content"]/section[2]/div[2]/article/div[2]/div/div[5]/form/div/div[3]/div[1]/div[2]/div/div[1]/div/div/div/input[2]', self.departure)
        #time.sleep(1)
        se.click_by_id(driver, self.depart_id)

        se.send_keys_by_xpath(driver, '//*[@id="page-content"]/section[2]/div[2]/article/div[2]/div/div[5]/form/div/div[3]/div[1]/div[2]/div/div[2]/div/div/div/input[2]', self.destination)
        #time.sleep(1)
        se.click_by_id(driver, self.dest_id)

        se.send_keys_by_xpath(driver, '//*[@id="page-content"]/section[2]/div[2]/article/div[2]/div/div[5]/form/div/div[3]/div[1]/div[3]/div[1]/div/div[1]/div/div[1]/div/div[2]/input', self.date)

        se.click_by_xpath(driver, '//*[@id="page-content"]/section[2]/div[2]/article/div[2]/div/div[5]/form/div/div[3]/div[1]/div[4]/div[1]/div[2]')
        #pos = driver.find_element_by_xpath('//*[@id="page-content"]/section[2]/div[2]/article/div[2]/div/div[5]/form/div/div[3]/div[1]/div[4]/div[2]/div[1]/ul/li[2]/div/div[2]/input')
        #pos.clear()
        #pos.send_keys(self.quantity)
        #se.send_keys_by_name(driver, '/sessionWorkflow/productWorkflow[@product='Rail']/tripRequirements/allJourneyRequirements/@adultTravellers', self.quantity)
        se.click_by_id(driver, 'findtrains')

    def pick_train(self):
        se.click_by_name(driver, "/sessionWorkflow/productWorkflow[@product='Rail']/selectedJourney[1]/@selectedPassengerFareBeanKey")
        se.click_by_xpath(driver, "/html/body/div[3]/div/div/div[3]/div[2]/div[3]/form[1]/table/tbody/tr[3]/td/div/input")
        se.click_by_xpath(driver, "/html/body/div[2]/div/div/div[2]/form/div[2]/div[2]/input")
    def log_in(self):
        driver.find_element_by_id('email').send_keys(self.email)
        driver.find_element_by_id( 'password').send_keys(self.password)
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/div/form/div/div[3]/input").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/form/div[3]/div/div/div[1]/div/p[3]/label/span[1]").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/form/div[4]/div[2]/input").click()
    def main(self):
        self.input_information()
        self.pick_train()
        self.log_in()

if __name__ == '__main__':
    app.run(debug=True)
    begin = time.time()
    print(begin)
    print(departure)
    #driver = webdriver.Firefox()
    driver = webdriver.Chrome()
    obj = buy_ticket(departure, depart_id, destination, dest_id, date123, quantity, 'anong9420@gmail.com', 'Deming0519@')
    obj.main()
    end = time.time()
    T = int(end-begin)
    print("total_time = %d sec" %T)

