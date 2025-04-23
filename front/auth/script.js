document.getElementById('volunteerForm').addEventListener('submit', function(e) {
    e.preventDefault();
    clearErrors();

    // Получаем значения полей
    const fullName = document.getElementById('fullName').value.trim();
    const birthDate = document.getElementById('birthDate').value;
    const phone = document.getElementById('phone').value.trim();

    let isValid = true;

    // Валидация ФИО (минимум 2 слова)
    if (!fullName || fullName.split(' ').length < 2) {
        showError('fullNameError', 'Введите полное ФИО (минимум 2 слова)');
        isValid = false;
    }

    // Валидация даты рождения (возраст 14+ лет)
    if (!birthDate) {
        showError('birthDateError', 'Укажите дату рождения');
        isValid = false;
    } else {
        const today = new Date();
        const birthDateObj = new Date(birthDate);
        const age = today.getFullYear() - birthDateObj.getFullYear();
        if (age < 14) {
            showError('birthDateError', 'Волонтер должен быть старше 14 лет');
            isValid = false;
        }
    }

    // Валидация телефона (простая проверка на 11 цифр)
    const phoneRegex = /^\+?[0-9\s\-\(\)]{10,}$/;
    if (!phoneRegex.test(phone)) {
        showError('phoneError', 'Введите корректный номер телефона');
        isValid = false;
    }

    // Если все ок — отправляем данные
    if (isValid) {
        alert('Регистрация успешна! Данные:\nФИО: ' + fullName + '\nДата рождения: ' + birthDate + '\nТелефон: ' + phone);
        // Здесь можно отправить данные на сервер через fetch()
    }
});

function showError(id, message) {
    const errorElement = document.getElementById(id);
    errorElement.textContent = message;
}

function clearErrors() {
    const errors = document.querySelectorAll('.error');
    errors.forEach(error => {
        error.textContent = '';
    });
}