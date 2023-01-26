import scripts.print as module
from inspect import getmembers, isfunction  

to_execute = [fnct for fnct, _ in getmembers(module, isfunction) if fnct != 'get_stuff']


func = getattr(module, to_execute[0])

func('Hidden Stuff')