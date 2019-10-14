class Movie {
  rating: number;

  constructor(public id: number, public title: string, public year: number) {}

  rate(rating: number): void {
    this.rating = rating;
  }
}

const ironMan = new Movie(1, 'Iron Man', 2008);

ironMan(4);
