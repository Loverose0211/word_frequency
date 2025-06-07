import os

# 1. 提示用户输入文件路径
file_path = input("请输入要分析的文本文件路径(例如:sample.txt):")

# 2. 检查文件是否存在
if not os.path.isfile(file_path):
    print("❗文件不存在，请检查路径是否正确")
else:
    try:  # 添加错误处理，防止程序崩溃
        # 3. 尝试打开文件并读取内容
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # 4. 将文本统一转为小写（统一处理大小写）
        text = text.lower()
        
        # 5. 去除标点符号（优化版：使用列表，提高性能）
        cleaned_chars = []  # 用列表收集字符，比字符串拼接更高效
        for char in text:
            if char.isalpha() or char.isspace():  # 只保留字母和空格
                cleaned_chars.append(char)
            else:
                cleaned_chars.append(' ')  # 用空格替代标点
        
        # 将列表转换为字符串（一次性分配内存）
        cleaned_text = ''.join(cleaned_chars)
        
        # 6. 按空格切分成单词列表
        words = cleaned_text.split()
        
        # 7. 过滤空字符串（防止连续空格产生的空单词）
        words = [word for word in words if word]  # 列表推导式，只保留非空单词
        
        # 8. 统计词频
        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        
        # 9. 按词频排序（从高到低）
        sorted_words = []
        for word, count in word_count.items():
            sorted_words.append((count, word))  # 创建 (频率, 单词) 元组
        
        # 简单排序：冒泡排序（初学者容易理解）
        for i in range(len(sorted_words)):
            for j in range(len(sorted_words) - 1 - i):
                if sorted_words[j][0] < sorted_words[j + 1][0]:  # 比较频率
                    # 交换位置
                    sorted_words[j], sorted_words[j + 1] = sorted_words[j + 1], sorted_words[j]
        
        # 10. 输出结果
        print(f"\n🔍 词频统计结果如下（共找到 {len(word_count)} 个不同单词）：\n")
        print("=" * 40)
        
        for count, word in sorted_words:
            print(f'单词 "{word}" 出现频率：{count}')
        
        # 11. 输出统计摘要
        total_words = len(words)
        unique_words = len(word_count)
        print("\n" + "=" * 40)
        print(f"📊 统计摘要：")
        print(f"   总单词数：{total_words}")
        print(f"   不同单词数：{unique_words}")
        if total_words > 0:
            print(f"   重复率：{((total_words - unique_words) / total_words * 100):.1f}%")
    
    except Exception as e:
        print(f"❗读取文件时出错：{e}")
        print("可能的原因：")
        print("1. 文件编码不是UTF-8")
        print("2. 文件被其他程序占用")
        print("3. 权限不足")