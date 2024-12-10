# Minecraft Server Status Bot

Telegram бот для отслеживания статуса Minecraft сервера. Показывает количество игроков онлайн и их никнеймы.

## Возможности бота

- Проверка статуса сервера (онлайн/оффлайн)
- Отображение количества игроков онлайн
- Список активных игроков
- Пересылка сообщений администратору
- Удобное управление через кнопки

## Описание
Telegram бот для отслеживания статуса Minecraft сервера. Бот позволяет пользователям легко проверять текущий онлайн на сервере, видеть список активных игроков и получать информацию о состоянии сервера.

## Основные функции
- Проверка онлайна: Показывает количество игроков онлайн и их никнеймы
- Статус сервера: Отображает текущий статус сервера (онлайн/оффлайн)
- Информация о сервере: Показывает максимальное количество слотов

## Установка

1. **Подготовка**
   - Установите Python 3.8 или выше

2. **Скачивание проекта**
   - Просто скачайте и распакуйте файлы


3. **Установка зависимостей**
   ```bash
   - pip install -r requirements.txt
   ```

4. **Настройка**
   - Создайте бота через [@BotFather](https://t.me/BotFather) и получите токен
   - Откройте файл `config.py` и заполните следующие параметры:
     ```python
     TELEGRAM_BOT_TOKEN = "ваш_токен_бота"
     MINECRAFT_SERVER_IP = "айпи_сервера"
     MINECRAFT_SERVER_PORT = "порт_сервера"  # обычно 25565
     ```

5. **Запуск**
   ```bash
   python bot.py
   ```

## Использование

1. **Команды бота**
   - `/start` - Начать работу с ботом
   - `/check` - Проверить статус сервера
   - `/heavymetal2` - Пасхалка

2. **Кнопки**
   - "О боте" - Информация о боте
   - "Проверить онлайн" - Статус сервера
   - "Heavy Metal" - Пасхалка

## Решение проблем

1. **Бот не запускается**
   - Проверьте правильность токена
   - Убедитесь, что все зависимости установлены
   - Проверьте права доступа к файлам

2. **Не работает проверка сервера**
   - Проверьте правильность IP и порта
   - Убедитесь, что сервер включен
   - Проверьте доступность порта

## Обновление


## Поддержка

По всем вопросам обращайтесь:
- funpay - https://funpay.com/users/2551770/
