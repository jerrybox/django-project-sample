django-project-Sample:
----------------------
The sample project based on django==1.11 and python36.


super user:
-----------
```
admin
password123
```

change the remote repository url:
---------------------------------
git remote set-url origin https://github.com/jerrybox/new_project.git



API 定义规范：
-------------

1. XX数据查询

    * 路径：/query
    * 方式：GET
    * 功能：根据条件进行区域数据查询，返回结果
    * 请求参数：

        | 参数名称   | 是否必须 | 示例  | 备注 |
        | -------- |:-------:| ----:| :-----|
        | id       | 否      | 61000    | 区域编号 |
        | depth    | 否      |   3      | 获取层级深度，默认1，结果顶级为西安，depth为2时，西安下级区域也需返回 |
        | keywords | 否      |    北京  | 区域名称搜索关键词 |

    * 返回数据-成功：

        ```js
        {
          "code": 0,  //返回结果代码，0表示成功，其他数值表示失败
          "message": "SUCCESS",  //返回描述
          "data": {  //返回数据主体
            "id": "610100",
            "name": "西安市",
            "districts": [
              {
                "id": "610102",
                "name": "新城区",
                "districts": []
              },
              {
                "id": "610103",
                "name": "碑林区",
                "districts": []
              }
              ……
            ]
          }
        }

        ```

    * 返回数据-失败：

        ```js
        {
          "code": 1003,  //返回结果代码，0表示成功，其他数值表示失败
          "message": "请输入查询条件",  //返回描述
        }
        ```

    * 其他错误自定义:

        ```js

        ```


测试用例：
-------------
1. testcase：

    - 查看网页
        - 翻页
        - 跳转
        - 外链
    - 过滤搜索
        - 单条件
        - 多条件
        - 准确性
        - 翻页
    - 创建对象
        - 正常创建
        - 唯一字段重复
        - 必填字段空缺
        - 异常格式
    - 修改对象
        - 正常修改
        - 唯一字段重复
        - 必填字段空缺
        - 异常格式
    - 删除对象
        - 关联对象操作
        - 物理删除
        - 逻辑删除
    - 批量操作
        - 原子性
        - 错误提示
    - 404提示信息
    - 不会出现500
    - 界面操作容错性
        - 全部输入框输入
    - 代码层面容错性
        - 恶意修改参数：修改url
        - 修改html的代码
