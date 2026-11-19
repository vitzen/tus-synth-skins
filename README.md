# Simpless — Skins for Modular Synthesizers

[![GitHub Release](https://img.shields.io/github/v/pitez/tus-synth-skins?label=release)](https://github.com/vitzen/tus-synth-skins/releases)
[![GitHub Actions](https://img.shields.io/github/actions/workflow/status/vitzen/tus-synth-skins/release.yml)](https://github.com/vitzen/tus-synth-skins/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/vitzen/tus-synth-skins/blob/main/LICENSE)

---

**Simpless** — это минималистичный скин для синтезаторов в стиле **The Usual Suspects** (Xenia и др.).

Дизайн: мягкие rounded-панели на тёмном фоне, muted copper-orange акценты (цвет Xenia hardware), cream текст, красный акцент.
Создан с любовью к аудио-интерфейсам и open-source культуре.

---

## 🎹 Для музыкантов

Simpless создан музыкантом и программистом, который ценит:
- **Чистый UI** — ничего лишнего, всё на месте
- **Тёмную тему** — удобно работать ночью
- **Наличие Gabarito шрифта** (SIL OFL) — читаемость и стиль
- **Полную совместимость** с дефолтным скином синтезатора

Скин меняет внешний вид интерфейса, но оставляет всё функционал на месте.

---

## 📦 Установка

1. Скачать архив `Simpless-<синтезатор>-<версия>.zip`
2. Распаковать — внутри папка **Simpless/**
3. Поместить в директорию скинов синтезатора:
   - **Windows**: `%APPDATA%\The Usual Suspects\<синтезатор>\skins\`
   - **macOS**: `~/Library/Application Support/The Usual Suspects/<синтезатор>/skins/`
     *(или иногда `~/Documents/The Usual Suspects/<синтезатор>/skins/`)*
4. Выбрать **Simpless** в меню скинов

---

## 📸 Скриншоты

Скриншоты из релизов доступны в соответствующем `release/<синтезатор>/`.

---

## 🛠 Для разработчиков

- Исходные файлы скинов лежат в папке `release/<синтезатор>/`
- Скрипт сборки: `scripts/build_zip.py`
- Маппинг синтезаторов: `.github/synth-map.yml`
- Workflow релиза: `.github/workflows/release.yml`
- Тег формата: `<synth>/v<version>` (например, `xenia/v0.1.0`)

---

## 💖 Поддержка

Если вам нравится эта работа, можете поддержать разработчика:

[![GitHub Sponsor](https://img.shields.io/badge/Support%20via%20GitHub%20Sponsor-%231DA1F2?logo=github-sponsors)](https://github.com/sponsors/vitzen)

---

## 📜 Лицензия

MIT — свободно, но с указанием авторства.

---

## 👤 Автор

**Vitalii Zenkov (KYOTO)** — full-stack developer и музыкант.
GitHub: [@vitzen](https://github.com/vitzen)
