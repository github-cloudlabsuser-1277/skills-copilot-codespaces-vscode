const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function calculate(expression) {
    try {
        const result = eval(expression);
        return result;
    } catch (error) {
        return 'Invalid expression';
    }
}

function promptUser() {
    rl.question('Enter an expression to calculate or type "exit" to quit: ', (input) => {
        if (input.toLowerCase() === 'exit') {
            rl.close();
        } else {
            const result = calculate(input);
            console.log(`Result: ${result}`);
            promptUser();
        }
    });
}

console.log('Simple Calculator');
promptUser();