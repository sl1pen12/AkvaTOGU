with open('src/pages/SchedulePage.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Испавить все имена тренеров
content = content.replace("'Отмена� �.�.'", "'Петрова М.И.'")
content = content.replace("'Отмена� �.�.'", "'Сидоров В.П.'")

# Испавить специализации
content = content.replace("'Отмена�����'", "'Акваэробика'")
content = content.replace("'Отмена� Отмена��'", "'Детское плавание'")
content = content.replace("'Отмена��'", "'Обучение плаванию'")

with open('src/pages/SchedulePage.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done')
