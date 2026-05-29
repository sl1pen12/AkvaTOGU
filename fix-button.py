with open('src/pages/SchedulePage.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('{hasActivePurchase ? \'Отмена', '{hasActivePurchase ? \'Подтвердить запись\' : \'Оплатить и записаться\'')

with open('src/pages/SchedulePage.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done')
