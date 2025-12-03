# Neon Corp | Secure Login

Симуляция защищенной корпоративной панели входа с "самописным" WAF.

## Что сделано?

-   **Современный интерфейс:** Реализована тема Cyberpunk/Neon с использованием Bootstrap 5 и кастомного CSS.
-   **Логика WAF:** Реализован фильтр, блокирующий комментарии и ключевые слова в нижнем регистре, требующий обхода.

## Как установить?

1. **Разверните минимальный Docker контейнер**

2.  **Подготовка окружения :**
    Установите Python 3
    ```bash
    sudo apt update
    sudo apt install python3 python3-venv
    ```

3.  **Настройка проекта :**
    Создайте виртуальное окружение и активируйте его
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Для Linux/Mac
    # venv\Scripts\activate   # Для Windows
    ```

4.  **Установка зависимостей :**
    Установите зависимости
    ```bash
    pip install -r requirements.txt
    ```

5.  **Настройка флага :**
    Откройте файл `config.py` и измените значение переменной `FLAG`
    ```python
    FLAG = "CTF{your_custom_flag_here}"
    ```

6.  **Запуск :**
    Запустите сервер
    ```bash
    python3 app.py
    ```
    Задача будет доступна по адресу: `http://0.0.0.0:8080`

## Примененная уязвимость в задаче

**SQL Injection (Union-Based + WAF Bypass)**

## Скриншоты

<img width="1220" height="751" alt="image" src="https://github.com/user-attachments/assets/60de16cd-d057-418c-91a7-4e575feac1c8" />


## **Happy Hacking!**

by [csoftware-arigpt](https://github.com/csoftware-arigpt)
