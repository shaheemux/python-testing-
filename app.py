from flask import Blueprint; 

views = Blueprint(__name__ ,"views")

@views.route("/")
def home():
    return "This is also ez"
