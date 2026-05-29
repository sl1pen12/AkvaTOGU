with open('src/pages/SchedulePage.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Испавить текст "Ошибка" в разных местах
content = content.replace("Ошибка", "Расписание", 1)  # Только первое вхождение - заголовок секции
content = content.replace("Ошибка", "Всего мест")  # В карточках мест

# Испавить текст в карточке сессии
content = content.replace("Расписание Расписание", "Специализация", 1)
content = content.replace("Ошибка Расписание Ошибка Ошибка", "Запись спишет 1 занятие с абонемента", 1)

with open('src/pages/SchedulePage.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done')
