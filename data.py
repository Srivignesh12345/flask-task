from flask_mongoengine import MongoEngine

url="mongodb+srv://Srivignesh:sri12345*@cluster0.2pgxwru.mongodb.net/vicky?retryWrites=true&w=majority"

mydata = MongoEngine()
class Bikes(mydata.Document):
    bikeregno=mydata.StringField()
    bikemodel=mydata.StringField()
    bikecc=mydata.IntField()
    bikebrand=mydata.StringField()
    bikemileage=mydata.IntField()
    bikeownername=mydata.StringField()
    bikeownercount=mydata.IntField()
    bikelocation=mydata.StringField()
    bikeownerphone=mydata.IntField()