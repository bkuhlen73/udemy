interface Movie {
  id: number;
  title: string;
  year: number;
  rating: number;
  rate(rating: number): void;
}

class ActionMovie implements Movie {
  public rating: number;
  constructor(public id: number, public title: string, public year: number) {}
  rate(rating: number) {
    this.rating = rating;
  }
}

function show(movie: Movie) {
  console.log('Now showing: ', movie.title);
}

const infinityWar = new Movie(3, 'Avengers: Infinity War', 2018);
show(infinityWar);
