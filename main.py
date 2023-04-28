from flask import Flask,render_template,request,session,redirect,flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
from flask_mail import Mail
import os
from werkzeug.utils import secure_filename
import math


app = Flask(__name__)

with open('static/config.json','r') as c:
    params= json.load(c)["params"]
    
app.secret_key = 'super-secret-key'
# connection with database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/flask_db'
db = SQLAlchemy(app)
app.config['upload_folder']=params['upload_filelocation']
# mail setup
# app.config.update(
#     MAIL_SERVER = "smtp.gmail.com",
#     MAIL_PORT = "465",
#     MAIL_USE_SSL = 'True',
#     MAIL_USERNAME = "chandanjnp40769@gmail.com",
#     MAIL_PASSWORD ="chandan@3142",
# )
# mail = Mail(app)




class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120),nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    message=db.Column(db.String(120), nullable=False)
    
class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    # tagline = db.Column(db.String(180), nullable=False)
    slug = db.Column(db.String(120),nullable=False)
    content= db.Column(db.String(150), nullable=False)
    img_file= db.Column(db.String(150), nullable=False)
    sub_title= db.Column(db.String(150), nullable=False)
    date= db.Column(db.String(150), nullable=False)
   
   
    
@app.route("/")
def home():
    posts = Posts.query.filter_by().all()
    last = math.ceil(len(posts)/int(params['no_of_posts']))
    page = request.args.get('page')
    if(not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts = posts[(page-1)*int(params['no_of_posts']):(page-1)*int(params['no_of_posts'])+int(params['no_of_posts'])]
    if(page==1):
        prev="#"
        next="/?page="+str(page+1)
    elif(page==last):
        prev='/?page='+str(page-1)
        next='#'
    else:
        prev='/?page='+str(page-1)
        next="/?page="+str(page+1)
        
    return render_template("index.html", params=params,posts=posts,prev=prev, next=next)
  
  
  
@app.route("/about")
def about():
      return render_template("about.html", params=params)
  
  
  
  
  
@app.route("/dashboard",methods=['POST','GEt'])
def dashboard():
    #if user already login
    if('user' in session and session['user']==params['user_name']):
        posts = Posts.query.all()
        return render_template('dashboard.html',params=params,posts = posts)
    if(request.method=='POST'):
        username=request.form.get('uname')
        password=request.form.get('pass')
        if(username==params['user_name'] and password==params['user_password']):
            session['user']=username
            posts = Posts.query.all()
            return render_template('dashboard.html',params=params,posts = posts)
    return render_template('login.html',params=params)
   

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/dashboard')


@app.route("/upload",methods=['GET','POST'])
def upload():
    if('user' in session and session['user']==params['user_name']):
        if(request.method=='POST'):
            f = request.files['file']
            f.save(os.path.join(app.config['upload_folder'],secure_filename(f.filename)))
            return "uploaded successfully"
   
@app.route("/edit/newblog",methods=['GET','POST'])
def newblog():
    if('user' in session and session['user']==params['user_name']):
        if(request.method=='POST'):
            box_title=request.form.get('title')
            sub_title=request.form.get('subtitle')
            slug=request.form.get('slug')
            content=request.form.get('content')
            img_file=request.form.get('imagefile')
            date = datetime.now()
            post=Posts(title=box_title,sub_title=sub_title,slug=slug,content=content,img_file=img_file,date=date)
            db.session.add(post)
            db.session.commit()
            return redirect('/dashboard')  
    return render_template('newblog.html',params=params)
   


  
@app.route("/edit/<string:sno>",methods=['GET','POST'])
def editblog(sno):
    if('user' in session and session['user']==params['user_name']):
        if(request.method=='POST'):
            box_title=request.form.get('title')
            sub_title=request.form.get('subtitle')
            slug=request.form.get('slug')
            content=request.form.get('content')
            img_file=request.form.get('imagefile')
            date = datetime.now()
            if (sno=='0'):
                post=Posts(title=box_title,sub_title=sub_title,slug=slug,content=content,img_file=img_file,date=date)
                db.session.add(post)
                db.session.commit()
                return redirect('/dashboard')
            else:
                post=Posts.query.filter_by(sno=sno).first()
                post.title = box_title
                post.sub_title = sub_title
                post.slug = slug
                post.content = content
                post.img_file = img_file
                post.date = date
                db.session.commit()
                return redirect('/dashboard')
    post=Posts.query.filter_by(sno=sno).first()
    return render_template('edit.html',params=params,post=post)




@app.route("/delete/<string:sno>",methods=['GET'])
def deletepost(sno):
    if('user' in session and session['user']==params['user_name']):
        post = Posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
        return redirect('/dashboard')
  


@app.route("/post/<string:post_slug>",methods=['GET'])
def post(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template("post.html", params=params, post=post)
  
  
  
@app.route("/contact", methods=['GET','POST'])
def contact():
    if(request.method=='POST'):
        name=request.form.get('name')
        phone=request.form.get('phone')
        email=request.form.get('email')
        message=request.form.get('message')
        entry = Contact(name=name,phone= phone,email=email,message=message);
        db.session.add(entry)
        db.session.commit()
        # mail.send('New message from '+ name, 
        #           sender=email,
        #           recipients = "chandanjnp40769@gmail.com",
        #           body = message + '\n' + phone)
        flash("Thanks for contact with us","success")
        flash("we will soon contact with you","primary")
    return render_template("contact.html", params=params)

app.run(debug=True)