with open('src/pages/SchedulePage.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Испавить текст кнопки
content = content.replace("{hasActivePurchase ? 'Расписание� Ошибка' : 'Ошибка�� � Расписание'}", "{hasActivePurchase ? 'Подтвердить запись' : 'Оплатить и записаться'}")
content = content.replace(">Ошибка</Button>", ">Отмена</Button>")

with open('src/pages/SchedulePage.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done')
