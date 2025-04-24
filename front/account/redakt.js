function editProfile() {
    const fullName = document.getElementById('fullName');
    const orgName = document.getElementById('orgName');
    const email = document.getElementById('email');
    const bonuses = document.getElementById('bonuses');
    const button = document.getElementById('editBtn');

    if (button.textContent === 'Редактировать профиль') {
        fullName.innerHTML = `<input type="text" id="inputName" value="${fullName.textContent}">`;
        orgName.innerHTML = `<input type="text" id="inputOrg" value="${orgName.textContent}">`;
        email.innerHTML = `<input type="email" id="inputEmail" value="${email.textContent}">`;
        bonuses.innerHTML = `<input type="text" id="inputBonuses" value="${bonuses.textContent}">`;
        button.textContent = 'Сохранить';
    } else {
        const updatedData = {
            fullName: document.getElementById('inputName').value,
            orgName: document.getElementById('inputOrg').value,
            email: document.getElementById('inputEmail').value,
            bonuses: document.getElementById('inputBonuses').value,
        };

        // Пример отправки на сервер (замени URL на свой)
        fetch('/update-profile', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(updatedData),
        }).then(response => response.json()).then(data => {
            fullName.textContent = updatedData.fullName;
            orgName.textContent = updatedData.orgName;
            email.textContent = updatedData.email;
            bonuses.textContent = updatedData.bonuses;
            button.textContent = 'Редактировать профиль';
        }).catch(error => {
            alert('Ошибка при сохранении 😿');
            console.error('Error:', error);
        });
    }
}