from flask import Flask,request,render_template
import recommend as rc
import pickle
titles = pickle.load(open('./pickles/indices.pkl','rb'))

app = Flask('__name__')

@app.route('/')
def index():
    recommendations = rc.recommend('23:59',6)
    return render_template('index.html',
                           titles = titles)


@app.route('/recommend',methods=["POST"])
def recommend():
    rec = request.form['rec']
    recommend = rc.recommend(rec,6)
    return f"{recommend}"









if __name__=='__main__':
    Flask.run(debug=True)