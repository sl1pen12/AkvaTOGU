with open('src/pages/SchedulePage.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Заголовки и сообщения
content = content.replace("'Специализация��'", "'Запись'")
content = content.replace("`����� ${selectedSession.start_time", "`Время: ${selectedSession.start_time")
content = content.replace("`Всего мест��", "`Осталось мест: ${remaining}")
content = content.replace("title: 'Всего мест��!', description: `Всего мест�� Всего мест�:", "title: 'Успешно!', description: `Осталось мест:")
content = content.replace("title: 'Всего мест', description: bookResult.error || '�� Всего мест� Расписание'", "title: 'Ошибка', description: bookResult.error || 'Не удалось записаться'")
content = content.replace("title: 'Всего мест��� Всего мест'", "title: 'Запись'")
content = content.replace("`Всего мест�: ${category.name}", "`Абонемент куплен: ${category.name}")
content = content.replace("title: 'Всего мест�!', description: `Всего мест�: ${category.name}", "title: 'Успешно!', description: `Абонемент куплен: ${category.name}")
content = content.replace("title: 'Всего мест', description: error.message || '�� Всего мест� Абонемент активен�'", "title: 'Ошибка', description: error.message || 'Не удалось выполнить операцию'")
content = content.replace(">Всего мест<", ">Запись на сеанс<")
content = content.replace(">Всего мест��...<", ">Загрузка...<")
content = content.replace(">��� Всего мест�<", ">Сеансов нет<")
content = content.replace(">Всего мест �� �����<", ">Подтверждение записи<")
content = content.replace("��� Всего мест ����� Всего мест Всего мест���", "Информация о сеансе")
content = content.replace("Расписание - Расписание ���� ����� Всего мест", "Информация о сеансе")

with open('src/pages/SchedulePage.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done')
