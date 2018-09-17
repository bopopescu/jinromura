#難易度の値分だけ★を表示するためのrangeメソッドの設定
from django import template

register = template.library()

@register.filter(name="range")
def _range(_min,args_None):
    _max, _step = None,args_None
    if args:
        if not isinstance(args, int):
            _max, _step = map(int,args,split(','))
        else:
            _max = args
        args = filter(None,(_min,_max,_step))
        return range(*args)
