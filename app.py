import pandas as pd
import random

form = pd.read_excel("Exercise.xlsx")
single_form = form[form['Type'] == 'single']
multiple_form = form[form['Type'] == 'multiple']
judge_form = form[form['Type'] == 'judge']
form_lst = [form, single_form, multiple_form, judge_form]

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

def random_list(n):
    ran_lst = list(range(1, n+1))
    random.shuffle(ran_lst)
    return ran_lst

def ans_question(flag):
    if flag > 0 and flag < len(form_lst):
        ques_lst = form_lst[flag].reset_index()
        n = len(ques_lst)
        ran_lst = random_list(n)
        for i in ran_lst:
            print(ques_lst.loc[i, 'Question'])
            print(ques_lst.loc[i, 'Option'])
            user_ans = input('请输入答案：')
            if user_ans.lower() == ques_lst.loc[i, 'Answer'].lower():
                print(random.choice(correct))
            else:
                print(random.choice(incorrect))
            print(f'正确答案是：{ques_lst.loc[i, "Answer"]}')
            print(ques_lst.loc[i, 'Analysis'])
            feedback = input('继续答题请按回车，\n想换题型或退出程序请输入“滚”，\n答案有误我要反馈请输入“老毕登”')
            if feedback == '滚':
                break
            elif feedback == '老毕登':
                feedback_ans=input('你认为的正确答案是：')
                print(f"请复制以下内容然后发给我：\nV你{ques_lst.loc[i, 'ID']}元，请你喝电解质水。\n暗号从{ques_lst.loc[i, 'Answer']}改成{feedback_ans}。")
            

# 程序入口
print('这是一个数导刷题的小程序：D，它将随机生成你想要的题型供你刷题。')
print('（注：所有的答案及解析来自ChaGPT4.0，不保证答案准确性，答案如有出入以老师为准，遇到答案有疑问的请及时联系我！）')

flag = 1
while flag > 0:
    flag = int(input('想写单选请输入1，\n想写多选请输入2，\n想写判断请输入3，\n退出程序请输入0。\n'))
    ans_question(flag)
