# ansibleApi
====

[![pyversions](https://img.shields.io/badge/python-3.6-blue.svg)]()
[![ansibleversions](https://img.shields.io/badge/ansible-2.4-red.svg)]()
[![ver](https://img.shields.io/badge/release-v1.2-red.svg)]()



# Usage:



```python

# _*_ encoding=utf-8 _*_



__author__ = 'weizhen'



from ansibleApi import MyApi



# hostfile 可以是一个静态文件, 也可以是一个get_inventory文件 (最后把取到的内容print出来)

api = MyApi(<hostfile>)



# 执行 Ad-hoc

api.run(<host>, <module>, <module_args>)



# 执行 playbook

api.run_playbook(<host>, <playbookfile>)



# 获取返回值

api.get_result() # 字典

api.get_json() # json

```



# hosts 文件格式



- ini



```

[group1]

host1 ansible_ssh_host = xxx.xx.xx.xxx

```



- dict



```

{

    'group1': {

        'hosts': [

            '1.1.1.1', '2.2.2.2'

        ],

        'vars': {

            'some_vars': 'some_values'

        },

        'children': [

            'other_group'

        ]

    },

    'group2': {

        'hosts': {

            'host1': {

                'ansible_ssh_host': '1.1.1.1',

                'ansible_ssh_pass': '123456',

                'ansible_ssh_user': 'root'

            },

            'host2': {

                'ansible_ssh_host': '2.2.2.2',

                'ansible_ssh_pass': '123456'

            }

        }

    }

}

```

