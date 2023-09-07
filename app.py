from flask import Flask,jsonify,render_template,request,redirect,session
from data import *

app=Flask(__name__)

app.config['MONGODB_HOST']=url
mydata.init_app(app)
app.secret_key='sri'

@app.route("/logout")
def performOut():
    if session.get('logged'):
        session['logged']=None
    return render_template("login.html")

@app.route("/",methods=['GET','POST'])
def performLogin():
    if request.method=="GET":
        return render_template("login.html")
    else:
        user=request.form['User']
        pas=request.form['pass']
        if user=="srivignesh" and pas=="sri12345*":
            session['logged']=user
            return redirect("/nav")
        elif user=="vicky" and pas=="vicky112":
            session['logged']=user 
            return redirect("/nav")
        else:
            return render_template("login.html")


@app.route("/erase/<bikeregno>")
def performDelete(bikeregno):
    if session.get('logged'):
        collected=Bikes.objects(bikeregno=bikeregno).first()
        collected.delete()
        return redirect("/list")
    else:
        return render_template("login.html")

@app.route("/update/<bikeregno>",methods=["GET","POST"])
def performEdit(bikeregno):
    if session.get('logged'):
        if request.method=="GET":
            collected=Bikes.objects(bikeregno=bikeregno).first()
            return render_template("edit.html",data=collected)
        else:
            bikebrand=request.form['bikebrand']
            bikeregno=request.form['bikeregno']
            bikemodel=request.form['bikemodel']
            bikecc=int(request.form['bikecc'])
            bikemileage=int(request.form['bikemileage'])
            bikeownername=(request.form['bikeownername'])
            bikeownerphone=int(request.form['bikeownerphone'])
            bikeownercount=int(request.form['bikeownercount'])
            bikelocation=(request.form['bikelocation'])
            Bikes.objects(bikeregno=bikeregno).update_one(set__bikeregno=bikeregno,
                                                set__bikemodel=bikemodel,
                                                set__bikebrand=bikebrand,
                                                set__bikecc=bikecc,
                                                set__bikemileage=bikemileage,
                                                set__bikeownername=bikeownername,
                                                set__bikeownerphone=bikeownerphone,
                                                set__bikeownercount=bikeownercount,
                                                set__bikelocation=bikelocation)
            return redirect("/list")
    else:
        return render_template("login.html")

@app.route("/pick/<bikeregno>")
def showRead(bikeregno):
    if session.get('logged'):
        collected=Bikes.objects(bikeregno=bikeregno).first()
        return render_template("read.html",data=collected)
    else:
        return render_template("login.html")

@app.route("/new",methods=['GET','POST'])
def new():
    if session.get('logged'):
        if request.method=="GET":
            return render_template("Bikes.html")
        else:
            bike=Bikes()
            bike.bikebrand=(request.form['bikebrand'])
            bike.bikeregno=(request.form['bikeregno'])
            bike.bikecc=int(request.form['bikecc'])
            bike.bikemileage=int(request.form['bikemileage'])
            bike.bikemodel=(request.form['bikemodel'])
            bike.bikelocation=(request.form['bikelocation'])
            bike.bikeownername=(request.form['bikeownername'])
            bike.bikeownerphone=int(request.form['bikeownerphone'])
            bike.bikeownercount=int(request.form['bikeownercount'])

            bike.save()
        
        return redirect("/list")
    else:
        return render_template("login.html")

@app.route("/nav")
def showHome():
    if session.get('logged'):
        return render_template("navigation.html")
    else:
        return render_template("login.html")

@app.route("/list")
def listAll():
    if session.get('logged'):
        collected=Bikes.objects.all()
        return render_template("view.html",data=collected)
    else:
        return render_template("login.html")
@app.route("/test")
def checkConnection():
    return jsonify(Bikes.objects.all())

@app.route("/shortlist",methods=['GET','POST'])
def performFilter():

    if session.get('logged'):
        if request.method=="GET":
            return render_template("filter.html")
        else:
            bikebrand=request.form['bikebrand']
            bikemodel=request.form['bikemodel']
            bikecc=request.form['bikecc']
            bikeownercount=request.form['bikeownercount']
            if bikebrand=="" and bikemodel!="" and bikecc=="" and bikeownercount=="Select Count":
                collected=Bikes.objects(bikemodel__iexact=bikemodel)
                return render_template("view.html",data=collected)
            elif bikebrand!="" and bikemodel=="" and bikecc=="" and bikeownercount=="Select Count":
                collected=Bikes.objects(bikebrand__startswith=bikebrand)
                return render_template("view.html",data=collected)
            elif bikebrand=="" and bikemodel=="" and bikecc=="" and bikeownercount!="Select Count":
                print("Count based "+bikeownercount)
                bikeownercount=int(bikeownercount)
                collected=Bikes.objects(bikeownercount__gte=bikeownercount)
                return render_template("view.html",data=collected)
            elif bikebrand=="" and bikemodel=="" and bikecc!="" and bikeownercount=="Select Count":
                bikecc=int(request.form['bikecc'])
                collected=Bikes.objects(bikecc__gte=bikecc)
                return render_template("view.html",data=collected)
            # elif bikebrand=="" and bikemodel=="Select Count" and bikecc=="" and bikeownercount!="":
            #     bikeownercount=int(bikeownercount)
            #     collected=Bikes.objects(bikeownercount__lte=bikeownercount)
            #     return render_template("view.html",data=collected)
            else:
                return render_template("filter.html")
    else:
        return render_template("login.html")
if __name__=="__main__":
    app.run(debug=True,port=2328)