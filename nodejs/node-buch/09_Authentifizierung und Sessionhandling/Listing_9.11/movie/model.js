const sqlite = require('sqlite3');
const db = new sqlite.Database('./movie.db');

function getAll(userId) {
  return new Promise((resolve, reject) => {
    const query = `SELECT Movies.*, count(Ratings.rating) AS numOfRatings, sum(Ratings.rating) as sumOfRatings, r.rating as userRating 
    FROM Movies 
    LEFT JOIN Ratings ON Movies.id = Ratings.movie 
    LEFT JOIN Ratings AS r ON Movies.id = r.movie AND r.user = ? 
    WHERE Movies.user = ? OR public = 1
    GROUP BY Movies.id;`;
    db.all(query, [userId, userId], (error, results) => {
      if (error) {
        console.log(error);
        reject(error);
      } else {
        resolve(results);
      }
    });
  });
}

function getOne(id, userId) {
  return new Promise((resolve, reject) => {
    const query =
      'SELECT * FROM Movies WHERE id = ? AND (user = ? OR public = 1)';
    db.get(query, [id, userId], (error, results) => {
      if (error) {
        reject(error);
      } else {
        resolve(results);
      }
    });
  });
}

function insert(movie, userId) {
  return new Promise((resolve, reject) => {
    const query =
      'INSERT INTO Movies (title, year, public, user) VALUES (?, ?, ?, ?)';
    db.run(
      query,
      [movie.title, movie.year, movie.public, userId],
      (error, result) => {
        if (error) {
          reject(error);
        } else {
          const query = 'SELECT last_insert_rowid()';
          db.get(query, (error, result) => {
            if (error) {
              reject(error);
            } else {
              movie.id = result;
              resolve(movie);
            }
          });
        }
      },
    );
  });
}

function update(movie, userId) {
  return new Promise((resolve, reject) => {
    const query =
      'UPDATE Movies SET title = ?, year = ?, public = ?, user = ? WHERE id = ?';
    db.run(
      query,
      [movie.title, movie.year, movie.public, userId, movie.id],
      (error, results) => {
        if (error) {
          console.log(error);
          reject(error);
        } else {
          resolve(results);
        }
      },
    );
  });
}

function remove(id, userId) {
  return new Promise((resolve, reject) => {
    const query =
      'DELETE FROM Movies WHERE id = ? AND (user = ? OR public = 1)';
    db.run(query, [id, userId], (error, results) => {
      if (error) {
        reject(error);
      } else {
        resolve(results);
      }
    });
  });
}

function rate(rating) {
  return new Promise((resolve, reject) => {
    const query = 'DELETE FROM Ratings WHERE movie = ? AND user = ?';
    db.run(query, [rating.movie, rating.user], error => {
      if (error) {
        reject(error);
      } else {
        const query =
          'INSERT INTO Ratings (movie, user, rating) VALUES (?, ?, ?)';
        debugger;
        db.run(query, [rating.movie, rating.user, rating.rating], error => {
          if (error) {
            reject(error);
          } else {
            resolve();
          }
        });
      }
    });
  });
}

module.exports = {
  getAll,
  get(id, userId) {
    return getOne(id, userId);
  },
  delete(id, userId) {
    return remove(id, userId);
  },
  save(movie, userId) {
    if (!movie.id) {
      return insert(movie, userId);
    } else {
      return update(movie, userId);
    }
  },
  rate,
};
