import requests, sys
movie_name = ''
op = sys.argv


if len(op) > 3 and op[1] == 'movie':
    movie_name = ' '.join(op[2:])

else:
    print('Please enter correct operation')
# try:
#     op = sys.argv
#     lazimsiz = op[1]
#     movie_name = " ".join(op[1:])
# except:
#     print('Please enter correct operation')


if movie_name:
    url = f'http://www.omdbapi.com/?t={movie_name}&apikey=9c94b45d'
    try:
        response = requests.get(url)
        response_json = response.json()

        print(f'\nTitle : {response_json["Title"]}\nYear : {response_json["Year"]}\nReleased : {response_json["Released"]}\nGenre : {response_json["Genre"]}\nDirector : {response_json["Director"]}\n')
    except:
        print('Movie not found')