import numpy as np

stuff = {"event_name1": ["1/2/3", "fun"], "event_name2": ["3/4/19", "educational"], "event_name3": ["3/4/18", "educational"]}

event_cats = [x[1] for x in list(stuff.values())]
print (event_cats)
