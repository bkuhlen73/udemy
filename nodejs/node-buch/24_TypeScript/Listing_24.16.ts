class Movie {
  rating: number;

  constructor(public id: number, public title: string, public year: number) {}
}

function rate(movie: Movie, rating: number): void {
  movie.rating = rating;
}

const ironMan = new Movie(1, 'Iron Man', 2008);

rate(ironMan, 4);
