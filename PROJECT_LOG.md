# PROJECT LOG

## Обзор проекта

Репозиторий `tus-synth-skins` предназначен для создания скинов для VST-синтезаторов компании **The Usual Suspects**.

Первый скин — **Simpless** для синтезатора **Xenia**. Расположен в папке `Simpless_Xenia`.

Общие идеи дизайна, распространяемые на все скины, описаны в `DESIGN.md`.

## Скин Simpless (Xenia)

### Автор
Vitalii Zenkov (KYOTO) — kyotochillout@gmail.com

### Версия
0.1

### Описание
Clean, minimal re-design интерфейса Xenia. Цель — спокойный, неперегруженный вид, при котором каждый элемент управления легко считывается. Вместо busy hardware-style графики — набор softly rounded панелей на тёмном фоне.

### Структура папки `Simpless_Xenia/`

| Файл / папка | Назначение |
|---|---|
| `README.txt` | Описание скина, авторские права, контакты, palette, compatibility, installation, font, inspiration, modifications |
| `Simpless.rml` | Разметка интерфейса (RML, 785 строк): корневое тело, все страницы (Osc, Mod, Arp/FX, Multi, Wave, Patch Manager), элементы управления и их позиции |
| `Simpless.rcss` | Таблица стилей (RCSS, 1027 строк): спрайт-листы, классы ручек, кнопок, светодиодов, выпадающих списков, цветовая палитра |
| `bgMain.png` | Фоновое изображение корневого окна (3352×2008) |
| `pgOsc.png`, `pgMod.png`, `pgArp.png`, `pgMulti.png`, `pgWave.png`, `pgPatchManager.png` | Фоновые изображения страниц |
| `kbMainBi*.png`, `kbMainKT*.png`, `kbMainUni*.png`, `kbRedUni*.png`, `kbWavetable*.png` | Спрайт-листы ручек (разные стили/размеры) |
| `lbPlayParams_page*.png` | Спрайт-лист больших ручек (octave/semi/quality) |
| `btBrowser.png` | Кнопка патч-менеджера |
| `btWaveEditor.png` | Кнопка волнового редактора |
| `buttonLEDclick.png` | Кнопки переключения страниц |
| `simp_button*.png` | Кнопки основного стиля (обычные, плюс/минус, красные плюс/минус, малые) |
| `led.png`, `ledMidi.png` | Светодиоды (обычные и MIDI) |
| `f1Type*.png` | Иконки типов фильтра F1 |
| `Gabarito-VariableFont_wght.ttf` | Шрифт Gabarito (SIL Open Font License) |
| `OFL-Gabarito.txt` | Лицензия шрифта Gabarito |

### Дизайн (из DESIGN.md / README.txt)

- **Внешний вид:** каждая секция (осцилляторы, волны, микшер, фильтры, обертки, модуляционные слоты и т.д.) на своей округлой панели с тёмной заголовком-вкладкой.
- **Ручки:** простые кремовые колпачки с тонкой тиковой обводкой, значение читается за один взгляд.
- **Текст:** тонкий, дружелюбный шрифт Gabarito.
- **Выпадающие списки и кнопки:** тот же округлый тёмный стиль.
- **Активные состояния:** красные светодиоды и кнопки.
- **Палитра:** мягкий медный-оранжевый для панелей (оттенок couleurs Xenia), кремовый текст/элементы, тёмная рамка вокруг всего окна, красный как единственный акцент для включённого.
- **Совместимость:** сохранены element IDs и структура, которые ожидает плагин, поэтому все страницы (Main, Mod, Arp/FX, Multi, Wave, Patch Manager) работают как в дефолтном скине; все контролы находятся там, где плагин их ищет.

### Установка
Положить папку `Simpless` в директорию `skins` плагина Xenia и выбрать "Simpless" в меню скинов.

### Классы стилей (Simpless.rcss)

Спрайт-листы: `btBrowser`, `kbMainBi_page0`, `kbMainKT_page0`, `kbMainUni_page0`, `kbRedUni_page0`, `kbWavetable_page0`, `lbPlayParams_page0`, `lbPlayParams_page1`, `ledMidi`, `led`, `buttonLEDclick`, `simp_button`, `simp_button_minus`, `simp_button_plus`, `simp_button_red_minus`, `simp_button_red_plus`, `simp_button_small`.

Классы UI: `.btBrowser`, `.knob`…`.knob5`, `.led`, `.ledMidi`, `.list`, `.grid`, `.pm-infopanel`, `.listentry`, `.gridentry`, `.pm-hlayout`, `.pm-info-headline`, `.pm-info-name`, `.pm-info-text`, `.pm-status`, `.pm-vlayout`, `.pm-count`, `.txt`, `.txt1`, `.txt2`, `.buttonLEDclick`, `.simp_button` (все варианты), `body`, `input.text`, скроллбары, `tree`, `treenode`.

### Страницы (Simpless.rml)

1. **Root / главное окно** — MIDI-LED, кнопки страниц (Main, Mod, Arp/FX, Multi, Wave, Patch Manager), Part Select (8 частей), Save, Multi Mode, Main Volume, 4 playing-parameter секции (knob1/knob2/knob3 варианты).
2. **pageOsc** (tabpage 0) — Oscillator 1/2, Wave 1/2, Mixer, Amplifier, Quality, Filters (F1/F2), Filter Envelope, LFOs 1/2, Amp Envelope.
3. **pageMod** (tabpage 2) — 16 Modulation Slots (Source/Dest/Amount), Free Envelope, Modifiers, Control Delay, Wave Envelope (8 стадий), Glide.
4. **pageArp** (tabpage 3) — Arpeggiator (Mode, Clock, Pattern, Direction, Order, Velocity, Tempo, Range, Reset), 16 пользовательских паттернов, Pattern Length, Effects (Chorus, Flanger, AutoWah, Overdrive, AmpMod, Delay), Glide, Detune, DePan, Play Parameters, Patch Parameters, Main Volume.
5. **pageMulti** (tabpage 4) — 8 мульти-частей (MI0…MI7): Transpose, Detune, Key Low/High, Velo Lo/Hi, Pan, Volume, Midi Channel, Output, Enabled.
6. **pageWave** (tabpage 5) — Wave Editor: Wave Tables, Wave Control Table, Waves, Wave Editor (Preview, Save, Frequency, Phase).
7. **pagePatchManager** (tabpage 1) — Part Select, Patch Manager, 8 частей с Volume/Pan, PatchName, контейнер patchmanager (template `patchmanager`).

### Ход работы

- `b83b338` — Add .gitignore
- `3eb587f` — Initial commit

В дальнейшем в этот файл будут вноситься записи о работе со всеми скинами проекта.

---

## 📋 UNIVERSAL SKIN PROMPT (используется для каждого нового скина)

> **Делаем скин Simpless для синтезатора `<НАЗВАНИЕ>` (The Usual Suspects).**
> **Приложены:** `DESIGN.md` (стиль, читать первым), `skin-kit.zip` (общие спрайты, шрифт, скрипты), исходный скин `<имя>.zip`.
>
> **Исходные данные:**
> - Цвет панелей: `<например, приглушённый цвет железа / hex>`
> - Логотип и названия секций: из исходного скина
> - Начни со страницы: `<Main / Osc / ...>`
>
> **Правила:**
> 1. Стиль строго по `DESIGN.md`: палитра, рамка 14 dp (сверху 24), зазоры 14 dp, Gabarito, `.txt` 24 dp / 400, красный без свечения.
> 2. Все id плагина (`xtKnob`, `xtButton`, `xtLed`, `dropdown` и т.д.) не менять, классы с префиксом `simp_`.
> 3. Регуляторы выравнивать по подписям: центр на 89 dp выше центра подписи.
> 4. Сдвигать элементы только по дереву (`tools/shift_toplevel.py`), не по отступам. Надписи на фоне с кольцами переносить через `tools/move_text.py`.
> 5. Работай по одной странице, показывай результат, дальше только после моего ответа.
> 6. Отвечай коротко, без длинных объяснений. Присылай только изменённые файлы, не весь архив.
> 7. В конце обнови `DESIGN.md` (журнал решений) и `README` шаблон из `skin-kit/template`.

---
