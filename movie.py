from flask import Flask,render_template,request
import name
from bs4 import BeautifulSoup as SOUP
import re
import requests as HTTP

app=Flask(__name__)

@app.route('/')
def method():
    return render_template('input.html')

@app.route('/home',methods=['POST','GET'])
def home1():
    emotion=request.form['mood']
    #emotion = input("Enter the emotion: ")
    a = name.main(emotion)
    string=''
    count = 0
    if(emotion == "Disgust" or emotion == "Anger"
                           or emotion=="Surprise"):
 
        for i in a:
 
            
            tmp = str(i).split('>;')
 
            if(len(tmp) == 3):
                string=string+':'+tmp[1][:-3]
 
            if(count > 13):
                break
            count += 1
    else:
        for i in a:
            tmp = str(i).split('>')
 
            if(len(tmp) == 3):
                string=string+':'+tmp[1][:-3]
 
            if(count > 11):
                break
            count+=1
    s=string.split(':')
    return render_template('out.html',string=s)


app.run(debug=True)