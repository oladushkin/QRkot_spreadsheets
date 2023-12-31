# QRKot

## Описание
Фонд собирает пожертвования на различные целевые проекты.  

### Проекты
В Фонде может быть открыто несколько целевых проектов. У каждого проекта есть название,  
описание и сумма, которую планируется собрать. После того, как нужная сумма собрана — проект закрывается.  
Пожертвования в проекты поступают по принципу First In, First Out: все пожертвования идут в проект,  
открытый раньше других; когда этот проект набирает необходимую сумму  
и закрывается — пожертвования начинают поступать в следующий проект.  

### Пожертвования
Каждый пользователь может сделать пожертвование и сопроводить его комментарием.  
Пожертвования не целевые: они вносятся в фонд, а не в конкретный проект.  
Каждое полученное пожертвование автоматически добавляется в первый открытый проект,  
который ещё не набрал нужную сумму. Если пожертвование больше нужной суммы или же в  
Фонде нет открытых проектов — оставшиеся деньги ждут открытия следующего проекта.  
При создании нового проекта все неинвестированные пожертвования автоматически вкладываются в новый проект.  

### Пользователи
Целевые проекты создаются администраторами сайта.  
Любой пользователь может видеть список всех проектов, включая требуемые  
и уже внесенные суммы. Это касается всех проектов — и открытых, и закрытых.  
Зарегистрированные пользователи могут отправлять пожертвования и просматривать список своих пожертвований. 

### Отчеты Google
Приложение QRKot есть возможность формирования отчёта в гугл-таблице.  
В таблице выведены закрытые проекты, отсортированные по скорости сбора средств — от тех,  
что закрылись быстрее всего, до тех, что долго собирали нужную сумму.
---

## Установка
1. Скачивать репозиторий.  
`git@github.com:oladushkin/cat_charity_fund.git`
2. Установить виртуальное окружение.
`python -m venv venv`
3. Активировать окружение.
`. venv/Scripts/activate`
4. Установка зависимостей.
`pip install -r requirements.txt`
5. Заполнить переменные окружения (env.example).
6. Создание БД.
`alembic upgrade head`
7. Запуск приложения.
`uvicorn app.main:app `
---

## Инструменты
- Python 3.9
- FastAPI
- SQLAlchemy
---

## Автор

Шелепин Дмитрий|[GitHub](https://github.com/oladushkin)