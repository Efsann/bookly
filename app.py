# from flask import Flask, render_template, request, redirect, url_for

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return redirect(url_for('login'))

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']

#         # Sadə yoxlama
#         if email == 'test@example.com' and password == '12345':
#             return redirect(url_for('index'))  # indi index.html-ə yönləndirəcək
#         else:
#             return "Email və ya şifrə yanlışdır", 401
#     return render_template('login.html')


# @app.route('/index')
# def index():
#     return render_template('index.html')


# if __name__ == "__main__":
#     app.run(debug=True)
