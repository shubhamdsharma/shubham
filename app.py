Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from flask import Flask, render_template, request, redirect, url_for
... 
... app = Flask(__name__)
... 
... # Dummy user credentials
... ALLOWED_USERNAME = 'shubhamdsharma'
... ALLOWED_PASSWORD = 'shubhamUpsc'
... 
... @app.route('/')
... def index():
...     return render_template('index.html')
... 
... @app.route('/login', methods=['POST'])
... def login():
...     username = request.form['username']
...     password = request.form['password']
...     if username == ALLOWED_USERNAME and password == ALLOWED_PASSWORD:
...         return redirect(url_for('enter_data'))
...     else:
...         return render_template('index.html', message='Invalid username or password. Please try again.')
... 
... @app.route('/enter_data')
... def enter_data():
...     # This page requires authentication, so ensure the user is logged in
...     return render_template('enter_data.html')
... 
... if __name__ == '__main__':
...     app.run(debug=True)
