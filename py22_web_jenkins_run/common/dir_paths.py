import os


class DirPaths:
    # 工程目录
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 测试用例存放目录
    testcases_dir = os.path.join(project_dir, 'TestCases')
    # 测试报告存放目录
    report_dir = os.path.join(project_dir, 'Outputs', 'reports')
    # 失败截图存放目录
    screenshots_dir = os.path.join(project_dir, 'Outputs', 'page_screenshots')
    # 日志存放截图
    logs_dir = os.path.join(project_dir, 'Outputs', 'logs')
