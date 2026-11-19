# HOWTORELEASE — Шпаргалка по созданию релиза Simpless

## Подготовка (один раз, перед первым релизом)

1. Убедиться, что в `.github/synth-map.yml` есть маппинг для синтезатора:
   ```yaml
   xenia: Simpless_Xenia
   # othersynth: Simpless_OtherSynth
   ```

2. Проверить, что workflow `.github/workflows/release.yml` работает (GitHub Actions включен в репо).

---

## Создание нового релиза (пошагово)

### 1. Подготовить нотесы и скрины

```bash
# Скопировать шаблон под новую версию
cp release/template.md release/xenia/v0.2.0.md

# Отредактировать release/xenia/v0.2.0.md:
# - Заголовок: # Simpless for Xenia v0.2.0 / # Simpless для Xenia v0.2.0
# - Заменить {AUTHOR} на своё имя (Vitalii Zenkov (KYOTO))
# - Заполнить раздел "What's New / Что нового"
# - Проверить пути установки (уже верные)
```

### 2. Добавить скриншоты (опционально, но рекомендуется)

```bash
# Положить скрины в папку (PNG/JPG)
# release/xenia/screenshots/main.png
# release/xenia/screenshots/osc.png
# release/xenia/screenshots/mod.png
# ...
# Имена файлов = alt-text в маркдауне (workflow вставит их автоматически)
```

> **Важно про ссылки на скриншоты:** workflow использует ссылки вида  
> `https://github.com/{repo}/blob/{sha}/release/{synth}/screenshots/{name}?raw=true`  
> **НЕ** используйте `raw.githubusercontent.com/...` — GitHub не отдаёт raw-контент для файлов в репозитории через этот домен (404). Нужно именно `github.com/.../blob/...?raw=true`.

### 3. Закоммитить изменения нотесов/скринов

```bash
git add release/xenia/v0.2.0.md release/xenia/screenshots/
git commit -m "Release notes for xenia/v0.2.0"
git push origin main
```

> **Важно:** нотесы и скрины должны быть в `main` **до** пуша тега, иначе workflow их не увидит.

### 4. Создать и запушить тег

```bash
# Формат тега: <synth>/v<version>
git tag xenia/v0.2.0
git push origin xenia/v0.2.0
```

### 5. Дождаться завершения GitHub Actions

- Зайти в **Actions** → workflow "Create Release" → ждать зелёной галочки (~1-2 мин).
- Релиз появится в **Releases**: `Simpless-Xenia-v0.2.0`
- Архив: `Simpless-Xenia-v0.2.0.zip` (внутри папка `Simpless/`)
- Body: из `release/xenia/v0.2.0.md`
- Скриншоты: загружены как assets и вставлены в описание

### 6. Проверить релиз на GitHub

- Открыть: `https://github.com/vitzen/tus-synth-skins/releases/tag/xenia/v0.2.0`
- Убедиться, что архив скачивается, структура правильная, тексты читаются.

---

## Типичные ошибки

| Ошибка | Причина | Решение |
|--------|---------|---------|
| Workflow failed: "Synth not found in synth-map.yml" | Нет записи в `.github/synth-map.yml` | Добавить `newsynth: Simpless_NewSynth` и пушнуть в main |
| Release notes пустые / дефолтные | Файл `release/xenia/v0.2.0.md` не закоммичен в main до тега | Сначала коммит нотесов, потом тег |
| Архив не создался / пустой | Неправильный `source_dir` в synth-map.yml | Проверить, что папка исходников существует |
| Скриншоты не вставились / битые картинки | Использован `raw.githubusercontent.com` вместо `github.com/.../blob/...?raw=true` | Workflow использует правильный формат, не меняйте ссылки вручную |

---

## Для нового синтезатора (например, "othersynth")

1. Создать папку исходников: `Simpless_OtherSynth/` (структура как `Simpless_Xenia/`)
2. Добавить в `.github/synth-map.yml`:
   ```yaml
   othersynth: Simpless_OtherSynth
   ```
3. Создать `release/othersynth/v0.1.0.md` (копия шаблона)
4. Создать `release/othersynth/screenshots/`
5. Тег: `git tag othersynth/v0.1.0 && git push origin othersynth/v0.1.0`

---

## Локальная проверка сборки архива (без GitHub)

```bash
python3 scripts/build_zip.py \
  --source-dir Simpless_Xenia \
  --synth xenia \
  --version v0.2.0 \
  --output-dir .
# Создаст Simpless-Xenia-v0.2.0.zip в корне
unzip -l Simpless-Xenia-v0.2.0.zip | head -20  # проверить структуру
rm Simpless-Xenia-v0.2.0.zip  # убрать тестовый архив
```

---

## Полезные ссылки

- Releases: https://github.com/vitzen/tus-synth-skins/releases
- Actions: https://github.com/vitzen/tus-synth-skins/actions
- Workflow файл: `.github/workflows/release.yml`
- Скрипт сборки: `scripts/build_zip.py`
- Маппинг синтезаторов: `.github/synth-map.yml`
- Шаблон нотесов: `release/template.md`