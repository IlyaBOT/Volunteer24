
function editProfile() {
    const button = document.getElementById('editBtn');

    if (button.textContent === 'Редактировать профиль') {
        document.getElementById('fullName').innerHTML = `<input type="text" id="inputName" value="${document.getElementById('fullName').textContent}">`;
        document.getElementById('email').innerHTML = `<input type="email" id="inputEmail" value="${document.getElementById('email').textContent}">`;
        document.getElementById('inn').innerHTML = `<input type="text" id="inputINN" value="${document.getElementById('inn').textContent}">`;
        document.getElementById('phone').innerHTML = `<input type="text" id="inputPhone" value="${document.getElementById('phone').textContent}">`;
        document.getElementById('dob').innerHTML = `<input type="text" id="inputDOB" value="${document.getElementById('dob').textContent}">`;
        button.textContent = 'Сохранить';
    } else {
        const updatedData = {
            fullName: document.getElementById('inputName').value,
            email: document.getElementById('inputEmail').value,
            inn: document.getElementById('inputINN').value,
            phone: document.getElementById('inputPhone').value,
            dob: document.getElementById('inputDOB').value,
            bonuses: document.getElementById('inputBonuses').value,
        };

        fetch('/update-profile', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(updatedData),
        }).then(response => response.json()).then(data => {
            document.getElementById('fullName').textContent = updatedData.fullName;
            document.getElementById('email').textContent = updatedData.email;
            document.getElementById('inn').textContent = updatedData.inn;
            document.getElementById('phone').textContent = updatedData.phone;
            document.getElementById('dob').textContent = updatedData.dob;
            button.textContent = 'Редактировать профиль';
        }).catch(error => {
            alert('Ошибка при сохранении ');
            console.error('Ошибка:', error);
        });
    }
}

