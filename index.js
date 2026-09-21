let counter = {
    value: 0,

    increase() {
        this.value++;
    },

    decrease() {
        this.value--;
    },

    reset() {
        this.value = 0;
    },

    render() {
        let counterElement = document.getElementById('counter');

        counterElement.textContent = this.value;

        if (this.value > 0) {
            counterElement.style.color = 'green';
        } else if (this.value === 0) {
            counterElement.style.color = 'gray';
        } else {
            counterElement.style.color = 'red';
        }
    }
};


function handleIncreaseClick() {
    counter.increase();
    counter.render();
}


function handleResetClick() {
    counter.reset();
    counter.render();
}


function handleDecreaseClick() {
    counter.decrease();
    counter.render();
}


document.getElementById('increase-btn').addEventListener('click', handleIncreaseClick);

document.getElementById('reset-btn').addEventListener('click', handleResetClick);

document.getElementById('decrease-btn').addEventListener('click', handleDecreaseClick);


// ЛОТО

function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);

    return Math.floor(Math.random() * (max - min + 1)) + min;
}


function generateLotto() {

    let numbersElement = document.getElementById('numbers');

    numbersElement.innerHTML = '';

    for (let i = 0; i < 6; i++) {

        let randomNumber = getRandomInt(1, 99);

        let number = String(randomNumber).padStart(2, '0');

        let circle = document.createElement('div');

        circle.classList.add('circle');

        circle.textContent = number;

        numbersElement.appendChild(circle);
    }
}


document.getElementById('generate-btn').addEventListener('click', generateLotto);
