try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        text = file.read()
    print("开始读取")
    print(text)
    print("读取结束")
except FileNotFoundError:
    print("找不到sample.txt文件")
    print("请确认文件在当前目录中")
    # 在你现有代码后面添加
words = text.split()  # 把文本分割成单词列表
print("单词列表：")
for word in words:
    print(word)

# 统计每个单词出现次数
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("词频统计：")
for word, count in word_count.items():
    print(f"{word}: {count}")