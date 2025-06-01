# 尝试执行下面的代码，如果出错会进入except部分
try:
    # 打开名为sample.txt的文件，以只读模式（r）和utf-8编码方式
    with open("sample.txt", "r", encoding="utf-8") as file:
        # 读取文件的全部内容，存到变量text里
        text = file.read()
    print("开始读取")  # 输出提示，表示开始读取文件
    print(text)       # 输出文件内容
    print("读取结束")  # 输出提示，表示读取结束
    words = text.split()  # split()是字符串的方法，把字符串按空格分开，变成一个单词列表
    print("单词列表：")
    for word in words:
        print(word)  # 逐个输出每个单词

# 创建一个空字典，用来统计每个单词出现的次数
    word_count = {}
    for word in words:
    # 如果单词已经在字典里，次数加1，否则设为1
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    print("词频统计：")
# items()是字典的方法，会把字典里的每一对（单词, 次数）都拿出来
    for word, count in word_count.items():
        print(f"{word}: {count}")  # 输出单词和对应的次数
except FileNotFoundError:
    # 如果找不到sample.txt文件，会执行这里的代码
    print("找不到sample.txt文件")
    print("请确认文件在当前目录中")

# 把文本内容按空格分割成单词列表

