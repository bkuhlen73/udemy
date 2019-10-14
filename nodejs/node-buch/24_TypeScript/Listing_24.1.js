class Movie {
  constructor(title, year) {
    if (typeof title !== 'string' || typeof year !== 'number') {
      throw new TypeError('Wrong types supplied');
    }
    this.title = title;
    this.year = year;
  }
}

function rateMovie(movie, rating) {
  if (!(movie instanceof Movie) || typeof rating !== 'number') {
    throw new TypeError('Wrong types supplied');
  }
  movie.rating = rating;
}

const ironMan = new Movie('Iron Man', '2008');

rateMovie('Iron Man', 4);
