import re

with open('src/pages/SchedulePage.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Исправить hasPaidRemainingForService на canUseRemaining (которая определена выше)
content = content.replace('if (activePurchase && hasPaidRemainingForService) {', 'if (activePurchase && canUseRemaining) {')

# 2. Убрать текст "Осталось занятий: 0" из модального окна, когда remaining == 0
# Вместо этого показывать только "Требуется оплата занятия" без счётчика
old_zero = '''                        <div>
                        <div className="flex items-center gap-2 mb-3">
                      <div className="p-2 bg-[#9c1d3b]/10 rounded-lg">
                        <Icon name="CreditCard" size={18} className="text-[#9c1d3b]" />
                      </div>
                      <div>
                        <p className="font-bold text-[#9c1d3b]">Осталось занятий: 0</p>
                        <p className="text-xs text-gray-600">Требуется оплата занятия</p>
                      </div>
                    </div>'''

new_zero = '''                        <div>
                    <div className="flex items-center gap-2 mb-3">
                      <div className="p-2 bg-[#9c1d3b]/10 rounded-lg">
                        <Icon name="CreditCard" size={18} className="text-[#9c1d3b]" />
                      </div>
                      <div>
                        <p className="font-bold text-[#9c1d3b]">Требуется оплата занятия</p>
                        <p className="text-xs text-gray-600">Выберите количество занятий для покупки</p>
                      </div>
                    </div>'''

content = content.replace(old_zero, new_zero)

with open('src/pages/SchedulePage.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Fixed!')
