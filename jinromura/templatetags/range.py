#難易度の値分だけ★を表示するためのrangeメソッドの設定
from django import template
#タグライブラリの有効化
register = template.Library()

#register.filterデコレータ　register.filter('range',range)と同義
@register.filter(name='range')
def _range(_min, args=None):
    _max, _step = None, None
    if args:
        #isinstance:第一引数が第二引数のインスタンスならTRUE
        if not isinstance(args, int):
            _max, _step = map(int, args.split(','))
        else:
            _max = args
    #filterの第一引数noneだと第二引数そのまま入る
    args = filter(None, (_min,_max,_step))
    #return range(最初の数,最後の数値,増加する量)
    return range(*args)
