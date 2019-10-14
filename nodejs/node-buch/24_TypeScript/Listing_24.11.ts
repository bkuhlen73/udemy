class User {
  name: string;
  setName(name: string): void {
    this.name = name;
  }
}
const userA = new User();
userA.setName('Klaus');
const userB = new User();
userB.setName('Hans-Peter');

function compare(userA: User, userB: User): boolean {
  return userA.name === userB.name;
}

const cmp = (userA: User, userB: User): boolean => {
  return userA.name === userB.name;
};

console.log('compare: ', compare(userA, userB));
console.log('compare: ', cmp(userA, userB));
