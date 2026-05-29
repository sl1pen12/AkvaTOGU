with open('src/pages/SchedulePage.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

import re
content = re.sub(r'\{hasActivePurchase \?.+?\}', '{hasActivePurchase ? \'Подтвердить запись\' : \'Оплатить и записаться\' }', content, flags=re.DOTALL)

with open('src/pages/SchedulePage.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done')
