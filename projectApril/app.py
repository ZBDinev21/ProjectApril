from flask import Flask, render_template, redirect, url_for, request, session, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if valid_credentials(username, password):
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('account'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        
        if register_user(username, password, email):
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Registration failed. Username may already exist.', 'error')
    
    return render_template('register.html')

@app.route('/account')
def account():
    if 'username' not in session:
        flash('Please log in to view your account', 'error')
        return redirect(url_for('login'))
    
    return render_template('account.html', username=session['username'])

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out', 'info')
    return redirect(url_for('home'))

def valid_credentials(username, password):
    pass

def register_user(username, password, email):
    pass

if __name__ == '__main__':
    app.run(debug=True)