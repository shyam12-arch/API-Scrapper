
# column: id,title,overview,release_date,popularity,vote_avg,vote_count
# size: 10557*7
# page: 528

import pandas as pd
import requests
import pymysql as sql


id = []
title = []
overview = []
release_date = []
popularity = []
vote_average = []
vote_count = []

for i in range(3):
    response = requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=103104b0c1097f8ad3a11f8add24e37d&language=en-US&page={i}')
    df = response.json()['results']

    for i in range(20):
        ids = df[i]['id']
        titles = df[i]['title']
        overviews = df[i]['overview']
        release_dates = df[i]['release_date']
        popularitys = df[i]['popularity']
        vote_averages = df[i]['vote_average']
        vote_counts = df[i]['vote_count']
#         print(ids)
#         print(titles)
#         print(overviews)
#         print(release_dates)
#         print(popularitys)
#         print(vote_averages)
#         print(vote_counts)

        con = sql.connect(host='localhost', user='root', passwd='Krish@4558$', database='manoj')
        cur = con.cursor()  # create object help in query execution

        # data insertion:
        cur.execute("insert into api values(%s,'%s','%s','%s',%s,%s,%s)"%(ids, titles, overviews, release_dates, popularitys, vote_averages, vote_counts))
        con.commit()  # for making parmanent change in table
        
--------------------------------------------------------------------------       
#         id.append(ids)
#         title.append(titles)
#         overview.append(overviews)
#         release_date.append(release_dates)
#         popularity.append(popularitys)
#         vote_average.append(vote_averages)
#         vote_count.append(vote_counts)

# create dictionary for convert above data into csv file format:

# dictionary = {'id': id, 'title': title, 'overview': overview, 'release_date': release_date, 'popularity': popularity, 'vote_average': vote_average, 'vote_count': vote_count}
# df = pd.DataFrame(dictionary)
# to_csv = df.to_csv('/Users/shyamtyagi/api.csv')

--------------------------------------------------------------------------

#     for getting perticular col info. :

#     ids = [d['id'] for d in df]
#     titles = [d['title'] for d in df]
#     overviews = [d['overview'] for d in df]
#     release_dates = [d['release_date'] for d in df]
#     popularitys = [d['popularity'] for d in df]
#     vote_avgs = [d['vote_average'] for d in df]
#     vote_counts = [d['vote_count'] for d in df]








