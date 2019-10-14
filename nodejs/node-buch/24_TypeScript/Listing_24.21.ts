class Movie {
  constructor(public id: number, public title: string, public year: number) {}
}

class Collection<T> {
  private items: T[] = [];

  public add(item: T): void {
    this.items.push(item);
  }

  public getAll(): T[] {
    return this.items;
  }
}

const myMovies = new Collection<Movie>();

myMovies.add(new Movie(1, 'Iron Man', 2008));
console.log(myMovies.getAll());
