'''
给你一个项目，出具一个自动化测试方案
你打算怎么做？做哪些？要花多久的时间？用什么来做？需要什么样的资源？
1、选择哪个内容做自动化测试？web网页？接口？APP？
2、做哪些？ 历史功能（重复又繁琐）
           项目的核心功能
           功能稳定、重复性高的
           流程
           线上环境当中，出bug最多的模块
           用户使用率最高的
3、花多久的时间？
预估你要写多少个接口用例？
要实现多少个web功能用例
调试？优化？Jenkins集成？接口业务了解
4、用什么来做？框架选型（用例编写规范、命名规范、结构规范）
5、从用例开始到结束整个过程的流程
定期反馈你的成果：覆盖了哪些功能？有多少用例？通过率是多少？bug量？脚本问题？优化工作、优化工作流程
6、运行策略？目的是什么？
冒烟/回归  历史bug的对比：没有自动化之前线上的bug、有了自动化之后的bug
什么时候运行自动化脚本？
通过率 用例覆盖率 功能模块

PO模式 Page Object 页面对象模型   Page Factory 页面工厂模型（java）
所有的用例 = 全部是在页面上的操作
任何一个用例 = 页面1 操作1 + 页面2 操作2&4&6 + 页面3 操作5 + 页面2去验证一下结果
把每一个页面封装成一个类（页面类） -- 元素定位（属性）+元素操作（功能/行为）
封装的对象：页面1类（操作1） 页面2类（操作2、操作4、操作6） 页面3类（操作5）
分层：测试对象 + 测试用例
'''