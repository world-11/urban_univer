team_1 = "Мастера кода"
team_2 = "Волшебники данных"
team1_num = 6
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
task_total = score_1 + score_2
time_avg = (team1_time + team2_time) / task_total
challenge_result = ''

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = "Победа команды Мастера кода!"
elif score_1 < score_2 or score1 == score_2 and team1_time < team2_time:
    challenge_result = "Победа команды Волшебники Данных!"
else:
    challenge_result = "Ничья!"

print('В команде %s участников %s' %(team_1, team1_num))
print('Итого сегодня в командах участников: %s  %s' %(team1_num, team2_num))
print('Команда {} решила задач {}'.format(team_2, str(score_2)))
print('{} решили задачи за {}'.format(team_2, str(team1_time)))
print(f'Команды решили {score_1} и {score_2} задач')
print(f"Результат битвы: {challenge_result}")
print(f"Сегодня было решено {task_total} задач, в среднем по {round(time_avg, 1)} секунды на задачу!.")
