# Flask Web App With Python
- Updated from here:  https://pythonspot.com/flask-web-app-with-python/
- Further Explanation:  http://flask.pocoo.org/docs/1.0/quickstart/

In this tutorial you’ll learn how to build a web app with Python. We’ll use a micro-framework called Flask.

## Why Flask?
- easy to use.
- built in development server and debugger
- integrated unit testing support
- RESTful request dispatching
- uses Jinja2 templating
- support for secure cookies (client side sessions)
- 100% WSGI 1.0 compliant
- Unicode based
= extensively documented

### Installing Flask
Install Flask using the command:

`$ pip install Flask`

### Create the first app
Create a file called hello.py
```
from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
   return "Hello World!"
 
if __name__ == "__main__":
   app.run()
```

Finally run the web app using this command:

(UNIX)

`$ export FLASK_APP=hello.py; export FLASK_ENV=development`

(WINDOWS)

`$ set FLASK_APP=hello.py; set FLASK_ENV=development`

`flask run`

Open http://localhost:5000/ in your webbrowser, and “Hello World!” should appear.

### Creating URL routes
URL Routing makes URLs in your Web app easy to remember.

We will now create some URL routes:
- /hello
- /members/
- /members/name/

Copy the code below and save it as app.py
```
from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def index():
   return "Index!"
 
@app.route("/hello")
def hello():
   return "Hello World!"
 
@app.route("/members")
def members():
   return "Members"
 
@app.route("/members/<string:name>/")
def getMember(name):
   return name
 
if __name__ == "__main__":
   app.run()
```

Start app.py

`$ set FLASK_APP=app.py; set FLASK_ENV=development`

`flask run`

Try the URLs in your browser:

- http://127.0.0.1:5000/
- http://127.0.0.1:5000/hello
- http://127.0.0.1:5000/members
- http://127.0.0.1:5000/members/Jordan/

### Style Flask Pages

We will separate code and User Interface using a technique called Templates. We make the directory called /templates/ and create the template:

`<h1>Hello {{name}}</h1>`

The Python Flask app with have a new URL route. We have changed the default port to 80, the default HTTP port:

```
from flask import Flask, flash, redirect, render_template, request, session, abort
 
app = Flask(__name__)
 
@app.route("/")
def index():
   return "Flask App!"
 
@app.route("/hello/<string:name>/")
def hello(name):
   return render_template(
   'test.html',name=name)</string:name>
 
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80)
```

You can then open : http://127.0.0.1/hello/Jackson/

### Styling the template
Do you want a better looking template? Lets modify the file:
```
{% extends "layout.html" %}
{% block body %}
<div class="block1">
<h1>Hello {{name}}!</h1>
<h2>Here is an interesting quote for you:</h2>
"The limits of my language are the limits of my mind. All I know is what I have words for."
<img src="http://www.naturalprogramming.com/images/smilingpython.gif">
</div>
{% endblock %}
```

We then create layout.html which defines the look of the page. (You may want to split the stylesheet and layout.html file). Copy this as layout.html
```
<title>Website</title>
 
<style>
@import url(http://fonts.googleapis.com/css?family=Amatic+SC:700);</p>
<p>body{<br />
    text-align: center;<br />
}<br />
h1{<br />
    font-family: 'Amatic SC', cursive;<br />
    font-weight: normal;<br />
    color: #8ac640;<br />
    font-size: 2.5em;<br />
}</p>
</style>
{% block body %}
{% endblock %}
```
Restart the App (if needed) and open the url. http://127.0.0.1/hello/Jackson/
You can pick any name other than Jackson.

### Passing Variables
Lets display random quotes instead of always the same quote. We will need to pass both the name variable and the quote variable. To pass multiple variables to the function, we simply do this:
```
   return render_template(
'test.html',**locals())
```

Our new test.html template will look like this:
```
{% extends "layout.html" %}
{% block body %}
<div class="block1">
<h1>Hello {{name}}!</h1>
<h2>Here is an interesting quote for you:</h2>
{{quote}}
 
<img src="http://www.naturalprogramming.com/images/smilingpython.gif">
 
</div>
{% endblock %}
```

We will need to pick a random quote. To do so, we use this code:
```
    quotes = [ "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
"'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
"'To understand recursion you must first understand recursion..' -- Unknown",
"'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
"'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
"'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"  ]
randomNumber = randint(0,len(quotes)-1)
quote = quotes[randomNumber]
```

The first thing you see is we have defined an array of multiples quotes. These can be accessed as quote[0], quote[1], quote[2] and so on. The function randint() returns a random number between 0 and the total number of quotes, one is subtracted because we start counting from zero. Finally we set the quote variable to the quote the computer has chosen. Copy the code below to app.py:
```
from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint
 
app = Flask(__name__)
 
@app.route("/")
def index():
   return "Flask App!"
 
#@app.route("/hello/<string:name>")
@app.route("/hello/<string:name>/")
def hello(name):
#    return name
quotes = [ "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
"'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
"'To understand recursion you must first understand recursion..' -- Unknown",
"'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
"'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
"'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"  ]
randomNumber = randint(0,len(quotes)-1)
quote = quotes[randomNumber] </string:name></string:name>
 
return render_template(
'test.html',**locals())
 
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80)
```

When you restart the application it will return one of these quotes at random.
