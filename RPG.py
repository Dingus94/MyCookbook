import datetime
import time
localtime = time.localtime(time.time())
tasks = {'lift weights': [3, 2, 1], 'eliptical': [2, 3, 1], 'practice coding': [1, 1, 3]}


class Hero:
    def __init__(self, name, strength, stamina, intelligence):
        self.name = name
        self.strength = strength
        self.stamina = stamina
        self.intelligence = intelligence

    def __repr__(self):
        return 'Hero: {} \nStrength: {} \nStamina: {} \nIntelligence: {}'.format(self.name, self.strength, self.stamina, self.intelligence)

    def complete_task(self, task):
        if task in tasks.keys():
            self.strength += (tasks.get(task)[0])
            self.stamina += (tasks.get(task)[1])
            self.intelligence += (tasks.get(task)[2])

    def stat_decay(self):
        while True:
            if localtime.tm_sec == 0:
                self.strength -= 5
                self.stamina -= 5
                self.intelligence -= 5
                print(Thomas)


    def add_new_tasks(newtask, str, sta, int):
        new_tasks = {newtask: [str, sta, int]}
        return tasks.update(new_tasks)





Thomas = Hero("Thomas", 6, 8, 20)

Thomas.complete_task('lift weights')

Hero.add_new_tasks('shadow box', 1, 2, 1)

Thomas.complete_task('shadow box')

print(Thomas)

time.sleep(60)




