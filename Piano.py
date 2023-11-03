from winsound import Beep
class Piano:
    """
    包含按88个键，因此有个按键列表，但是弹琴被直接化为了弹音符，因此可以不需要所有的按键，但需要小字一组按键的位置
    钢琴需要根据调号，确定音符的位置，中音，低音，高音
    方法：初始化按键，演奏谱子
    """
    def __init__(self):
        [self.C4, self.D4, self.E4, self.F4, self.G4, self.A4, self.B4] = \
            [39, 41, 43, 44, 46, 48, 50]            # 中央组在钢琴上的位置
        self.ALL = [round(440 * (2 ** (1 / 12)) ** (i - 49)) for i in range(1, 89)]      # 所有键盘频率
        self.NaturalMajor = [-1, 0, 2, 4, 5, 7, 9, 11, 12]      # 自然大调间隔, 1=?为自然大调
        self.Dorian = []    # 多利亚调
        self.Phrygian = []      # 弗利几亚调
        self.Lydian = []        # 利底亚调
        self.MixedLydian = []       # 混合利底亚调
        self.NaturalMinor = []      # 自然小调
        self.Lochlian = []          # 洛克利亚调
        self.nn, self.nl, self.nh, self.nll, self.nhh = None, None, None, None, None
        self.hertz_list = []        # 音符转换为频率列表

    def init_note(self, base):
        """
        初始化音符，得到每个音符对应的频率
        :return:
        """
        major = {"1": self.NaturalMajor, "2": self.Dorian, "3": self.Phrygian, "4": self.Lydian, "5": self.MixedLydian,
                 "6": self.NaturalMinor, "7": self.Lochlian}[base[0]]
        b_key = {"C": self.C4, "D": self.D4, "E": self.E4, "F": self.F4, "G": self.G4, "A": self.A4, "B": self.B4}[base[-1]]
        # 中音
        self.nn = [self.ALL[b_key + i] for i in major]
        # 低音
        self.nl = [self.ALL[b_key + i - 12] for i in major]
        # 高音
        self.nh = [self.ALL[b_key + i + 12] for i in major]
        # 倍低
        self.nll = [self.ALL[b_key + i - 24] for i in major]
        # 倍高
        self.nhh = [self.ALL[b_key + i + 24] for i in major]
        # 超低
        # 超高

    def note_analysis(self, note_list):
        """
        解析曲谱
        :return:
        """
        for i, part in enumerate(note_list):
            part_hertz = []
            for j, section in enumerate(part):
                sec_cut = section.split(",")
                sec_hertz_cut = []
                for k, val in enumerate(sec_cut):
                    if "l" in val:
                        tar_hertz = self.nl[int(val[0])]
                    elif "h" in val:
                        tar_hertz = self.nh[int(val[0])]
                    else:
                        tar_hertz = self.nn[int(val[0])]
                    if "#" in val:
                        tar_hertz = self.ALL[self.ALL.index(tar_hertz) + 1]
                    elif "b" in val:
                        tar_hertz = self.ALL[self.ALL.index(tar_hertz) - 1]
                    else:
                        pass
                    if "0" in val:
                        tar_hertz = 37      # 最低可接受频率，相当于不响
                    sec_hertz_cut.append(tar_hertz)
                part_hertz.append(sec_hertz_cut)
            self.hertz_list.append(part_hertz)

    def play(self, notation):
        """
        演奏乐曲
        :return:
        """
        self.init_note(notation.base)
        self.note_analysis(notation.note_list)
        for i, val in enumerate(self.hertz_list):
            for j, val2 in enumerate(val):
                for k, val3 in enumerate(val2):
                    print(val3, notation.beat_list[i][j][k])
                    Beep(val3, int(notation.beat_list[i][j][k] * notation.duration))

