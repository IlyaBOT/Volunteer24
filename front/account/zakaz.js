document.addEventListener("DOMContentLoaded", function() {
    // Функция для загрузки данных о заказах с сервера
    async function fetchOrders() {
        try {
            const response = await fetch('/api/orders');  // Подставь сюда путь к твоему API
            if (!response.ok) {
                throw new Error('Ошибка загрузки данных');
            }
            const orders = await response.json();  // Преобразуем ответ в JSON
            populateOrders(orders);
        } catch (error) {
            console.error('Ошибка:', error);
        }
    }

    // Функция для создания блоков с заказами
    function populateOrders(orders) {
        const container = document.querySelector('#ordersContainer');
        container.innerHTML = ''; // Очищаем контейнер перед добавлением новых заказов

        // Проходим по каждому заказу и создаём блок
        orders.forEach(order => {
            const orderBlock = document.createElement('div');
            orderBlock.classList.add('order-block');

            orderBlock.innerHTML = `
                <h5>${order.partner_name}</h5>
                <p><strong>Email:</strong> ${order.partner_email}</p>
                <p><strong>Бонус за выполнение:</strong> ${order.bonus_description}</p>
                <button class="btn btn-primary" onclick="acceptOrder('${order.partner_name}')">Принять заказ</button>
            `;

            container.appendChild(orderBlock);
        });
    }

    // Функция для обработки принятия заказа
    function acceptOrder(partnerName) {
        alert(`Заказ от ${partnerName} принят!`);
        // Здесь можно добавить логику для обработки принятия заказа (например, отправить запрос на сервер)
    }

    // Загружаем заказы при загрузке страницы
    fetchOrders();
});