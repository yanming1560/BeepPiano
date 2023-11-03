# BeepPiano
通过winsound模块，模拟钢琴\n
1.piano_simple_test.py，实现了一个简单的例子，计算钢琴键的频率，设置音调基准，然后演奏；
2.Piano.py 建立了一个钢琴类，钢琴需要根据调号，确定音符的位置，中音，低音，高音，然后解析简谱，最后演奏简谱。
3.Notation.py建立了一个简谱类，曲谱主要有，音调，节拍，名字，词曲作者，谱子。谱子需要进行分析。目前做到的是，把音符和拍子分开表示
4.Player用来演奏，先实例化一个简谱类，然后定义参数。然后实例化一个钢琴类，用钢琴演奏简谱。主要在这个脚本里进行操作。

注意，在输入简谱和拍子时，可能需要一点点乐理知识：
![天空之城简谱](https://github.com/yanming1560/BeepPiano/assets/36906575/2b341fd1-b671-48fd-819f-96110740a0f3)

在简谱中：
1. 低音6，输入'6l'；高音6，输入'6h'；中音6，直接输入'6'。升号#和降号b直接放在后面。
2. 拍子需要一定的乐理知识，普通1是一个四分拍，1---是一个完整拍子。一个四分拍所用的时长，在Notation里的duration定义。
3. 目前只支持自然大调，也就是"1=C"到"1=B"，其他调式作者还没接触，但是预留了属性。
4. 目前是一个完整拍子的音符，通过字符串放在一起，用逗号隔开，比如'7l,4l#,4l#,7l'，四拍放在一个list里，主要是为了方便输入，分组好找一点。
