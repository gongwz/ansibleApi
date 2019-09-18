# _*_ encoding=utf-8 _*_

__author__ = 'weizhen'


from ansibleApi import MyApi

# hostfile 可以是一个静态文件, 也可以是一个get_inventory文件 (最后把取到的内容print出来)
api = MyApi("hosts")

# 执行 Ad-hoc
api.run("172.28.62.129", "command","ls -al /opt")

# 执行 playbook
api.run_playbook("172.28.62.129", "test.yml")

# 获取返回值 字典
dic_res = api.get_result()
print(dic_res)

# 获取返回值 json
json_res = api.get_json()
print(json_res)
