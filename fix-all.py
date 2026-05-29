import re

with open('src/pages/SchedulePage.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Удалить блок выбора тарифа
content = re.sub(r'\{!activeTariffId \?\s*<div className="mb-4">.*?ALL_TARIFFS\.map\(\(tariff\) => \(.*?\)\)\s*</div>\s*</div>\s*\) : \{', '{', content, flags=re.DOTALL)

# 2. Заменить кнопки на радио
old_btn = """<button
                          key={idx}
                          onClick={() => setSelectedCategoryIndex(idx)}
                          className={'w-full p-3 rounded-lg border-2 transition-all text-left ' +
                            (selectedCategoryIndex === idx ? 'border-[#9c1d3b] bg-[#9c1d3b]/10' : 'border-gray-200 hover:border-[#9c1d3b]/50')}
                        >
                          <div className="flex items-center justify-between">
                            <span className="font-medium text-gray-900">{cat.name}</span>
                            <Badge variant={selectedCategoryIndex === idx ? 'default' : 'secondary'} className="text-base">
                              {cat.price}
                            </Badge>
                          </div>
                        </button>"""

new_radio = """<label
                          key={idx}
                          className={'w-full p-3 rounded-lg border-2 transition-all cursor-pointer ' +
                            (selectedCategoryIndex === idx ? 'border-[#9c1d3b] bg-[#9c1d3b]/10' : 'border-gray-200 hover:border-[#9c1d3b]/50')}
                        >
                          <div className="flex items-center gap-3">
                            <input
                              type="radio"
                              name="abonent"
                              checked={selectedCategoryIndex === idx}
                              onChange={() => setSelectedCategoryIndex(idx)}
                              className="w-4 h-4 text-[#9c1d3b]"
                            />
                            <div className="flex-1">
                              <span className="font-medium text-gray-900">{cat.name}</span>
                              <p className="text-xs text-gray-500 mt-0.5">
                                {cat.sessions === 1 ? 'Разовое посещение' : \`\${cat.sessions} занятий\`}
                              </p>
                            </div>
                            <Badge variant={selectedCategoryIndex === idx ? 'default' : 'secondary'} className="text-base shrink-0">
                              {cat.price}
                            </Badge>
                          </div>
                        </label>"""

content = content.replace(old_btn, new_radio)

# 3. Заменить текст
content = content.replace('Выберите абонемент для покупки:', 'Выберите абонемент (количество занятий):')

with open('src/pages/SchedulePage.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('All fixes applied!')
