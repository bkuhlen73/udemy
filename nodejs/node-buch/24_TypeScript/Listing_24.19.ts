class Movie {
  constructor(public id: number, public title: string, public year: number) {}
}

function show(movie: { title: string }) {
  console.log('Now showing: ', movie.title);
}

const infinityWar = new Movie(3, 'Avengers: Infinity War', 2018);

show(infinityWar);
