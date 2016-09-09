#!/usr/bin/env python
import random
import sys
import time

team_list = ['Romanian Replacements',
            'STIFF ARM STRONG',
            'The Nard Dawgs',
            'Gronx',
            'Hay Balers',
            'Mike\'s Maulers',
            'Simms2Bavaro',
            'Mustachios',
            'ButteredCorn',
            'GANG GREEN',
            'Samurai Racoons',
            'The Yinzers']

num = 1
while len(team_list) > 0:
    random.shuffle(team_list)
    team = random.choice(team_list)
    print "%i: %s" % (num, team)
    time.sleep(5)
    team_list.remove(team)
    num += 1

sys.exit(0)
