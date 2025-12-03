from flask import Flask, render_template, render_template_string

app = Flask(__name__)
app.static_folder = 'static'

cybersecurity_specialties = {
    "pentester": {
        "role_title": "Специалист по тестированию на проникновение",
        "core_focus": "Проактивное выявление уязвимостей",
        "key_competencies": ["Автоматизация (Python, Bash)", "OSINT", "Социальная инженерия", "Веб- и сетевые уязвимости"],
        "detailed_description": "Пентестер — это специалист по кибербезопасности, который занимается тестированием компьютерных систем, сетей и приложений на наличие уязвимостей. Его задача — имитировать кибератаки, найти слабые места в защите, получить доступ к закрытой информации и затем зафиксировать и сообщить о найденных проблемах, чтобы специалисты по безопасности могли устранить их.",
        "visual_representation": "static/hacker.png",
        "icon": "fa-user-secret"
    },
    "analyst": {
        "role_title": "SOC-аналитик",
        "core_focus": "Мониторинг и реагирование на угрозы",
        "key_competencies": ["Работа с SIEM-системами", "Анализ сетевого трафика (Wireshark)", "Расследование инцидентов", "Критическое мышление"],
        "detailed_description": "Аналитик безопасности отслеживает IT-инфраструктуру организации в режиме 24/7, выявляет аномальную активность и реагирует на киберинциденты.",
        "visual_representation": "static/soc.png",
        "icon": "fa-shield-halved"
    },
    "forensic": {
        "role_title": "Криминалист (Digital Forensics)",
        "core_focus": "Расследование киберинцидентов",
        "key_competencies": ["Reverse инжиниринг", "Юридические аспекты цифровых доказательств", "Анализ вредоносного ПО"],
        "detailed_description": "Криминалист расследует киберпреступления, анализируя данные с компьютеров, сетей и мобильных устройств. Восстанавливает удаленные или поврежденные данные, обеспечивает юридическую силу доказательств.",
        "visual_representation": "static/dfir2.png",
        "icon": "fa-magnifying-glass"
    }
}

def block_config(string):
    # Блокируем только config для обучения альтернативным SSTI техникам
    if "config" in string:
        return True
    return False

@app.route('/')
def index():
    render = render_template('index.html', specialties=cybersecurity_specialties)
    return render_template_string(render)

@app.route('/<specialty>')
def detail(specialty):
    specialty = specialty.lower()
    try:
        render = render_template('specialty_name.html', data=cybersecurity_specialties[specialty], specialty_key=specialty)
        return render_template_string(render)
    except:
        if block_config(specialty):
            return render_template('error.html')

        render = render_template('404.html', specialty=specialty)
        return render_template_string(render)

if __name__ == '__main__':
    import os
    debug_mode = os.environ.get('FLASK_ENV') != 'production'
    app.run(debug=debug_mode, host='0.0.0.0', port=5232)
