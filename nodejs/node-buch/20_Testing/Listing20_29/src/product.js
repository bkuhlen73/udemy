function getCategories(data) {
  const categories = [];
  for (let i = 0; i < data.length; i++) {
    categories[data[i].category.position] = data[i].category.name;
  }
  return categories.filter(function() {
    return true;
  });
}

module.exports = { getCategories };
