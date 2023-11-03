

class Notation:
    """
    曲谱主要有，音调，节拍，名字，词曲作者，谱子
    谱子需要进行分析。目前做到的是，把音符和拍子分开表示
    """
    def __init__(self):
        self.name = None            # 歌曲名称
        self.lyricist = None        # 作词
        self.composer = None        # 作曲
        self.base = None        # 确定音调，如，1=C，字符串格式
        self.beat = None        # 节拍
        self.note_list = None        # 谱子
        self.beat_list = None           # 拍子
        self.duration = None           # 节奏，正常为500，0.5s一个四分拍

