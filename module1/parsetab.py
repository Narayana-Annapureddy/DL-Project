
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BEGINTABLE CLOSEDATA CLOSEDIV CLOSEHEAD CLOSEHEADER CLOSEHREF CLOSEROW CLOSESPAN CLOSESTYLE CLOSETABLE CONTENT GARBAGE OPENDATA OPENDIV OPENHEAD OPENHEADER OPENHREF OPENROW OPENSPAN OPENSTYLE OPENTABLE SPACEstart : tabletable : BEGINTABLE skiptag OPENHEAD content skiprow CLOSEHEADER OPENTABLE skiprows handlerowskiprows : skiprow skiprow skiprow skiprow skiprow skiprow skiprowskiprow : OPENROW unwanted CLOSEROWskiptag : CONTENT skiptag\n               | OPENHREF skiptag\n               | CLOSEHREF skiptag\n               | SPACE skiptag\n               | emptyunwanted : GARBAGE unwanted\n                | OPENHREF unwanted\n                | CLOSEHREF unwanted\n                | CONTENT unwanted\n                | OPENDATA unwanted\n                | CLOSEDATA unwanted\n                | SPACE unwanted\n                | OPENSPAN unwanted\n                | CLOSESPAN unwanted\n                | OPENHEADER unwanted\n                | CLOSEHEADER unwanted\n                | emptyhandlerow : OPENROW dataCell CLOSEROW  handlerow\n                 | emptydataCell : OPENDATA CONTENT CLOSEDATA dataCell\n                | OPENDATA OPENHREF content CLOSEHREF CLOSEDATA dataCell\n                | OPENDATA CLOSEDATA dataCell\n                | emptyempty :content : CONTENT content\n               | empty'
    
_lr_action_items = {'BEGINTABLE':([0,],[3,]),'$end':([1,2,36,49,51,53,59,64,71,],[0,-1,-4,-28,-2,-23,-28,-22,-3,]),'CONTENT':([3,5,6,7,8,10,16,19,23,24,25,26,27,28,29,30,31,32,33,56,62,],[5,5,5,5,5,16,16,26,26,26,26,26,26,26,26,26,26,26,26,60,16,]),'OPENHREF':([3,5,6,7,8,19,23,24,25,26,27,28,29,30,31,32,33,56,],[6,6,6,6,6,24,24,24,24,24,24,24,24,24,24,24,24,62,]),'CLOSEHREF':([3,5,6,7,8,16,17,19,20,23,24,25,26,27,28,29,30,31,32,33,62,67,],[7,7,7,7,7,-28,-30,25,-29,25,25,25,25,25,25,25,25,25,25,25,-28,70,]),'SPACE':([3,5,6,7,8,19,23,24,25,26,27,28,29,30,31,32,33,],[8,8,8,8,8,29,29,29,29,29,29,29,29,29,29,29,29,]),'OPENHEAD':([3,4,5,6,7,8,9,11,12,13,14,],[-28,10,-28,-28,-28,-28,-9,-5,-6,-7,-8,]),'OPENROW':([10,15,16,17,20,35,36,48,49,50,54,58,59,63,68,71,],[-28,19,-28,-30,-29,19,-4,19,52,19,19,19,52,19,19,-3,]),'CLOSEHEADER':([18,19,23,24,25,26,27,28,29,30,31,32,33,36,],[21,33,33,33,33,33,33,33,33,33,33,33,33,-4,]),'GARBAGE':([19,23,24,25,26,27,28,29,30,31,32,33,],[23,23,23,23,23,23,23,23,23,23,23,23,]),'OPENDATA':([19,23,24,25,26,27,28,29,30,31,32,33,52,61,65,72,],[27,27,27,27,27,27,27,27,27,27,27,27,56,56,56,56,]),'CLOSEDATA':([19,23,24,25,26,27,28,29,30,31,32,33,56,60,70,],[28,28,28,28,28,28,28,28,28,28,28,28,61,65,72,]),'OPENSPAN':([19,23,24,25,26,27,28,29,30,31,32,33,],[30,30,30,30,30,30,30,30,30,30,30,30,]),'CLOSESPAN':([19,23,24,25,26,27,28,29,30,31,32,33,],[31,31,31,31,31,31,31,31,31,31,31,31,]),'OPENHEADER':([19,23,24,25,26,27,28,29,30,31,32,33,],[32,32,32,32,32,32,32,32,32,32,32,32,]),'CLOSEROW':([19,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,39,40,41,42,43,44,45,46,47,52,55,57,61,65,66,69,72,73,],[-28,36,-28,-28,-28,-28,-28,-28,-28,-28,-28,-28,-28,-21,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-28,59,-27,-28,-28,-26,-24,-28,-25,]),'OPENTABLE':([21,],[35,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'table':([0,],[2,]),'skiptag':([3,5,6,7,8,],[4,11,12,13,14,]),'empty':([3,5,6,7,8,10,16,19,23,24,25,26,27,28,29,30,31,32,33,49,52,59,61,62,65,72,],[9,9,9,9,9,17,17,34,34,34,34,34,34,34,34,34,34,34,34,53,57,53,57,17,57,57,]),'content':([10,16,62,],[15,20,67,]),'skiprow':([15,35,48,50,54,58,63,68,],[18,48,50,54,58,63,68,71,]),'unwanted':([19,23,24,25,26,27,28,29,30,31,32,33,],[22,37,38,39,40,41,42,43,44,45,46,47,]),'skiprows':([35,],[49,]),'handlerow':([49,59,],[51,64,]),'dataCell':([52,61,65,72,],[55,66,69,73,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> table','start',1,'p_start','task1.py',105),
  ('table -> BEGINTABLE skiptag OPENHEAD content skiprow CLOSEHEADER OPENTABLE skiprows handlerow','table',9,'p_table','task1.py',109),
  ('skiprows -> skiprow skiprow skiprow skiprow skiprow skiprow skiprow','skiprows',7,'p_skiprows','task1.py',112),
  ('skiprow -> OPENROW unwanted CLOSEROW','skiprow',3,'p_skiprow','task1.py',117),
  ('skiptag -> CONTENT skiptag','skiptag',2,'p_skiptag','task1.py',121),
  ('skiptag -> OPENHREF skiptag','skiptag',2,'p_skiptag','task1.py',122),
  ('skiptag -> CLOSEHREF skiptag','skiptag',2,'p_skiptag','task1.py',123),
  ('skiptag -> SPACE skiptag','skiptag',2,'p_skiptag','task1.py',124),
  ('skiptag -> empty','skiptag',1,'p_skiptag','task1.py',125),
  ('unwanted -> GARBAGE unwanted','unwanted',2,'p_unwanted','task1.py',128),
  ('unwanted -> OPENHREF unwanted','unwanted',2,'p_unwanted','task1.py',129),
  ('unwanted -> CLOSEHREF unwanted','unwanted',2,'p_unwanted','task1.py',130),
  ('unwanted -> CONTENT unwanted','unwanted',2,'p_unwanted','task1.py',131),
  ('unwanted -> OPENDATA unwanted','unwanted',2,'p_unwanted','task1.py',132),
  ('unwanted -> CLOSEDATA unwanted','unwanted',2,'p_unwanted','task1.py',133),
  ('unwanted -> SPACE unwanted','unwanted',2,'p_unwanted','task1.py',134),
  ('unwanted -> OPENSPAN unwanted','unwanted',2,'p_unwanted','task1.py',135),
  ('unwanted -> CLOSESPAN unwanted','unwanted',2,'p_unwanted','task1.py',136),
  ('unwanted -> OPENHEADER unwanted','unwanted',2,'p_unwanted','task1.py',137),
  ('unwanted -> CLOSEHEADER unwanted','unwanted',2,'p_unwanted','task1.py',138),
  ('unwanted -> empty','unwanted',1,'p_unwanted','task1.py',139),
  ('handlerow -> OPENROW dataCell CLOSEROW handlerow','handlerow',4,'p_handlerow','task1.py',143),
  ('handlerow -> empty','handlerow',1,'p_handlerow','task1.py',144),
  ('dataCell -> OPENDATA CONTENT CLOSEDATA dataCell','dataCell',4,'p_dataCell','task1.py',148),
  ('dataCell -> OPENDATA OPENHREF content CLOSEHREF CLOSEDATA dataCell','dataCell',6,'p_dataCell','task1.py',149),
  ('dataCell -> OPENDATA CLOSEDATA dataCell','dataCell',3,'p_dataCell','task1.py',150),
  ('dataCell -> empty','dataCell',1,'p_dataCell','task1.py',151),
  ('empty -> <empty>','empty',0,'p_empty','task1.py',167),
  ('content -> CONTENT content','content',2,'p_content','task1.py',171),
  ('content -> empty','content',1,'p_content','task1.py',172),
]
