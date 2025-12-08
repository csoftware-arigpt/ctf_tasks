# NetDiag | Secure Network Diagnostics

Веб сервис для проверки работы сервиса через `ping`

---

## Что сделано?

- **Эмуляция реальной утилиты диагностики:**  
  Приложение позволяет указать домен или IP, запускает системный `ping` и отображает «сырой» вывод утилиты в браузере.

- **Юзабилити для участников:**  
  Добавлены быстрые пресеты популярных хостов, индикатор текущей цели, аккуратный вывод stdout/stderr в «окне терминала».
  
---

## Как установить?


#### Подготовка окружения: установите Python 3

Для Debian/Ubuntu:

```bash
sudo apt update
sudo apt install python3 python3-venv
```

#### Настройка проекта: создайте виртуальное окружение и активируйте его

```bash
python3 -m venv venv
source venv/bin/activate      # Для Linux/MacOS
# venv\Scripts\activate       # Для Windows (cmd/PowerShell)
```

#### Установка зависимостей

```bash
pip install -r requirements.txt
```

#### Настройка флага

В каталоге проекта лежит файл `flag.txt` 
Задайте в нём нужный флаг в формате вашего CTF, например:

```text
CTF{your_custom_flag_here}
```

При развёртывании в контейнере этот файл копируется в `/flag.txt`, откуда его и предстоит извлечь.

#### Запуск

```bash
python3 app.py
```

По умолчанию Flask поднимает сервис на `0.0.0.0:5000`
Если хотите использовать порт `8080` измените запуск в `app.py`:

```python
app.run(host="0.0.0.0", port=8080, debug=False)
```

Тогда задание будет доступно по адресу:  
`http://0.0.0.0:8080`

---

## Применённая уязвимость в задаче

**Command Injection (OS Command Injection через `subprocess`)**

---

## Скриншоты

<img width="988" height="538" alt="image" src="https://github.com/user-attachments/assets/d9ed453d-e65c-46d7-8a8d-5162a6e21868" />


---

Happy Hacking! 

by [csoftware-arigpt](https://github.com/csoftware-arigpt)
