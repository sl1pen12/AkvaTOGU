import re

with open('src/pages/SchedulePage.tsx.bak', 'r', encoding='utf-8-sig') as f:
    content = f.read()

# Найти и удалить блок выбора тарифа
pattern = r'\{!activeTariffId \?\s*<div className="mb-4">\s*<p className="text-sm text-gray-600 mb-2 flex items-center gap-1">\s*<Icon name="Ticket" size=\{14\} />\s*Выберите тариф для записи:\s*</p>\s*<div className="space-y-1 max-h-40 overflow-y-auto">\s*\{ALL_TARIFFS\.map\(\(tariff\) => \(\)\s*<button\s*key=\{tariff\.id\}\s*onClick=\{\(\) => handleTariffSelectFromModal\(tariff\.id\)\}\s*className="w-full p-3 rounded-lg border-2 border-gray-200 hover:border-\[\#9c1d3b\] hover:bg-\[\#9c1d3b\]/5 text-left transition-all"\s*>\s*<span className="font-semibold text-gray-900">\$\{tariff\.name\}</span>\s*</button>\s*\)\)\s*</div>\s*</div>\s*\) : \('
replacement = '{'
content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# Заменить текст
content = content.replace('Выберите абонемент для покупки:', 'Выберите абонемент (количество занятий):')

with open('src/pages/SchedulePage.tsx', 'w', encoding='utf-8-sig') as f:
    f.write(content)

print('Fixed!')
