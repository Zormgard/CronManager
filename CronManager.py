from crontab import CronTab
import argparse
import os ,sys
import logging

class CronManager:

	def __init__(self):
		self.cron = CronTab(user=True)

#create a 2min cron job
	def add_minutely_cron_job(self, name, user, command, enviroment=None):
		cron_job = self.cron.new(command=command , user='infowise')
		cron_job.minute.every(2)
		cron_job.enable()
		self.cron.write()
		if self.cron.render():
			print(self.cron.render())
			return True

#create a job that runs in the hours between 0-23
	def add_hourly_cron_job(self, name, user, command, enviroment=None):
		cron_job = self.cron.new(command=command, user='infowise')
		cron_job.minute.on(0)
		cron_job.hour.during(0,23)
		cron_job.enable()
		self.cron.write()
		if self.cron.render():
			print(self.cron.render())
			return True

#create a daily job
	def add_daily_cron_job(self, name, user, command, enviroment=None):
		cron_job = self.cron.new(command=command, user='infowise')
		cron_job.minute.on(0)
		cron_job.hour.on(0)
		cron_job.enable()
		self.cron.write()
		if self.cron.render():
			print(self.cron.render())
			return True

#create a weekly job that runs in the month 1-12
	def add_weekly_cron_job(self, name, user, command, enviroment=None):
		cron_job = self.cron.new(command=command)
		cron_job.minute.on(0)
		cron_job.hour.on(0)
		cron_job.day.on(1)
		cron_job.month.during(1,12)
		cron_job.enable()
		self.cron.write()
		if self.cron.render():
			print(self.cron.render())
			return True

#create a job that run every 3 month
	def add_quarterly_cron_job(self, name, user, command, enviroment=None):
		cron_job = self.cron.new(command=command)
		cron_job.minute.on(0)
		cron_job.hour.on(0)
		cron_job.day.on(1)
		cron_job.month.on(3,6,9,12)
		cron_job.enable()
		self.cron.write()
		if self.cron.render():
			print(self.cron.render())
			return True

#create a yearly job

	def add_yearly_cron_job(self, name, user, command, enviroment=None):
		cron_job = self.cron.new(command=command)
		cron_job.minute.on(0)
		cron_job.hour.on(0)
		cron_job.minute.on(12)
		cron_job.enable()
		self.cron.write()
		if self.cron.render():
			print(self.cron.render())
			return True




