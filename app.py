from flask import Flask, render_template,request
import requests


app = Flask(__name__)
app.secret_key = 'secret123'

@app.route('/')
def index():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey=7e1737d3191d4fe894fc579df01b7bde"
    r= requests.get(url).json()
    case = {
        'articles': r['articles']
    }
    return render_template('index.html',cases = case)
@app.route('/sports')
def sports():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=7e1737d3191d4fe894fc579df01b7bde"
    r= requests.get(url).json()
    case = {
        'articles': r['articles']
    }
    return render_template('sports.html',cases = case)

@app.route('/business')
def business():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=7e1737d3191d4fe894fc579df01b7bde"
    r= requests.get(url).json()
    case = {
        'articles': r['articles']
    }
    return render_template('business.html',cases = case)

@app.route('/technology')
def technology():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=7e1737d3191d4fe894fc579df01b7bde"
    r= requests.get(url).json()
    case = {
        'articles': r['articles']
    }
    return render_template('tech.html',cases = case)

@app.route('/science')
def science():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=7e1737d3191d4fe894fc579df01b7bde"
    r= requests.get(url).json()
    case = {
        'articles': r['articles']
    }
    return render_template('science.html',cases = case)

@app.route('/health')
def health():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=7e1737d3191d4fe894fc579df01b7bde"
    r= requests.get(url).json()
    case = {
        'articles': r['articles']
    }
    return render_template('health.html',cases = case)
if __name__ == '__main__':
    app.run(debug=True)