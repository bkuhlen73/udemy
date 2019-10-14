class Movie {
  constructor(public id: number, public title: string, public year: number) {}
}
class HorrorMovie extends Movie {
  type: 'Horror';
}

function show(movie: Movie) {
  console.log('Now showing: ', movie.title);
}

const shining = new HorrorMovie(1, 'The Shining', 1980);

show(shining);
