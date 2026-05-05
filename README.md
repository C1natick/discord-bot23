# Discord Bot 24/7 🤖

Модерационный Discord бот, который работает 24/7 даже когда ваш ПК выключен.

## Функции

✅ **Автоматическая выдача ролей** - новичкам при входе выдаётся роль "🌱 Новичок"  
✅ **Команда /ban** - забанить участника с указанием причины  
✅ **Логирование** - все события логируются в консоль

## Быстрый старт на Replit (5 минут)

### 1️⃣ Получить Bot Token

1. Перейдите на [Discord Developer Portal](https://discord.com/developers/applications)
2. Нажмите **"New Application"** и дайте боту имя
3. Перейдите во вкладку **"Bot"** → **"Add Bot"**
4. В разделе **"TOKEN"** нажмите **"Copy"** (скопируется ваш токен)
5. Включите необходимые **Intents**:
   - ✅ **Server Members Intent**
   - ✅ **Guild Members Intent**

### 2️⃣ Развернуть на Replit

1. Перейдите на [Replit.com](https://replit.com)
2. Нажмите **"Create"** → **"Import from GitHub"**
3. Вставьте ссылку: `https://github.com/C1natick/discord-bot23`
4. Нажмите **"Import"**

### 3️⃣ Добавить Token

1. На странице Replit найдите кнопку **"Secrets"** (значок замка) слева
2. Создайте новую переменную:
   - **Key:** `DISCORD_BOT_TOKEN`
   - **Value:** `ваш_токен_из_discord_developer_portal`
3. Нажмите **"Add new secret"**

### 4️⃣ Запустить бота

Нажмите большую кнопку **"Run"** сверху - бот запустится и будет работать 24/7!

### 5️⃣ Добавить бота на сервер

1. На [Discord Developer Portal](https://discord.com/developers/applications) откройте ваше приложение
2. Перейдите во вкладку **"OAuth2"** → **"URL Generator"**
3. Выберите **Scopes:** `bot` + `applications.commands`
4. Выберите **Permissions:**
   - ✅ Manage Roles
   - ✅ Ban Members
   - ✅ Read Messages/View Channels
   - ✅ Send Messages
5. Скопируйте сгенерированную ссылку и откройте в браузере
6. Выберите сервер и нажмите **"Authorize"**

### 6️⃣ Настроить роль "🌱 Новичок"

1. На Discord сервере создайте роль **"🌱 Новичок"** (если её нет)
2. Убедитесь, что роль бота находится **выше** роли "🌱 Новичок" в иерархии
3. Готово! Новичкам будет автоматически выдаваться роль

## Альтернативные способы развертывания

### Railway 🚂 (бесплатный, требует GitHub)

1. Перейдите на [Railway.app](https://railway.app)
2. Нажмите **"New Project"** → **"Deploy from GitHub repo"**
3. Выберите репозиторий `discord-bot23`
4. Добавьте переменную окружения: `DISCORD_BOT_TOKEN=ваш_токен`
5. Разверните!

### Render ⚡ (бесплатный, требует GitHub)

1. Перейдите на [render.com](https://render.com)
2. Нажмите **"New +" → "Web Service"**
3. Подключите GitHub репозиторий
4. Выберите **Build Command:** `pip install -r requirements.txt`
5. Выберите **Start Command:** `python main.py`
6. Добавьте **Environment Variable:** `DISCORD_BOT_TOKEN=ваш_токен`
7. Разверните!

## Локальный запуск

```bash
# Установить зависимости
pip install -r requirements.txt

# Создать файл .env и добавить токен
echo "DISCORD_BOT_TOKEN=ваш_токен" > .env

# Запустить бота
python main.py
```

## Структура проекта

```
discord-bot23/
├── main.py              # Основной код бота
├── requirements.txt     # Зависимости Python
├── .replit             # Конфиг для Replit
├── Procfile            # Конфиг для Heroku/Railway/Render
├── .env.example        # Пример переменных окружения
└── README.md           # Этот файл
```

## Команды бота

### /ban
Забанить участника сервера
- `member` - участник для бана
- `reason` - причина (опционально)

Пример: `/ban @User Спам`

## Решение проблем

### ❌ Бот не работает
- Проверьте, что `DISCORD_BOT_TOKEN` правильно добавлен в Secrets (Replit) или Variables (Railway/Render)
- Убедитесь, что Intents включены в Discord Developer Portal
- Проверьте логи в консоли Replit

### ❌ Роль не выдаётся автоматически
- Убедитесь, что роль "🌱 Новичок" существует на сервере
- Проверьте, что название роли точно совпадает (с эмодзи)
- Убедитесь, что роль бота выше в иерархии

### ❌ Команда /ban не работает
- Убедитесь, что у вас есть права на бан участников
- Проверьте, что роль бота выше в иерархии удаляемого пользователя

## Лицензия

MIT

## Автор

[C1natick](https://github.com/C1natick)
