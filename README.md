# Mixed-computing-self-test
小学生四则运算自测包括填写结果、对错判断、选择题等。可选择难度  
entrence 为程序入口也是第一个界面  
![图片](image/1.png)  
examination为第二个界面(作答评价)  
![图片](image/2.png)  
完整的流程:  
1.输入姓名并选择难度：(若查询成绩则点击查询：否则进入下一步)  
![图片](image/3.png)  
2.点击生成试题并作答：  
![图片](image/4.png)   
3.提交成绩：  
![图片](image/5.png)   
说明：7.jpg为界面背景图片，answer，question为暂存答案和问题，用于显示在界面上，退出系统后自动清除，grades存储成绩用于assessment评价系统评判成绩，signal信号为是否带括号，题目个数等的标志，每次运行程序后自动清理，name暂存名字用于界面输出成绩和保存成绩，评价到user_grade_assess.txt(用于查询成绩) ，Realcalculate用于生成表达式，test2用于字符串表达式的计算。  
转载请备注出处
