describe('Spy', () => {
  let buffer;

  beforeEach(() => {
    buffer = Buffer.from('Hello World');
  });

  it("should track calls to 'toString'", () => {
    spyOn(buffer, 'toString');

    buffer.toString();

    expect(buffer.toString).toHaveBeenCalled();
  });

  it('should return a different result', () => {
    spyOn(buffer, 'toString').and.returnValue('Hello Node.js');

    const result = buffer.toString();

    expect(buffer.toString).toHaveBeenCalled();
    expect(result).toEqual('Hello Node.js');
  });
});
