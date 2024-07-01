<<<<<<< HEAD
<<<<<<< Updated upstream
ver = "0.3"
=======
ver = "0.2"
>>>>>>> Stashed changes
=======
<<<<<<< HEAD
<<<<<<< Updated upstream
ver = "0.5"
=======
ver = "0.2"
>>>>>>> Stashed changes
=======
ver = "0.2"
>>>>>>> 5f6e6098760df310092771019596dc433978bbe9
>>>>>>> 4c66698dea615e302948831d83ed611dc01cdb75

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
<<<<<<< HEAD
<<<<<<< Updated upstream

newmember = Member("伊藤圭", "よろしく")
=======
newmember = Member("佐久間駿太", "3年です！")
mlist.append(newmember)
>>>>>>> Stashed changes

newmember = Member("高野瞬", "こんばんは")

=======
<<<<<<< HEAD
<<<<<<< Updated upstream
newmember = Member("蜂屋孝太郎", "アタオカです！")
=======
newmember = Member("服部一花", "姓の読みはハットリです")
>>>>>>> 5f6e6098760df310092771019596dc433978bbe9
>>>>>>> 4c66698dea615e302948831d83ed611dc01cdb75
mlist.append(newmember)

newmember = Member("伊藤圭", "よろしく")
=======
newmember = Member("石垣瑠平", "お願いします")
>>>>>>> Stashed changes
mlist.append(newmember)

newmember = Member("高野瞬", "こんばんは")
mlist.append(newmember)

newmember = Member("伊美祐希", "よろしくお願いいたします。")
mlist.append(newmember)

# メンバー表示
print("各メンバーから一言")
print()
for member in mlist:
    print(member.name + " ..... " + member.words)
