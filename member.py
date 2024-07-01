ver = "0.3"

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

newmember = Member("伊藤圭", "よろしく")

newmember = Member("高野瞬", "こんばんは")

mlist.append(newmember)


newmember = Member("伊美祐希", "よろしくお願いいたします。")
mlist.append(newmember)

# メンバー表示
print("各メンバーから一言")
print()
for member in mlist:
    print(member.name + " ..... " + member.words)
