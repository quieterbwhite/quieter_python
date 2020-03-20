from fastapi import FastAPI, Response
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1",
    "http://127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home(response: Response):
    response.headers["access-control-allow-origin"] = "*"
    return {
        "nodes":[
            {"id":"项目","label":"项目","class":"c0"},
            # 模块
            {"id":"基础","label":"基础","class":"c1"},
            {"id":"成员","label":"成员","class":"c1"},
            {"id":"模板","label":"模板","class":"c1"},
            {"id":"收藏","label":"收藏","class":"c1"},
            {"id":"提醒事项","label":"提醒事项","class":"c1"},
            {"id":"项目客户","label":"项目客户","class":"c1"},
            {"id":"计时","label":"计时","class":"c1"},
            {"id":"阶段","label":"阶段","class":"c1"},
            {"id":"其他","label":"其他","class":"c1"},
            # 接口 - 基础
            {"id":"项目列表","label":"项目列表","class":"c2"},
            {"id":"分类统计","label":"分类统计","class":"c2"},
            {"id":"业务类型","label":"业务类型","class":"c2"},
            {"id":"项目详情","label":"项目详情","class":"c2"},
            {"id":"委托方身份","label":"委托方身份","class":"c2"},
            {"id":"新建项目","label":"新建项目","class":"c2"},
            {"id":"分组业务类型统计","label":"分组业务类型统计","class":"c2"},
            {"id":"协办的律所","label":"协办的律所","class":"c2"},
            {"id":"编辑项目权限","label":"编辑项目权限","class":"c2"},
            {"id":"新建标签","label":"新建标签","class":"c2"},
            {"id":"标签列表","label":"标签列表","class":"c2"},
            # 接口 - 成员
            {"id": "所有案件成员", "label": "所有案件成员", "class": "c2"},
            {"id": "成员查询", "label": "成员查询", "class": "c2"},
            {"id": "成员列表", "label": "成员列表", "class": "c2"},
            {"id": "项目成员（剔除离职成员）", "label": "项目成员（剔除离职成员）", "class": "c2"},
            {"id": "同一律所的项目成员", "label": "同一律所的项目成员", "class": "c2"},
            {"id": "项目成员（包括离职成员）", "label": "项目成员（包括离职成员）", "class": "c2"},
            # 接口 - 模板
            {"id": "检查指定模板", "label": "检查指定模板", "class": "c2"},
            {"id": "指定案件模板", "label": "指定案件模板", "class": "c2"},
            {"id": "可选模板", "label": "可选模板", "class": "c2"},
            {"id": "是否导入完成", "label": "是否导入完成", "class": "c2"},
            # 接口 - 收藏
            {"id": "收藏项目", "label": "收藏项目", "class": "c2"},
            {"id": "取消收藏", "label": "取消收藏", "class": "c2"},

            # 接口 - 提醒事项
            {"id": "添加提醒", "label": "添加提醒", "class": "c2"},
            {"id": "获取提醒", "label": "获取提醒", "class": "c2"},
            {"id": "更新提醒", "label": "更新提醒", "class": "c2"},

            # 接口 - 项目客户
            {"id": "客户信息", "label": "客户信息", "class": "c2"},
            {"id": "客户列表", "label": "客户列表", "class": "c2"},
            {"id": "添加客户", "label": "添加客户", "class": "c2"},
            {"id": "客户详情", "label": "客户详情", "class": "c2"},
            {"id": "客户同步", "label": "客户同步", "class": "c2"},
            {"id": "从客户获取项目", "label": "从客户获取项目", "class": "c2"},

            # 接口 - 计时
            {"id": "计时类型列表", "label": "计时类型列表", "class": "c2"},
            {"id": "新建计时类型", "label": "新建计时类型", "class": "c2"},
            {"id": "计时详情", "label": "计时详情", "class": "c2"},
            {"id": "全局计时列表", "label": "全局计时列表", "class": "c2"},

            # 接口 - 阶段
            {"id": "阶段列表", "label": "阶段列表", "class": "c2"},
            {"id": "新建阶段", "label": "新建阶段", "class": "c2"},
            {"id": "阶段排序", "label": "阶段排序", "class": "c2"},
            {"id": "任务列表", "label": "任务列表", "class": "c2"},
            {"id": "任务详情", "label": "任务详情", "class": "c2"},
            {"id": "更新任务排序", "label": "更新任务排序", "class": "c2"},
            {"id": "更新任务到阶段", "label": "更新任务到阶段", "class": "c2"},
            {"id": "添加关注", "label": "添加关注", "class": "c2"},
            {"id": "添加指派人", "label": "添加指派人", "class": "c2"},
            {"id": "获取任务评论", "label": "获取任务评论", "class": "c2"},
            {"id": "添加评论", "label": "添加评论", "class": "c2"},
            {"id": "任务同步设置", "label": "任务同步设置", "class": "c2"},
            {"id": "搜索阶段和任务", "label": "搜索阶段和任务", "class": "c2"},
            {"id": "新建检查项", "label": "新建检查项", "class": "c2"},
            {"id": "检查项排序", "label": "检查项排序", "class": "c2"},
            {"id": "阶段和任务列表", "label": "阶段和任务列表", "class": "c2"},

            # 接口 - 其他

            # 表 - 项目
            {"id": "项目与标签的映射关系", "label": "项目与标签的映射关系", "class": "db_project_class"},
            {"id": "项目组织节点关联表", "label": "项目组织节点关联表", "class": "db_project_class"},
            {"id": "项目客户联系人映射表", "label": "项目客户联系人映射表", "class": "db_project_class"},
            {"id": "项目客户映射表", "label": "项目客户映射表", "class": "db_project_class"},
            {"id": "项目与角色编码表", "label": "项目与角色编码表", "class": "db_project_class"},
            {"id": "项目基础表", "label": "项目基础表", "class": "db_project_class"},
            {"id": "任务用户表", "label": "任务用户表", "class": "db_project_class"},
            {"id": "用户收藏项目关联表", "label": "用户收藏项目关联表", "class": "db_project_class"},
            {"id": "项目成员表", "label": "项目成员表", "class": "db_project_class"},
            {"id": "项目协办成员表", "label": "项目协办成员表", "class": "db_project_class"},
            {"id": "项目业务类型配置表", "label": "项目业务类型配置表", "class": "db_project_class"},
            {"id": "诉讼项目扩展表", "label": "诉讼项目扩展表", "class": "db_project_class"},
            {"id": "诉讼项目对方当事人表", "label": "诉讼项目对方当事人表", "class": "db_project_class"},
            {"id": "项目与标签的映射关系表", "label": "项目与标签的映射关系表", "class": "db_project_class"},
            {"id": "用户收藏项目关联表", "label": "用户收藏项目关联表", "class": "db_project_class"},

            # 表 - 用户
            {"id": "律所组织节点表", "label": "律所组织节点表", "class": "db_user_class"},
            {"id": "角色表", "label": "角色表", "class": "db_user_class"},

            # 表 - 审批
            {"id": "审批事件表", "label": "审批事件表", "class": "db_approve_class"},

            # 表 - 客户管理
            {"id": "客户信息表", "label": "客户信息表", "class": "db_approve_class"},
            {"id": "客户联系人表", "label": "客户联系人表", "class": "db_approve_class"},

            # 表 - 文件

            # 表 - 项目

        ],
        "edges":[
            {"source":"项目","target":"基础","weight":3},
            {"source":"项目","target":"成员","weight":3},
            {"source":"项目","target":"模板","weight":3},
            {"source":"项目","target":"收藏","weight":3},
            {"source":"项目","target":"提醒事项","weight":3},
            {"source":"项目","target":"项目客户","weight":3},
            {"source":"项目","target":"计时","weight":3},
            {"source":"项目","target":"阶段","weight":3},
            {"source":"项目","target":"其他","weight":3},
            # 接口 - 基础
            {"source": "基础", "target": "项目列表", "weight": 2},
            {"source": "基础", "target": "分类统计", "weight": 2},
            {"source": "基础", "target": "业务类型", "weight": 2},
            {"source": "基础", "target": "项目详情", "weight": 2},
            {"source": "基础", "target": "委托方身份", "weight": 2},
            {"source": "基础", "target": "新建项目", "weight": 2},
            {"source": "基础", "target": "分组业务类型统计", "weight": 2},
            {"source": "基础", "target": "协办的律所", "weight": 2},
            {"source": "基础", "target": "编辑项目权限", "weight": 2},
            {"source": "基础", "target": "新建标签", "weight": 2},
            {"source": "基础", "target": "标签列表", "weight": 2},
            # 接口 - 成员
            {"source": "成员", "target": "所有案件成员", "weight": 2},
            {"source": "成员", "target": "成员查询", "weight": 2},
            {"source": "成员", "target": "成员列表", "weight": 2},
            {"source": "成员", "target": "项目成员（剔除离职成员）", "weight": 2},
            {"source": "成员", "target": "同一律所的项目成员", "weight": 2},
            {"source": "成员", "target": "项目成员（包括离职成员）", "weight": 2},
            # 接口 - 模板
            {"source": "模板", "target": "检查指定模板", "weight": 2},
            {"source": "模板", "target": "指定案件模板", "weight": 2},
            {"source": "模板", "target": "可选模板", "weight": 2},
            {"source": "模板", "target": "是否导入完成", "weight": 2},
            # 接口 - 收藏
            {"source": "收藏", "target": "收藏项目", "weight": 2},
            {"source": "收藏", "target": "取消收藏", "weight": 2},
            # 接口 - 提醒事项
            {"source": "提醒事项", "target": "添加提醒", "weight": 2},
            {"source": "提醒事项", "target": "获取提醒", "weight": 2},
            {"source": "提醒事项", "target": "更新提醒", "weight": 2},
            # 接口 - 项目客户
            {"source": "项目客户", "target": "客户信息", "weight": 2},
            {"source": "项目客户", "target": "客户列表", "weight": 2},
            {"source": "项目客户", "target": "添加客户", "weight": 2},
            {"source": "项目客户", "target": "客户详情", "weight": 2},
            {"source": "项目客户", "target": "客户同步", "weight": 2},
            {"source": "项目客户", "target": "从客户获取项目", "weight": 2},
            # 接口 - 计时
            {"source": "计时", "target": "计时类型列表", "weight": 2},
            {"source": "计时", "target": "新建计时类型", "weight": 2},
            {"source": "计时", "target": "计时详情", "weight": 2},
            {"source": "计时", "target": "全局计时列表", "weight": 2},
            # 接口 - 阶段
            {"source": "阶段", "target": "阶段列表", "weight": 2},
            {"source": "阶段", "target": "新建阶段", "weight": 2},
            {"source": "阶段", "target": "阶段排序", "weight": 2},
            {"source": "阶段", "target": "任务列表", "weight": 2},
            {"source": "阶段", "target": "任务详情", "weight": 2},
            {"source": "阶段", "target": "更新任务排序", "weight": 2},
            {"source": "阶段", "target": "更新任务到阶段", "weight": 2},
            {"source": "阶段", "target": "添加关注", "weight": 2},
            {"source": "阶段", "target": "添加指派人", "weight": 2},
            {"source": "阶段", "target": "获取任务评论", "weight": 2},
            {"source": "阶段", "target": "添加评论", "weight": 2},
            {"source": "阶段", "target": "任务同步设置", "weight": 2},
            {"source": "阶段", "target": "搜索阶段和任务", "weight": 2},
            {"source": "阶段", "target": "新建检查项", "weight": 2},
            {"source": "阶段", "target": "检查项排序", "weight": 2},
            {"source": "阶段", "target": "阶段和任务列表", "weight": 2},

            # 接口 - 其他

            # 项目 - 项目列表
            {"source": "项目列表", "target": "项目与标签的映射关系", "weight": 5},
            {"source": "项目列表", "target": "项目组织节点关联表", "weight": 5},
            {"source": "项目列表", "target": "项目客户联系人映射表", "weight": 5},
            {"source": "项目列表", "target": "项目客户映射表", "weight": 5},
            {"source": "项目列表", "target": "项目与角色编码表", "weight": 5},
            {"source": "项目列表", "target": "项目基础表", "weight": 5},
            {"source": "项目列表", "target": "任务用户表", "weight": 5},
            {"source": "项目列表", "target": "用户收藏项目关联表", "weight": 5},
            {"source": "项目列表", "target": "律所组织节点表", "weight": 5},
            {"source": "项目列表", "target": "角色表", "weight": 5},
            {"source": "项目列表", "target": "审批事件表", "weight": 5},
            # 项目 - 分类统计
            {"source": "分类统计", "target": "律所组织节点表", "weight": 5},
            {"source": "分类统计", "target": "项目组织节点关联表", "weight": 5},
            {"source": "分类统计", "target": "项目基础表", "weight": 5},
            {"source": "分类统计", "target": "项目与角色编码表", "weight": 5},
            {"source": "分类统计", "target": "审批事件表", "weight": 5},
            # 项目 - 业务类型
            {"source": "业务类型", "target": "项目业务类型配置表", "weight": 5},
            # 项目 - 项目详情
            {"source": "项目详情", "target": "项目基础表", "weight": 5},
            {"source": "项目详情", "target": "项目与角色编码表", "weight": 5},
            {"source": "项目详情", "target": "项目组织节点关联表", "weight": 5},
            {"source": "项目详情", "target": "律所组织节点表", "weight": 5},
            {"source": "项目详情", "target": "项目业务类型配置表", "weight": 5},
            {"source": "项目详情", "target": "诉讼项目扩展表", "weight": 5},
            {"source": "项目详情", "target": "诉讼项目对方当事人表", "weight": 5},
            {"source": "项目详情", "target": "项目客户映射表", "weight": 5},
            {"source": "项目详情", "target": "客户信息表", "weight": 5},
            {"source": "项目详情", "target": "客户联系人表", "weight": 5},
            {"source": "项目详情", "target": "项目与标签的映射关系表", "weight": 5},
            {"source": "项目详情", "target": "律所组织节点表", "weight": 5},
            {"source": "项目详情", "target": "用户收藏项目关联表", "weight": 5},
            # 项目 - 委托方身份
            # 项目 - 新建项目
            # 项目 - 分组业务类型统计
            # 项目 - 协办的律所
            # 项目 - 编辑项目权限
            # 项目 - 新建标签
            # 项目 - 标签列表

            # 成员 - 所有案件成员
            # 成员 - 成员查询
            # 成员 - 成员列表
            # 成员 - 项目成员（剔除离职成员）
            # 成员 - 同一律所的项目成员
            # 成员 - 项目成员（包括离职成员）

            # 模板 - 检查指定模板
            # 模板 - 指定案件模板
            # 模板 - 可选模板
            # 模板 - 是否导入完成

            # 收藏 - 收藏项目
            # 收藏 - 取消收藏

            # 提醒事项 - 添加提醒
            # 提醒事项 - 获取提醒
            # 提醒事项 - 更新提醒

            # 项目客户 - 客户信息
            # 项目客户 - 客户列表
            # 项目客户 - 添加客户
            # 项目客户 - 客户详情
            # 项目客户 - 客户同步
            # 项目客户 - 从客户获取项目

            # 成员查询
            {"source": "成员查询", "target": "项目成员表", "weight": 5},
            {"source": "成员查询", "target": "项目协办成员表", "weight": 5},

        ]}

