with open('src/pages/SchedulePage.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Испавить дни недели
content = content.replace("['��', '��', '��', '��', '��', '��', '��']", "['ВС', 'ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ']")

# Испавить месяцы
content = content.replace("['���', '���', '���', '���', '���', '���', '���', '���', '���', '���', '���', '���']", "['янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']")

# Испавить имена тренеров и специализации
content = content.replace("'Отмена �.�.'", "'Иванов А.С.'")
content = content.replace("'Отмена��'", "'Плавание'")

with open('src/pages/SchedulePage.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done')
