ver = "0.12"

class Member:
    def __init__(self, name, words=""):
        self.name = name
        self.words = words
    
    def name(self):
        return self.name

print("メンバーリスト・アプリ  Ver. "+ver)
print("--------------------------------")

# メンバー追加
mlist = []
newmember = Member("江頭2:50", "エガちゃんです！")
mlist.append(newmember)

### 以下に自分を追加する ###
newmember = Member("齋藤空", "よろしくお願いします！")
mlist.append(newmember)
newmember = Member("蜂屋孝太郎", "アタオカです！")
mlist.append(newmember)
newmember = Member("伊藤圭", "よろしく")
mlist.append(newmember)
newmember = Member("佐久間駿太", "3年です！")
mlist.append(newmember)
newmember = Member("高野瞬", "こんばんは")
mlist.append(newmember)
newmember = Member("蜂屋孝太郎", "アタオカです！")
mlist.append(newmember)
newmember = Member("服部一花", "姓の読みはハットリです")
mlist.append(newmember)
newmember = Member("伊藤圭", "よろしく")
mlist.append(newmember)
newmember = Member("服部一花", "姓の読みはハットリです")
mlist.append(newmember)
newmember = Member("石垣瑠平", "お願いします")
mlist.append(newmember)
newmember = Member("石垣瑠平", "お願いします")
mlist.append(newmember)
newmember = Member("高野瞬", "こんばんは")
mlist.append(newmember)
newmember = Member("伊美祐希", "よろしくお願いいたします。")
mlist.append(newmember)
newmember = Member("山口莉歩", "ヤマグチです！")
mlist.append(newmember)

# メンバー表示
print("各メンバーから一言")
print()
for member in mlist:
    print(member.name + " ..... " + member.words)
