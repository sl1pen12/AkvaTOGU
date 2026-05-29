# Запуск приложения в Android Studio

## Требования

| Компонент | Версия |
|-----------|--------|
| Node.js | 18+ |
| JDK | **17** или **21** (Capacitor 8 внутри использует Java 21; в Android Studio: Settings → Build → Gradle → Gradle JDK) |
| Android Studio | Ladybug или новее |
| Android SDK | API **36**, минимум API **24** |

Проект уже настроен: Gradle **8.14.3**, AGP **8.13.0**, Capacitor **8**.

## Быстрый старт

### 1. Собрать веб-часть и синхронизировать с Android

В корне проекта (PowerShell или CMD):

```bat
npm install
npm run cap:sync
```

Или двойной щелчок по **`sync-android.bat`**.

### 2. Открыть в Android Studio

- **File → Open** → выберите папку **`android`** (не корень репозитория).
- Дождитесь синхронизации Gradle (может занять несколько минут при первом запуске).
- **Gradle JDK:** Settings → Build, Execution, Deployment → Build Tools → Gradle → **JDK 17**.

### 3. Запуск на эмуляторе или телефоне

1. Создайте AVD (Device Manager): API 34+ рекомендуется.
2. В Android Studio: **Run ▶** на модуле **app**.

По умолчанию приложение использует API на **Render**: `https://pool-backend-nmuz.onrender.com` (см. `src/config/api.ts`).

Для локального Flask на ПК перед сборкой задайте переменную и синхронизируйте:

```bat
set VITE_API_BASE_URL=http://10.0.2.2:5000
npm run cap:sync
```

(на реальном устройстве вместо `10.0.2.2` — IP вашего ПК в Wi‑Fi).

## Полезные команды

```bat
npm run cap:sync      :: build + cap sync android
npm run android:open  :: открыть проект в Android Studio
cd android
gradlew.bat assembleDebug   :: сборка APK из командной строки
```

## Структура

```
mobile-app-creation-2-main/
├── dist/                 ← веб-сборка (после npm run build)
├── android/              ← открывать ЭТУ папку в Android Studio
│   ├── app/
│   ├── variables.gradle
│   └── gradle/wrapper/
├── capacitor.config.ts
└── src/
```

## Частые проблемы

**Gradle sync failed / Java version**  
Установите JDK 17 или 21 и выберите его в Gradle JDK.

**Unable to delete directory ... build** (все 10 ошибок с одной причиной)

1. **Полностью закройте Android Studio** (File → Exit).
2. Запустите в корне проекта: **`clean-android-build.bat`** (двойной щелчок).
3. Запустите **`sync-android.bat`**.
4. Снова откройте папку `android` в Android Studio → **Build → Rebuild Project**.

Вручную из терминала:
```bat
cd android
gradlew.bat --stop
cd ..
clean-android-build.bat
```

Дополнительно:
- Не держите проект в **OneDrive** / облачной синхронизации — папки блокируются.
- Временно отключите антивирус для папки `android\app\build` или добавьте исключение.
- Не запускайте сборку из Studio и из терминала **одновременно**.

**Белый экран**  
Выполните `npm run cap:sync` — в `android/app/src/main/assets` должна появиться папка `public` с `index.html`.

**Нет связи с сервером на эмуляторе**  
Backend должен слушать `0.0.0.0:5000`, быть запущен на ПК; в приложении используется `10.0.2.2`, не `localhost`.

**google-services.json**  
Не обязателен. Без файла push не работает, приложение собирается нормально.
