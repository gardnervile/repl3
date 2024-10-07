import smtplib 
import os
password = os.environ['password']
website = "https://dvmn.org/referrals/JjL6nrWQ2450G9PuQReItKaZvJY6d9djQx1ItWpH/"
friend_name = "Данил"
sender_name = "Женя"
sender_email = "evgeniy.kondratiev@pet-subject.com"
friend_email = "Gardnervilek@yandex.ru"
letter = """From: {se}
To: {fe}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

Привет, {fn}! {sn} приглашает тебя на сайт {w}!

{w} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {w}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {w} 
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""".format(w=website, fn=friend_name, sn=sender_name, se=sender_email, fe=friend_email)
letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(sender_email, password)
server.sendmail(sender_email, friend_email, letter)
server.quit()
