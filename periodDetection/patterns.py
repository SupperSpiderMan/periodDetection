# -*- coding: utf-8 -*-
"""
Created on the 30th Apr 2018

@author : zhaojun HAO
"""
CHS_ARABIC_MAP = {
    u'零':0, u'一':1, u'二':2, u'俩':2, u'两':2, 
    u'三':3, u'四':4, u'五':5, u'六':6, u'七':7, 
    u'八':8, u'九':9, u'十':10,
    u'〇':0, u'壹':1, u'贰':2, u'叁':3, u'肆':4,
    u'伍':5, u'陆':6, u'柒':7, u'捌':8, u'玖':9,
    u'拾':10, u'幺': 1, 
    u'千': 10**3, u'仟' : 10**3,
    u'０':0, u'１':1, u'２':2, u'３':3, u'４':4,
    u'５':5, u'６':6, u'７':7, u'８':8, u'９':9,
    u'百' : 10 **2 , u'佰' : 10 **2
}

PATTERN = \
r'(?P<root>(?P<ordinal_root>[0-9去明前后大今本上下这个昨]+)(?P<unit_root>(?:年|全年|整年|一整年|半年|月|周|星期|礼拜|天|日)))?份?度?年?的?最?(?P<pos_affix>上|下|前|后|第|第|首|末)?(?P<number_affix>[0-9]+)?个?(?P<unit_affix>年|全年|整年|一整年|半年|季度|月|周|星期|礼拜|天|日|号)(?P<number_special>[0-9]+)?'

PATTERN2 = \
r'(?P<root>(?P<ordinal_root>[0-9去明前后大今本上下这个昨]+)(?P<unit_root>(?:年|全年|整年|一整年|半年|月|周|星期|礼拜|天|日)))?份?度?年?的?最?(?P<pos_affix>上|下|前|后|第|第|首|末)?(?P<number_affix>[0-9]+)?个?(?P<unit_affix>年|全年|整年|一整年|半年|季度|月|周|星期|礼拜|天|日|号)'


POS_AFFIX_DICT ={
    '上' : 'first',
    '下' : 'last',
    '前' : 'first',
    '后' : 'last',
    '首' : 'first',
    '末' : 'last' ,
    '第' : 'ordinal'
    # '周' : 'special',
    # '礼拜' : 'special',
    # '星期' : 'special'
} # 缺失则为第

UNIT_DICT ={
    '年' : [12, 'month'],
    '全年' : [12, 'month'],
    '整年' : [12, 'month'],
    '一整年' : [12, 'month'],
    '半年' : [6, 'month'],
    '季度' : [3, 'month'],
    '月' : [1, 'month'],
    '周' : [1, 'week'],
    '星期' : [1, 'week'],
    '礼拜' : [1, 'week'],
    '天' : [1, 'day'],
    '号' : [1, 'day'],
    '日' : [1, 'day']
} 

LEVEL_DICT = {
    'year' : 0,
    'month' : -1,
    'week' : -2,
    'day' : -3
}
