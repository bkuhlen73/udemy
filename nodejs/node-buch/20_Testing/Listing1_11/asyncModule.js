module.exports = function(success, message) {
  if (success) {
    return Promise.resolve(message);
  } else {
    return Promise.reject(message);
  }
};
