
import pickle

similarity_scores = pickle.load(open('./pickles/similarity_scores.pkl','rb'))
result_df = pickle.load(open('./pickles/result_df.pkl','rb'))
df_copy= result_df.copy()
df_copy.index = df_copy['title']
df_copy=df_copy['director']

def recommend(title,topn):
    index = df_copy.index.get_loc(title)
    indices = sorted(list(enumerate(similarity_scores[index])),key=lambda x:x[1], reverse=True)[:topn]
    indices = dict(indices)
    keys = list(indices.keys())
    recommend_df = result_df[result_df.index.isin(keys)]
    titles = []
    for i in keys:
        titles.append(recommend_df.loc[i,'title'])
    title_score = dict(zip(titles,indices.values()))
    recommend_df['score'] = recommend_df['title'].apply(lambda x:title_score[x])
    return recommend_df.sort_values(by='score',ascending=False)