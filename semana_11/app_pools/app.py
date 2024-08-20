from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


results = {
    "Python": 0,
    "JavaScript": 0,
    "Java": 0,
    "Go": 0,
    "C#":0
}



@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        choice = request.form.get('language')
        
        if choice in results:
            results[choice] +=1
            print(results)
            
           
   
    return render_template('index.html', resultado=results)



if __name__ == '__main__':
    app.run(debug=True)