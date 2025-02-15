# Docker Role

## Описание
Эта роль устанавливает и настраивает Docker и Docker Compose на Ubuntu системах.

## Требования
- Ansible 2.9+
- Ubuntu 24.04 (Noble)
- Права sudo на целевой машине

## Переменные роли

### Обязательные переменные
Нет обязательных переменных

### Опциональные переменные
```yaml
# Версия Docker для установки
docker_version: "latest"  # Текущая установленная: 27.5.1

# Версия Docker Compose для установки
docker_compose_version: "2.32.1"

# Пользователи для добавления в группу docker
docker_users:
  - "m7"
```

## Зависимости
Нет внешних зависимостей

## Пример использования

### Простой пример
```yaml
- hosts: all
  roles:
    - role: docker
```

### Расширенный пример
```yaml
- hosts: all
  become: true
  vars:
    docker_users:
      - "m7"
  roles:
    - role: docker
```

## Структура роли
```
docker/
├── defaults/
│   └── main.yml
├── handlers/
│   └── main.yml
├── tasks/
│   ├── main.yml
│   ├── install.yml
│   └── configure.yml
├── vars/
│   └── main.yml
└── README.md
```

## Выполняемые задачи
1. Установка необходимых зависимостей
2. Добавление Docker репозитория
3. Установка Docker (версия 27.5.1)
4. Установка Docker Compose (версия 2.32.1)
5. Настройка автозапуска Docker (systemctl enable docker)
6. Добавление пользователя в группу docker
7. Проверка установки

## Тестирование роли
```bash
# Проверка синтаксиса
ansible-playbook ansible/playbooks/dev/main.yaml --syntax-check

# Пробный запуск
ansible-playbook ansible/playbooks/dev/main.yaml --check -K

# Применение изменений
ansible-playbook ansible/playbooks/dev/main.yaml -K
```