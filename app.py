from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/gallery')
def anime():
    return render_template('gallery.html')  

@app.route('/artwork')
def artwork():
    return render_template('artwork.html') 

@app.route('/letter')
def letter():
    return render_template('letter.html') 

if __name__ == '__main__':
    app.run(debug=True)
