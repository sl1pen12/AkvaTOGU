with open('src/pages/SchedulePage.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

old = """            </div>

                    <div className="flex items-center gap-2 mb-3">"""

new = """            </div>

            <div className="mb-4">
              {hasActivePurchase ? (
                <div className="flex items-center gap-2 mb-3">"""

content = content.replace(old, new)

with open('src/pages/SchedulePage.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done')
