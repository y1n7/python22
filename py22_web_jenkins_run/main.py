import pytest
import os
from datetime import datetime
from common.dir_paths import DirPaths


report_name = datetime.now().strftime('%Y-%m-%d %H-%M-%S') + '.html'
report_file = os.path.join(DirPaths.report_dir, report_name)


if __name__ == '__main__':
    pytest.main(['-s', '-v', '--html=Outputs/reports/pytest.html',
                 '--alluredir=Outputs/allure'])

