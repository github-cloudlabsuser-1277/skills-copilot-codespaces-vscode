const data = [
    [{ name: 'John', age: 30 }, { name: 'Jane', age: 25 }],
    [{ name: 'Bob', age: 20 }]
];

const names = data.flat().map(person => person.name);

console.log(names); // ['John', 'Jane', 'Bob']