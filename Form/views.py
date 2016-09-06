
from flask import render_template, request, redirect, url_for, Response, make_response
from Form import database_helper 
from Form import app
from string import join 
import ast
from Tkinter import Tk
from tkFileDialog import askopenfilename

@app.route("/", methods=["GET", "POST"])
def urls():
    if request.method == "POST":
      url =request.form.get("url", None)
      url_entry = {
         "url": url
       }
      database_helper.add_url(url_entry) 
    return render_template("index.html")
    
@app.route("/users", methods=["GET", "POST"])
def users():
    user_list = database_helper.get_all_urls() #postgresql outputs strings with parathesis, qoats and extra commas
    user_list = str(user_list)  #convert the list of characters to character strings
    user_list = user_list.replace("('", "").replace("',)", "")  #replace (' and ',) with empty srings
    user_list = user_list.split(',')  #split the strings of characters into strigs seperated by commas
    user_list = user_list[1:-1]      # take out [ at beginning and ] at the end
    return render_template("users.html", user_list=user_list)


@app.route("/csvupload" )
def clever_function():
    tk = Tk()
    tk.withdraw()
    f = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    database_helper.upload(f)
    tk.destroy()
    return render_template("/csvupload.html")
    #return 'CSV file uoloaded!'
    
#app.jinja_env.globals.update(clever_function=clever_function)
 
    
    