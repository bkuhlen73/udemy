var __extends = (this && this.__extends) || (function () {
    var extendStatics = Object.setPrototypeOf ||
        ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
        function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var Movie = /** @class */ (function () {
    function Movie(id, title, year) {
        this.id = id;
        this.title = title;
        this.year = year;
    }
    return Movie;
}());
var HorrorMovie = /** @class */ (function (_super) {
    __extends(HorrorMovie, _super);
    function HorrorMovie() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    return HorrorMovie;
}(Movie));
function show(movie) {
    console.log('Now showing: ', movie.title);
}
var shining = new HorrorMovie(1, 'The Shining', 1980);
show(shining);
