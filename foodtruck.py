import psycopg2
from flask import Flask, request, redirect, render_template

app = Flask(__name__)


#---------- DB ------------------
def connectToDB():
  conn = psycopg2.connect("dbname=food_truck_DB")
  cur = conn.cursor()
  return conn, cur

def closeDB(conn, cur):
  cur.close()
  conn.close()

#---------------------------------



@app.route('/')
def index():
  return render_template('home.html')


@app.route('/menu')
def showMenu():
  conn, cur = connectToDB()
  cur.execute("SELECT * FROM food")
  results = cur.fetchall() # tuples in a list
  closeDB(conn,cur)
  priceList = []
  for item in results:
    price = item[3]
    print(price)
    priceList.append(price/100)
  new_price_list = [str(price)+'0' for price in priceList]

  return render_template('menu.html', list = results, priceList = new_price_list)


#-----detail page--------------------------

@app.route('/<name>')
def detail(name):
  conn, cur = connectToDB()
  print(name)
  cur.execute(f"SELECT * FROM food WHERE name = '{name}' ")
  result = cur.fetchone()
  closeDB(conn,cur)

  price = result[3]/100
  print(type(str(price)))
  price = str(price)+'0'

  return render_template('detail.html', item = result, price = price)


#-----contact page--------------------------
@app.route('/contact')
def showContact():
  return render_template('contact.html')


@app.route('/contact', methods=['POST'])
def saveForm():
  name = request.form.get('userName')
  email = request.form.get('userEmail')
  phone = request.form.get('userTel')
  message = request.form.get('userMessage')
  print(name, email, phone, message)

  # insert form data into form table
  conn, cur = connectToDB()
  try:
    cur.execute("INSERT INTO form(name, email, phone, message) VALUES(%s,%s,%s,%s)", (name, email, phone, message))
    conn.commit()
    print('Successfully inserted data into table.')
  except  (Exception, psycopg2.Error) as error:
    if (conn):
      print("Record failed to insert", error)
  finally:
    if (conn):
      closeDB(conn,cur)

  return redirect('/')


#-----about page--------------------------

@app.route('/about')
def showAbout():
  return render_template('about.html')


app.run(debug=True)