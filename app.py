'''你妈的我在写什么狗屎程序，这么简单的东西给我写的这么恶心人
假如你打开了这个文件，看到这些屎山代码，恳请大佬帮我改改
假如你不肯帮我改，请v我5块请我喝电解质水（歹毒
'''
import pandas as pd
import random
from docx import Document
import json

# 读取Excel文件
form = pd.read_excel("Exercise.xlsx")
single_form = form[form['Type'] == 'single']
multiple_form = form[form['Type'] == 'multiple']
judge_form = form[form['Type'] == 'judge']
form_lst = [single_form, multiple_form, judge_form]

# 回答正确和错误的回复
correct=['答对了！你小子有点水平嘛！',
         '太棒了！你简直是学霸！',
         '答对了，你真的很厉害！',
         '正确答案！666！',
         '答对了，给你个大红花🌺！',
         '你的答案完全正确，骄傲一下！',
         "哇，答对了，好厉害啊！",
         "答对了，这个问题对你来说太简单了吧！"]
incorrect=["哇，答错了，下次记得查查答案哦！",
           "嗯，这个答案似乎来自另一个星球。",
           "不对，但是别担心，你仍然是大学牲！",
           "答错了，但这是一个难题，你很努力了。",
           "这个答案不太对，但是你的幽默感却很棒！",
           "哈哈，戳啦，你的创造力让我大开眼界！",
           "不对，但也有可能是答案不对，有疑问及时反馈哦！",
           "和答案不一样，可能是答案错了哦，有问题记得反馈！",
           "戳啦！没出息没关系，还有气息就已经很厉害了呢！"]

# 初始化错题本文档
error_doc = Document()

# 保存和加载记忆值的文件名
memory_file = 'memory.json'

# 尝试从文件加载记忆值
try:
    with open(memory_file, 'r') as file:
        appeared_questions_from_file = json.load(file)
        appeared_questions = {key: set(value) for key, value in appeared_questions_from_file.items()}
except FileNotFoundError:
    appeared_questions = {'1': set(), '2': set(), '3': set()}

# 随机列表生成函数
def random_list(n):
    ran_lst = list(range(n))
    random.shuffle(ran_lst)
    return ran_lst

# 回答问题函数
def ans_question(form_type_index):
    form_type = form_lst[form_type_index - 1]
    ques_lst = form_type.reset_index()
    n = len(ques_lst)
    ran_lst = random_list(n)
    all_answered = True  # 检查是否所有题目都已答过

    for i in ran_lst:
        if str(ques_lst.loc[i, 'ID']) in appeared_questions.get(str(form_type_index), set()):
            continue
        all_answered = False
        appeared_questions[str(form_type_index)].add(str(ques_lst.loc[i, 'ID']))

        print(f"\n{ques_lst.loc[i, 'Question']}")
        print(ques_lst.loc[i, 'Option'])
        user_ans = input('请输入答案：')
        if user_ans.lower() == ques_lst.loc[i, 'Answer'].lower():
            print(random.choice(correct))
        else:
            print(random.choice(incorrect))
            error_doc.add_paragraph(f"{ques_lst.loc[i, 'Question']}\n{ques_lst.loc[i, 'Option']}\n你的答案：{user_ans}\n正确答案：{ques_lst.loc[i, 'Answer']}\n解析：{ques_lst.loc[i, 'Analysis']}\n\n\n")
            error_doc.save('错题本.docx')

        print(f'正确答案是：{ques_lst.loc[i, "Answer"]}')
        print(ques_lst.loc[i, 'Analysis'])
        print()
        feedback = input('继续答题请按回车\n想换题型或退出程序请输入“滚”\n答案有误我要反馈请输入“老毕登”')
        if feedback == '滚':
            break
        elif feedback == '老毕登':
            feedback_ans = input('你认为的正确答案是：')
            print(f"请复制以下内容然后发给我：\nV你{ques_lst.loc[i, 'ID']}元，请你喝电解质水。\n暗号从{ques_lst.loc[i, 'Answer']}改成{feedback_ans}。")

    if all_answered:
        print(f"提示：{form_type_index}类型的题目已全部答完！\n复制链接到浏览器，领取彩蛋：https://www.bilibili.com/video/BV1Pg411r7V5/?spm_id_from=333.337.search-card.all.click")


# 程序入口
def main():
    global appeared_questions
    print('这是数导刷题小程序2.1，它将随机生成你想要的题型供你刷题。')
    print('（注：答案及解析来自ChaGPT4.0和同学的反馈，目前这版应该是最接近标准答案的力，遇到答案有疑问的请及时联系我！）')
    print('客官用的顺手的话，v我5元助力我买电解质水（乞讨')
    print()
    while True:
        try:
            choice = int(input('想写单选请输入1，\n想写多选请输入2，\n想写判断请输入3，\n退出程序请输入0，\n格式化刷题记录请输入-1。\n'))
            if choice == 0:
                break
            if choice == -1:
                appeared_questions = {'1': set(), '2': set(), '3': set()}
                print("刷题记录已格式化。有魄力兄弟（抱拳）。")
                appeared_questions_for_json = {key: list(value) for key, value in appeared_questions.items()}
                with open(memory_file, 'w') as file:
                    json.dump(appeared_questions_for_json, file)
            else:
                ans_question(choice)
        except ValueError:
            print("你小子主打一个叛逆是吧？请输入有效数字！")

    # 保存错题本和记忆值
    error_doc.save('错题本.docx')
    print("错题本已保存。")
    appeared_questions_for_json = {key: list(value) for key, value in appeared_questions.items()}
    with open(memory_file, 'w') as file:
        json.dump(appeared_questions_for_json, file)

# 运行程序
main()
