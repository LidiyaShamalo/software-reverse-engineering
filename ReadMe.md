# 🎯 RE & Crackme Solutions Archive

Репозиторий содержит отчеты (Writeups), результаты статического/динамического анализа и скрипты автоматизации, а также исследования в области безопасности (включая анализ уязвимостей ядра и разработку PoC).

## 📂 Структура репозитория

Репозиторий структурирован по целевым задачам. Внутри каждой директории находятся оригинальные бинарники, отчеты и приложения.

```text
.
├── ReadMe.md                        # Этот файл
│
├── 1_crackme1_by_br0ken/
│   └── CrackMe1/
│       ├── CrackMe#1.exe            # Исходный исполняемый файл
│       ├── CrackMe#1_mod.exe        # Пропатченная версия (Этап 3)
│       ├── report.md                # Технический отчет по решению
│       ├── scr_generate_serial.py   # Python-скрипт (Кейген для Этапа 2)
│       └── report_appendices/       # Скриншоты анализа для отчета
│
├── 1_crackme1_by_midi/
│   └── midicrkme1/
│       ├── crackme.exe              # Исходный исполняемый файл
│       ├── crackme_mod.exe          # Пропатченная версия
│       ├── report.md                # Технический отчет
│       └── report_appendices/       # Скриншоты анализа для отчета
│
├── 1_linux_crackme_02 by cyrex/
│   └── crackme_02/
│       ├── crackme.exe              # Исходный исполняемый файл
│       ├── report_linux.md          # Технический отчет по решению
│       └── report_appendices/       # Скриншоты анализа для отчета
│
├── 1_linux_crackme by cyrex/
│   └── crackme_01/
│       ├── crackme.exe              # Исходный исполняемый файл
│       ├── report_linux.md          # Технический отчет по решению
│       └── report_appendices/       # Скриншоты анализа для отчета
│
├── 1_nts_crackme3_by_cyclops/
│   └── NTS-Crackme3/
│       ├── Crackme3.exe             # Исходный исполняемый файл
|       ├── loader.py                # Скрипт для динамической модификации программы в памяти при запуске
|       ├── patcher.py               # Скрипт для статической модификации программы
│       ├── report.md                # Технический отчет по решению
│       └── report_appendices/       # Скриншоты анализа для отчета
│
├── cve-2019-2215_binder_uaf/        # Исследование Binder UAF (Android Kernel)
│   ├── README.md                    # Краткое описание работы
│   ├── cve-2019-2215_report.md      # Полный технический отчет
│   ├── exploit/                     # Исходники эксплойта (C)
│   ├── kernel_patch/                # Патч ядра и конфигурация сборки
│   └── images/                      # Скриншоты и иллюстрации
│
├── find_key/
│   └── zeromakespipi/
│       ├── ZeroMakesPiPi.exe        # Исходный исполняемый файл
│       ├── report.md                # Технический отчет
│       ├── mfc71/                   # Необходимые зависимости (DLL)
│       └── report_appendices/       # Скриншоты анализа для отчета
│
└── LTFFT_1/
    ├── LTFFT1.exe                   # Пропатченная версия
    ├── LTFFT.exe                    # Исходный исполняемый файл
    ├── report.md                    # Технический отчет
    └── report_appendices/           # Скриншоты анализа для отчета
```


## 📊 Список решенных задач

| Папка / Задача | Платформа / Архитектура | Инструменты | Статус | Основные уязвимости / Особенности |
| :--- | :---: | :---: | :---: | :--- |
| [`1_crackme1_by_br0ken`](./1_crackme1_by_br0ken/CrackMe1/report.md) | Windows / x86 | IDA Pro | 🟩 Cracked | Out-of-bounds Read & Write, Patching |
| [`1_crackme1_by_midi`](./1_crackme1_by_midi/midicrkme1/report.md) | Windows / x86 | IDA Pro | 🟩 Cracked | Изучение управляющей логики, Patching |
| [`find_key` (ZeroMakesPiPi)](./find_key/zeromakespipi/report.md) | Windows / x86 (MFC) | IDA Pro | 🟩 Cracked | Анализ MFC-обработчиков кнопок |
| [`LTFFT_1`](./LTFFT_1/report.md) | Windows / x86 | IDA Pro | 🟩 Cracked | Обход условных переходов, Поиск строк |
| [`1_linux_crackme_02_by_cyrex`](./1_linux_crackme_02_by_cyrex/report_linux.md) | Linux / x64 | IDA Pro | 🟩 Cracked | Hardcoded Key (Зашитый ключ), Специфические зависимости (Файловый триггер), Обнаружение Anti-Debugging (ptrace) |
| [`1_linux_crackme_by_cyrex`](./1_linux_crackme_by_cyrex/report_linux.md) | Linux / x64 | IDA Pro | 🟩 Cracked | Hardcoded Key (Зашитый ключ), Изучение управляющей логики, Статический анализ строк |
| [`1_nts_crackme3_by_cyclops`](./1_nts_crackme3_by_cyclops/report.md) | Windows / x86 | IDA Pro | 🟩 Cracked | Переполнение буфера (массива), Контроль целостности, Анализ условий (XREFs), Статический патчинг, Динамический Runtime-инжект (WinAPI) |

## 🔬 Kernel / Exploit Research

| Папка | Платформа | Инструменты | Статус | Особенности |
|-------|-----------|-------------|--------|-------------|
| [`cve-2019-2215_binder_uaf`](./cve-2019-2215_binder_uaf/cve-2019-2215_report.md) | Android / x86_64 (goldfish) | GDB, pahole | 🟩 Root obtained (LPE) | Binder UAF, снятие addr_limit, overwrite struct cred |

## 🛠️ Используемый инструментарий

* **Статический анализ и декомпиляция:** IDA Pro (запущена локально на Linux-хосте).
* **Анализ ядра и структур:** GDB (gdb-multiarch), утилита `pahole`.
* **Скриптинг / Кейгены:** Python 3 (эмуляция переполнения регистров и x86-логики), C (написание PoC).
* **Среда тестирования:** Изолированная песочница VirtualBox (гостевая Windows для запуска crackme), Android Virtual Device (AVD) для тестирования эксплойтов ядра.

## 📜 Правила ведения истории (Conventional Commits)

В репозитории применяется строгий формат именования коммитов для прозрачного логирования шагов:

* `feat(crackme_name):` — добавление нового таска, написание скриптов автоматизации или кейгенов.
* `docs(crackme_name):` — оформление, написание или обновление файла отчета (`report.md`).
* `mod(crackme_name):` — фиксация патчей, модифицированных исполняемых файлов или создание бэкапов.
* `feat(infra):` — добавление общих инструментов автоматизации, внешних библиотек или серверов отладки.

## ⚠️ Отказ от ответственности

Все материалы, отчеты и написанные скрипты созданы исключительно в **учебных и исследовательских целях** для развития навыков реверс-инжиниринга. Автор не несет ответственности за любое несанкционированное использование предоставленной информации.
