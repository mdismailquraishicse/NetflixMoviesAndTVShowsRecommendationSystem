from flask import Flask,request,render_template,url_for
import recommend as rc
import pickle
titles = pickle.load(open('./pickles/indices.pkl','rb'))
result_df = pickle.load(open('./pickles/result_df.pkl','rb'))


app = Flask('__name__')

@app.route('/')
def index():
    recommendations = rc.recommend('23:59',3)
    return render_template('index.html',
                           titles = titles)


@app.route('/recommend',methods=["POST"])
def recommend():
    rec = request.form['rec']
    recommend = rc.recommend(rec,13)
    return render_template("recommendation.html",
                           recommend=recommend,
                           titles=list(recommend['title']))

@app.route('/details/<index>')
def details(index):
    details=result_df.loc[int(index)]
    return render_template("details.html",
                           df=details)









if __name__=='__main__':
    Flask.run(debug=False)