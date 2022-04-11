from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key= 'sdfasfevgjkmjt'





@app.route('/')                           
def index():


    return render_template('index.html')



@app.route('/results')
def results():
    
    return render_template('results_index.html')








@app.route('/users', methods=["POST"])                           
def process_users():
    print(request.form)
    print(request.form['name'])
    print(request.form['locations'])
    print(request.form['favorite_language'])
    print(request.form['comment'])

    session['name'] = request.form['name']
    session['locations'] = request.form['locations']
    session['favorite_language'] = request.form['favorite_language']
    session['comment'] = request.form['comment']
    return redirect('/results')


















#============================================
#Reset Session to Empty
#============================================

@app.route("/destroy_session")
def destroy_session():
    session.clear()
    return redirect("/")












if __name__=="__main__":
    app.run(debug=True)