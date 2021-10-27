def get_other_movies(movie_name):
    df_movie_users_series = ratings_movies.loc[ratings_movies['title']==movie_name]['userId']
    df_movie_users = pd.DataFrame(df_movie_users_series,columns=['userId'])
    other_movies = pd.merge(df_movie_users,ratings_movies,on='userId')
    other_users_watched = pd.DataFrame(other_movies.groupby('title')['userId'].count()).sort_values('userId',ascending=False)
    other_users_watched['perc_who_watched'] = round(other_users_watched['userId']*100/other_users_watched['userId'][0],1)
    return other_users_watched[:10]
  
  def recommend_movies():
  recom_movies=[]
  for mov in watched_movies:
      output = get_other_movies(mov)
      print(type(output))
      recom_movies = recom_movies + output   
 
  [print(i) for i in recom_movies]
  return recom_movies  
