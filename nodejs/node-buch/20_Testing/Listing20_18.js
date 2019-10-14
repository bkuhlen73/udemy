describe('Negation', function() {
  it('should work in positive case', function() {
    expect('Node.js').toEqual('Node.js');
  });

  it('should work in negative case', function() {
    expect('Node.js').not.toEqual('jQuery');
  });
});
