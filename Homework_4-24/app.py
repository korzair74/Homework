"""
Python Flask Movie App Homework

    CRUD Functionality

    id
    title
    year
    rating
    genre
    starring

Extra-Credit: Build a static front-end using flask's render_template method

"""

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=False)
    year = db.Column(db.String(100), unique =False)
    rating = db.Column(db.String(100), unique=False)
    starring = db.Column(db.String(160), unique=False)
    genre = db.Column(db.String(100), unique=False)
    def __init__(self, title, year, rating, starring, genre):
        self.title = title
        self.year = year
        self.rating = rating
        self.starring = starring 
        self.genre = genre 
        
class MovieScheme(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'year' 'rating', 'starring', 'genre')
movie_schema = MovieScheme()
movies_schema = MovieScheme(many=True)


@app.route('/movie', methods=['POST'])
def add_movie():
  title = request.json['title']
  year = request.json['year']
  rating = request.json['rating']
  starring = request.json['starring']
  genre = request.json['genre']
  new_movie = Movie(title, year, rating, starring, genre)

  db.session.add(new_movie)
  db.session.commit()

  movie = Movie.query.get(new_movie.id)
  return movie_schema.jsonify(movie)

@app.route('/movies', methods=['GET'])
def get_movies():
  all_movies = Movie.query.all()
  result = movies_schema.dump(all_movies)
  return jsonify(result)

@app.route('/movie/<id>', methods=["GET"])
def get_movie(id):
  movie = Movie.query.get(id)
  return movie_schema.jsonify(movie)


@app.route('/movie/<id>', methods=["PUT"])
def movie_update(id):
  movie = Movie.query.get(id)
  title = request.json['title']
  content = request.json['content']

  movie.title = title
  movie.content = content

  db.session.commit()
  return movie_schema.jsonify(movie)

@app.route('/movie/<id>', methods=["DELETE"])
def movie_delete(id):
  movie = Movie.query.get(id)
  db.session.delete(movie)
  db.session.commit()
  return "Movie was successfully Deleted"

  return

if __name__ == '__main__':
    app.run(debug=True)


