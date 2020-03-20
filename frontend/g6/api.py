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

            {"id":"基础","label":"基础","class":"c1"},
            {"id":"成员","label":"成员","class":"c1"},
            {"id":"模板","label":"模板","class":"c1"},
            {"id":"收藏","label":"收藏","class":"c1"},
            {"id":"提醒事项","label":"提醒事项","class":"c1"},
            {"id":"项目客户","label":"项目客户","class":"c1"},
            {"id":"计时","label":"计时","class":"c1"},
            {"id":"阶段","label":"阶段","class":"c1"},
            {"id":"其他","label":"其他","class":"c1"},

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

            {"id": "所有案件成员", "label": "所有案件成员", "class": "c2"},
            {"id": "成员查询", "label": "成员查询", "class": "c2"},
            {"id": "成员列表", "label": "成员列表", "class": "c2"},
            {"id": "项目成员（剔除离职成员）", "label": "项目成员（剔除离职成员）", "class": "c2"},
            {"id": "同一律所的项目成员", "label": "同一律所的项目成员", "class": "c2"},
            {"id": "项目成员（包括离职成员）", "label": "项目成员（包括离职成员）", "class": "c2"},

            {"id": "测试", "label": "测试", "class": "c3"},

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

            {"source": "成员", "target": "所有案件成员", "weight": 2},
            {"source": "成员", "target": "成员查询", "weight": 2},
            {"source": "成员", "target": "成员列表", "weight": 2},
            {"source": "成员", "target": "项目成员（剔除离职成员）", "weight": 2},
            {"source": "成员", "target": "同一律所的项目成员", "weight": 2},
            {"source": "成员", "target": "项目成员（包括离职成员）", "weight": 2},

            {"source": "项目列表", "target": "测试", "weight": 1},
            {"source": "所有案件成员", "target": "测试", "weight": 1},

        ]}

