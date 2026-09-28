let users = [
    {
        login: "samina",
        password: "12345",
        name: "Samina"
    },
    {
        login: "alex",
        password: "11111",
        name: "Alex"
    },
    {
        login: "Amira",
        password: "22222",
        name: "Amira"
    },
    {
        login: "anna",
        password: "33333",
        name: "Anna"
    },
    {
        login: "Odina",
        password: "44444",
        name: "Odina"
    },
    {
        login: "Ipara",
        password: "admin123",
        name: "Admin"
    }
];

let loginInput = document.querySelector('#loginInput');
let passwordInput = document.querySelector('#passwordInput');
let loginButton = document.querySelector('#loginButton');
let message = document.querySelector('#message');

let loginUser = () => {
    let login = loginInput.value.trim();
    let password = passwordInput.value.trim();

    let user = users.find(user => 
        user.login === login && user.password === password
    );

    if (user) {
        message.innerHTML = `lобро пожаловать босс, ${user.name}вы самая лучшая!`;
        message.style.background = "#dcfce7";
        message.style.color = "#166534";s
    } else {
        message.innerHTML = "Неверный логин или пароль повелитель";
        message.style.background = "#fee2e2";
        message.style.color = "#991b1b";
    }
};

loginButton.addEventListener("click", loginUser);