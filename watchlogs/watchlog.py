import logging
import os

import coloredlogs


def watchlog(name: str, level: str = 'INFO'):
    """
    [summary]

    Args:
        name (str): [description]
        level (str, optional): [description]. Defaults to None.

    Returns:
        [type]: [description]
    """
    # 檢查路徑
    # 資料夾
    directory = 'log'
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)

    # 記錄檔路徑
    filename = 'tmp.log'
    if not os.path.isfile(directory + '/' + filename):
        with open(directory + '/' + filename, 'w') as file:
            pass

    # log 格式化
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(name)

    # append stdout/console
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)

    # append log to file
    file = logging.FileHandler(filename='./log/tmp.log')
    file.setFormatter(formatter)
    logger.addHandler(file)

    # colored
    coloredlogs.install(logger=logger, level=level)
    return logger
