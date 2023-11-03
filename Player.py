from Piano import Piano
from Notation import Notation


piano = Piano()
CastleInSky = Notation()
# 定义乐曲
CastleInSky.name = "天空之称"      # 名称
CastleInSky.lyricist = ""      # 作词
CastleInSky.composer = "宫崎骏"      # 作曲
CastleInSky.base = "1=C"          # 音调
CastleInSky.beat = "4/4"          # 节拍
CastleInSky.duration = 500          # 节奏
# 谱子输入
CastleInSky.note_list = [['6l,7l', '1,7l,1,3', '7l,3l', '6l,5l,6l,1'], ['5l,3l', '4l,3l,4l,1', '3l,1', '7l,4l#,4l#,7l'],
                         ['7l,6l,7l', '1,7l,1,3', '7l,3l,3l', '6l,5l,6l,1'], ['5l,3l', '4l,1,7l,1', '2,3,1', '1,7l,6l,7l,5l#'],
                         ['6l,1,2', '3,2,3,5', '2,5l', '1,7l,1,2,3'], ['3', '6l,7l,1,7l,1,2', '1,5l,5l', '4,3,2,1'],
                         ['3,3', '6,6,5,5', '3,2,1,1', '2,1,2,5'], ['3,3', '6,6,5,5', '3,2,1,1', '2,1,2,7l'], ['6l,0']]
# 拍子输入
CastleInSky.beat_list = [[[0.5, 0.5], [1.5, 0.5, 1, 1], [3, 1], [1.5, 0.5, 1, 1]], [[3, 1], [1.5, 0.5, 0.5, 1.5], [3, 1], [1.5, 0.5, 1, 1]],
                         [[3, 0.5, 0.5], [1.5, 0.5, 1, 1], [3, 0.5, 0.5], [1.5, 0.5, 1, 1]], [[3, 1], [1, 0.5, 1.5, 1], [1, 0.5, 2.5], [0.5, 0.5, 1, 1, 1]],
                         [[3, 0.5, 0.5], [1.5, 0.5, 1, 1], [3, 1], [1.5, 0.5, 1, 0.5, 0.5]], [[4], [0.5, 0.5, 1, 0.5, 0.5, 1], [1.5, 0.5, 2], [1, 1, 1, 1]],
                         [[3, 1], [1.5, 0.5, 1.5, 0.5], [0.5, 0.5, 1, 2], [1.5, 0.5, 1, 1]], [[3, 1], [1.5, 0.5, 1.5, 0.5], [0.5, 0.5, 1, 2], [1.5, 0.5, 1, 1]],
                         [[3, 1]]]

# 演奏乐曲
piano.play(CastleInSky)