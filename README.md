# movies
REST API which provides information about movies

demo: \
 https://movie-api-demo.herokuapp.com/movies/ \
      https://movie-api-demo.herokuapp.com/comments/

to run:
1) clone following repository https://github.com/mssliw/movies.git \
   and install requirements by running:
   >> pip install -r requirements.txt
   
2) create postgresql database on your local machine by running: 
    >> psql 
    
    and then creating db:
    >> CREATE DATABASE movies;
    
3) run migrations by following command: 
    >> python manage.py migrate

4) start API by running: 
    >> python manage.py runserver

5) go to localhost:8000

You will be able to create new movie record in your database by sending post request (title is required).



Functionalities of API:

>>localhost:8000/movies 

lists all movies existing in your database

>>localhost:8000/movies/title  

returns details of movie with title you typed (if it exists in database)

>>localhost:8000/comments 

lists  comments existing in database

>>localhost:8000/comments/id 

lists all comments for typed id of the movie
