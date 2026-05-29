with open('src/pages/SchedulePage.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Испавить все оставшиеся "Всего мест" в сообщениях
content = content.replace("Всего мест�� Всего мест�:", "Осталось мест:")
content = content.replace("title: 'Всего мест��!', description: `Осталось мест:", "title: 'Успешно!', description: `Осталось мест:")
content = content.replace("title: 'Всего мест�!', description: `Абонемент куплен:", "title: 'Успешно!', description: `Абонемент куплен:")
content = content.replace(">Всего мест<", ">Запись на сеанс<")
content = content.replace("��� Расписание", "Абонемент активен")
content = content.replace(">Расписание<", ">Всего занятий<")
content = content.replace("Расписание��:", "Использовано:")

with open('src/pages/SchedulePage.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done')
