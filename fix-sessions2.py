with open('src/pages/SchedulePage.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Испавить TEST_SESSIONS
content = content.replace("'������ �.�.'", "'Иванов А.С.'")
content = content.replace("'������� �.�.'", "'Петрова М.И.'")
content = content.replace("'������� �.�.'", "'Сидоров В.П.'")
content = content.replace("'��������'", "'Плавание'")
content = content.replace("'�����������'", "'Акваэробика'")
content = content.replace("'������� ��������'", "'Детское плавание'")
content = content.replace("'�������� ��������'", "'Обучение плаванию'")
content = content.replace("'��������������� ��������'", "'Оздоровительное плавание'")

with open('src/pages/SchedulePage.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done')
