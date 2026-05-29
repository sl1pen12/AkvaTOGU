with open('src/pages/SchedulePage.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Испавить оставшиеся проблемы
content = content.replace("`Осталось мест: ${remaining} Всего мест�: ${remaining}", "`Осталось мест: ${remaining}")
content = content.replace(". ����� ${selectedSession.start_time", ". Время: ${selectedSession.start_time")
content = content.replace(">���<", ">Показать все<")
content = content.replace(">�Абонемент активен<", ">Абонемент активен<")
content = content.replace("'��� ����'", "'Мест нет'")
content = content.replace("' ����'", "' мест'")

with open('src/pages/SchedulePage.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done')
