// задание 1 

function getRange(start, end, step = 1) {
    let result = [];

    for (let i = start; i <= end; i += step) {
        result.push(i);
    }

    return result;
}

console.log(getRange(1, 10));
console.log(getRange(10, 30, 5));

// задание 2

function myReverse(text) {
    let result = "";

    for (let i = text.length - 1; i >= 0; i--) {
        result += text[i];
    }

    return result;
}

console.log(myReverse("123456789"));

// задание 3

function myReverse(text) {
    let result = "";

    for (let i = text.length - 1; i >= 0; i--) {
        result += text[i];
    }

    return result;
}

console.log(myReverse("123456789"));