

"""
接口请求核心逻辑
处理测试用例执行
处理测试集执行
数据的组装
数据的解析
数据的存储
状态的修改
等等
"""
"""
1. 从前台点击执行触发时、获取、返回的测试环境id、用例id、用例集id、
2. 依据上一步返回、去数据库提取测试服务器数据、测试用例数据、测试用例集数据、
3. 如果 测试用例、测试用例集 需要配置数据信息、提取配置数据信息、
4. 合并测试数据、将配置数据更新到请求的数据中、待下一步执行请求使用
5. 执行请求、接收响应、
6. 如果有检查点、进行测试结果检查校验测试是否通过
7. 请求完毕后、保存必要数据、更新测试最终状态、通过/失败
8. 执行最后清理工作
"""

"""
配置数据、
json文件、文本文件、数据库、执行上下午
分别设计、最后合成。

"""



def case_run(case_id):
    """
    测试用例执行
    """

def suite_run(suite_id):
    """
    测试用例集执行
    """



def request_run(data):
    """
    调用requests框架相关、处理单次请求的发起、执行的最终入口位置
    """