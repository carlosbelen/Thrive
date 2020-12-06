# Import the app variable from the init
from health_app import app, db
# Import specific packages from Flask
from flask import render_template,request,redirect,url_for

# Import our Form(s)
from health_app.forms import UserInfoForm, LoginForm, PostForm

# Import of our Model(s) for the Database
from health_app.models import User,Post, check_password_hash 

# Import for Flask Login funcitons - login_recheck_password_hashquired
#  login_user, current_user, logout_user
from flask_login import login_required,login_user,current_user,logout_user

#Default Home Route
@app.route('/')
def home():
    return render_template('home.html')

# Creation of Calculator Route:
@app.route('/calculators')
def calculators():
    return render_template('calculators.html')

# GET == Gathering Info
# POST == Sending Info
@app.route('/register', methods = ['GET', 'POST'])
def register():
    # Init our Form - INSTANTIATING HERE
    form = UserInfoForm()
    
    #now sending form information instead of just text (i.e. names)
    if request.method == 'POST' and form.validate():
        #Get Information from the form
        username = form.username.data
        email = form.email.data
        password = form.password.data
        # print the data to the server that comes form the form 
        print(username,email,password)

        # Creation/Init of our User Class (aka Model)  -- INSTANTIATING HERE
        user = User(username,email,password)

        # Open a connection to the database
        db.session.add(user)

        # Commit all data to the database
        db.session.commit()

    return render_template('register.html', user_form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        # Saving the logged in user to a variable
        logged_user = User.query.filter(User.email == email).first()
        #check the password of the newly found user
        #and validate the password against the hash value
        #inside of the database
        if logged_user and check_password_hash(logged_user.password, password):
            login_user(logged_user)
            # Redirected user
            return redirect(url_for('home'))
        else:
            # Redirect User to login route
            return redirect(url_for('login'))
    return render_template('login.html', login_form = form)

# Creation of logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# Creation of Blog route
@app.route('/blog')
def blog():
    # The following line is selecting all the information from post and displaying at home page
    posts = Post.query.all()
    return render_template('blog.html',user_posts = posts)

# Creation of Posts route
@app.route('/posts', methods = ['GET','POST'])
@login_required
def posts():
    form = PostForm()
    if request.method == 'POST' and form.validate():
        title = form.title.data
        content = form.content.data
        user_id = current_user.id
        post = Post(title,content,user_id)
        
        db.session.add(post)

        db.session.commit()
        return redirect(url_for('blog'))
    return render_template('posts.html', post_form = form)

# post detail route to display info about a post
@app.route('/posts/<int:post_id>')
@login_required
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post_detail.html', post = post)

@app.route('/posts/update/<int:post_id>',methods = ['GET','POST'])
@login_required
def post_update(post_id):
    # get the link (using link:post_id) check the form, once its validated, commit changes, return redirct to home to see changes
    post = Post.query.get_or_404(post_id)
    form = PostForm()

    if request.method == 'POST' and form.validate():
        title = form.title.data
        content = form.content.data
        user_id = current_user.id

        # Update the Database with the new Info
        post.title = title
        post.content = content
        post.user_id = user_id

        # Commit the changes to the database
        db.session.commit()
        return redirect(url_for('blog'))
    return render_template('post_update.html', update_form = form)

@app.route('/posts/delete/<int:post_id>',methods = ['GET','POST','DELETE'])
@login_required
def post_delete(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('blog'))
