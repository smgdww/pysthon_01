

# loguru模块

"""功能
1. 可以格式化日志
2. 着色(不同的颜色)
3. 生成到文件
4. 显示不同的日志级别
5. 只使用一个对象(非常方便)
"""

# 1. 下载安装 ：pip install loguru

# 2. 导包 ：
from loguru import logger


# 3.打印一条日志 ： hello world
logger.info("hello world")


# 输出不同的日志级别 ，分别是debug , info , warning ,sunccess ,error(重要级别依次递增)
"""
1.debug:调试日志
1.info:普通日志
1.warning ：警告日志
1.success ：成功日志
1.error ：错误日志
"""
logger.debug("这是一条debug日志")
logger.info("这是一条info日志")
logger.warning("这是一条warning日志")
logger.success("这是一条success日志")
logger.error("这是一条error日志")


# 输出到文件 ： add()  # 后面的level=的内容表达的是添加当前和当前以上级别的日志，以下的不添加
logger.add('a.log',format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {module} | {line}| {message}",level="DEBUG")
logger.debug("这是一条debug日志")
logger.info("这是一条info日志")
logger.warning("这是一条warning日志")
logger.success("这是一条success日志")
logger.error("这是一条error日志")


# 进行传入参数的格式化 ：与.format作用类似
logger.info("我的名字叫{}，今天星期{}",'张三','1')