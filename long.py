import copy
class Distance: # 大回り乗車の経路を計算する
    def __init__(self,g,m):
        lines = g.split("\n")
        self.size = int(lines[0]) 
        self.list = [[[],[],[]] for i in range(self.size+1)]
        for s in lines[1:]: 
            d1,d2,l,s = s.split(" ")
            self.connect(d1,d2,l,s)
        lines2 = m.split("\n")
        self.name = []
        for t in lines2:
            self.name.append(t)
    def connect(self,x,y,l,s): 
        self.connect1(x,y,l,s)
        self.connect1(y,x,l,s)
    def connect1(self,x,y,l,s):
        x = int(x)
        y = int(y)
        l = float(l)
        self.list[x][0].append(y) # 接続先の頂点を格納
        self.list[x][1].append(l) # 距離を格納
        self.list[x][2].append(s) # 路線名を格納
    def trav(self,frm,to):
        nlist = [] # 通った頂点のリスト
        l = 0 # 距離
        llist = [] # 経路ごとの距離のリスト
        elist = [] # 経路ごとの路線のリスト
        wlist = [] # 経路の経由駅と路線のリスト
        self.fmap = [None for i in range(self.size+1)] # 経由したことを判別するリスト
        self.travx(frm,frm,to,nlist,l,llist,wlist,elist) # 経路探索
        print("経路:",self.name[frm],"→",self.name[to])
        print("最長距離:",round(max(llist),1),"km")
        k1 = llist.index(max(llist))
        print("最長経路:",self.name[frm],end="")
        for i in range(len(wlist[k1][0])):
            print("→(",end="")
            print(wlist[k1][1][i],end="")
            print(")→",self.name[wlist[k1][0][i]],end="")
        print()
        print("最短距離:",round(min(llist),1),"km")
        k2 = llist.index(min(llist))
        ans2 = [self.name[frm]]
        print("最短経路:",self.name[frm],end="")
        for i in range(len(wlist[k2][0])):
            print("→(",end="")
            print(wlist[k2][1][i],end="")
            print(")→",self.name[wlist[k2][0][i]],end="")
        print()
    def travx(self,frm,d,to,nlist,l,llist,wlist,elist):
        if d == to: # 経路検出
            llist.append(l)
            wlist.append([copy.copy(nlist),copy.copy(elist)])
        for i in range(len(self.list[d][0])):
            u = self.list[d][0][i]
            p = self.list[d][1][i]
            a = self.list[d][2][i]
            if u != frm and self.fmap[u] == None: # 今の頂点から行けて、今まで通っていない頂点がある(始点を除く)
                nlist.append(u) # 頂点を追加
                elist.append(a) # 路線名を追加
                l += p # 距離を加算
                self.fmap[u] = d # 通ったことを記録する
                self.travx(frm,u,to,nlist,l,llist,wlist,elist)
                self.fmap[u] = None # 移動前に戻しておく
                l -= p
                nlist.pop(-1)
                elist.pop(-1)
def test():
    graph = '''57
1 2 1.3 東北本線
2 3 0.7 東北本線
3 4 1.6 東北本線
4 5 2.2 東北本線
5 6 1.3 東北本線
6 7 5.2 山手線
7 8 4.8 山手線
8 9 0.7 山手線
9 10 7.9 山手線
10 1 8.8 東海道本線
1 28 4.8 総武本線
2 29 1.3 中央本線(快速)
3 28 3.4 総武本線支線
3 29 0.9 総武本線支線
29 9 7.0 中央本線
27 28 15.8 総武本線
26 27 18.6 総武本線
11 27 5.9 武蔵野線
12 27 5.4 武蔵野線
25 26 16.1 総武本線
13 26 3.8 外房線
18 25 21.6 総武本線
23 25 13.1 成田線
17 18 13.8 東金線
23 24 10.8 成田線空港支線
1 11 18.2 京葉線
11 12 7.8 京葉線
12 13 17.0 京葉線
13 17 19.1 外房線
13 14 31.3 内房線
14 15 32.2 久留里線
14 16 88.1 内房線
16 17 89.5 外房線
18 19 40.4 総武本線
19 20 3.2 総武本線
19 21 31.8 成田線
21 22 17.4 鹿島線
21 23 30.5 成田線
5 30 22.9 常磐線
27 30 14.3 武蔵野線
23 31 32.9 成田線我孫子支線
30 31 10.6 常磐線
31 32 67.5 常磐線
32 33 16.5 常磐線
33 34 94.1 常磐線
33 35 10.1 水郡線
35 36 9.5 水郡線常陸太田支線
35 37 45.5 水郡線
6 38 6.1 東北本線
7 38 5.5 赤羽線(埼京線)
5 39 2.6 東北本線支線(尾久経由)
38 39 5.0 東北本線支線(尾久経由)
38 40 9.3 東北本線
38 41 10.6 東北本線(武蔵浦和経由・埼京線)
40 42 7.8 東北本線
41 42 7.4 東北本線(武蔵浦和経由・埼京線)
30 40 25.8 武蔵野線
40 41 1.9 武蔵野線
42 43 50.3 東北本線
43 32 50.2 水戸線
43 44 28.9 東北本線
44 45 11.7 東北本線
44 47 40.5 日光線
45 46 42.1 東北本線
45 48 20.4 烏山線
42 49 34.4 高崎線
49 50 35.9 高崎線
50 51 4.4 高崎線
51 52 7.3 上越線
51 55 29.7 信越本線
52 43 84.4 両毛線
52 53 13.8 上越線
53 54 38.0 上越線
53 56 55.3 吾妻線
42 57 30.6 川越線
50 57 60.9 八高線'''
    name = '''
東京
神田
秋葉原
上野
日暮里
田端
池袋
新宿
代々木
品川
市川塩浜
南船橋
蘇我
木更津
上総亀山
安房鴨川
大網
成東
松岸
銚子
香取
鹿島サッカースタジアム
成田
成田空港
佐倉
千葉
西船橋
錦糸町
御茶ノ水
新松戸
我孫子
友部
水戸
いわき
上菅谷
常陸太田
常陸大子
赤羽
尾久
南浦和
武蔵浦和
大宮
小山
宇都宮
宝積寺
黒磯
日光
烏山
熊谷
倉賀野
高崎
新前橋
渋川
水上
横川
大前
高麗川'''
    g = Distance(graph,name)
    g.trav(1,56)
    g.trav(54,34)
test()
