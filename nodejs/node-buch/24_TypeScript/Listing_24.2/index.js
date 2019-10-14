/*       */
class Movie {
                
               
                 
  constructor(title        , year        ) {
    this.title = title;
    this.year = year;
  }
}

function rateMovie(movie       , rating        ) {
  movie.rating = rating;
}

const ironMan        = new Movie('Iron Man', '2008');

rateMovie('Iron Man', 4);
