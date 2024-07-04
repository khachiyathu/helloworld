



<<<<<<< Updated upstream
<<<<<<< HEAD
ver = "0.3"
=======
ver = "0.14"
=======
ver = "0.2"
>>>>>>> Stashed changes

>>>>>>> 54d61dc7068851e05923c46e033d27a675c3f41e
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
<<<<<<< Updated upstream
<<<<<<< HEAD
newmember = Member("三瓶祥太", "よろしく！")
mlist.append(newmember)

newmember = Member("斎藤高史", "さいとうです！")

newmember = Member("蜂屋孝太郎", "アタオカです！")

newmember = Member("服部一花", "姓の読みはハットリです")

=======
newmember = Member("田部大地", "あたおかです！")
mlist.append(newmember)
newmember = Member("和田龍飛", "こんにちは")
mlist.append(newmember)

newmember = Member("酒井隆之介", "よろしく！")
mlist.append(newmember)
newmember = Member("齋藤空", "よろしくお願いします！")
mlist.append(newmember)
newmember = Member("蜂屋孝太郎", "アタオカです！")
>>>>>>> 54d61dc7068851e05923c46e033d27a675c3f41e
mlist.append(newmember)
newmember = Member("伊藤圭", "よろしく")
<<<<<<< HEAD

newmember = Member("石垣瑠平", "お願いします")


=======
mlist.append(newmember)
newmember = Member("佐久間駿太", "3年です！")
mlist.append(newmember)
newmember = Member("服部一花", "姓の読みはハットリです")
mlist.append(newmember)
newmember = Member("石垣瑠平", "お願いします")
mlist.append(newmember)
>>>>>>> 54d61dc7068851e05923c46e033d27a675c3f41e
newmember = Member("高野瞬", "こんばんは")
mlist.append(newmember)
newmember = Member("伊美祐希", "よろしくお願いいたします。")
<<<<<<< HEAD
=======
newmember = Member("三瓶祥太", "あたおかです！")
mlist.append(newmember)
>>>>>>> Stashed changes


=======
mlist.append(newmember)
newmember = Member("山口莉歩", "ヤマグチです！")
mlist.append(newmember)
newmember = Member("綱島隼斗", "おはようございます")
mlist.append(newmember)
             
>>>>>>> 54d61dc7068851e05923c46e033d27a675c3f41e
# メンバー表示
print("各メンバーから一言")
print()
for member in mlist:
    print(member.name + " ..... " + member.words)
