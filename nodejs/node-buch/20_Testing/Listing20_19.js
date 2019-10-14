const customMatchers = {
  toHaveATitle() {
    return {
      compare(actual) {
        const result = {
          pass: actual.hasOwnProperty('title'),
        };

        if (result.pass) {
          result.message = `Expected ${actual} to have a title`;
        } else {
          result.message = `Expected ${actual} to have a title, but it didn't.`;
        }
        return result;
      },
    };
  },
};

describe('Custom Matchers', () => {
  beforeAll(() => {
    jasmine.addMatchers(customMatchers);
  });

  it('should have a title property', () => {
    const withTitle = { title: 'My Title' };
    expect(withTitle).toHaveATitle();
  });

  it('should fail without a title', () => {
    const withoutTitle = { name: 'no title' };
    expect(withoutTitle).toHaveATitle();
  });
});
