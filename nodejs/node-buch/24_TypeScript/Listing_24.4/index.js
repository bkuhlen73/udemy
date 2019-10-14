var Movie = /** @class */ (function () {
    function Movie(title, year) {
        this.title = title;
        this.year = year;
    }
    return Movie;
}());
function rateMovie(movie, rating) {
    movie.rating = rating;
}
var ironMan = new Movie('Iron Man', '2008');
rateMovie('Iron Man', 4);
