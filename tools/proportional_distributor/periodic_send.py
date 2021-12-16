from crontab import CronTab

cron = CronTab(user='wangge')
for job in cron:
  print(job)
job = cron.new(command='echo hello_world >> ~/output.txt')
job.day.every(1)
cron.write()