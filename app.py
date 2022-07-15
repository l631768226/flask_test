from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import json

from service import IndexService, ProService, NewsService
from model import InfoData
from config import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)


@app.route("/")
def hello():
    return "OK"


@app.route("/index/info", methods=['post'])
def indexInfo():
    return IndexService.indexInfo()


@app.route("/news/detail", methods=['post'])
def newsDetail():
    data = request.get_data()
    datajson = json.loads(data)
    id = datajson['data']['id']
    return NewsService.newsDetail(id)


@app.route("/pro/detail", methods=['post'])
def proDetail():
    data = request.get_data()
    datajson = json.loads(data)
    id = datajson['data']['id']
    return ProService.proDetail(id)


@app.route("/pro/list", methods=['post'])
def proList():
    requestData = request.get_data()
    if requestData:
        dataJson = json.loads(requestData)
        data = dataJson.get('data', None)
        if data is not None:
            proClass = data.get('proClass', '')
            page = data.get('page', '0')
            pageSize = data.get('pageSize', '0')
            return ProService.proList(proClass, int(page), int(pageSize))
    else:
        resData = {'code': -1, 'msg': '传入数据有误', 'data': [], 'paging': None}
        return json.dumps(resData, ensure_ascii=False)


@app.route("/test1")
def sqlModel():
    result = InfoData.NewsInfo.query.all()
    for newsinfo in result:
        # print('title:%s' % newsinfo.title)
        print(json.dumps(InfoData.query_set_to_dict(newsinfo), ensure_ascii=False))
    return json.dumps(InfoData.query_set_to_list(result), ensure_ascii=False)


@app.route("/test2")
def objModel():
    rule = r'同志'
    result = db.session.query(InfoData.NewsInfo).filter(InfoData.NewsInfo.title.like('%' + rule + '%')).all()
    return json.dumps(InfoData.query_set_to_list(result), ensure_ascii=False)


@app.route("/test3", methods=['post'])
def postJson():
    resultStr = {'code': 1, 'msg': '', 'data': None, 'paging': None}
    pageInfo = {'pageNum': 1, 'pageSize': 1, 'size': 1, 'total': 1, 'pages': 1}
    data = request.get_data()
    if data is None:
        return "error"
    datajson = json.loads(data)
    page = int(datajson['page'])
    page_size = int(datajson['pageSize'])
    paginate = InfoData.NewsInfo.query.order_by('id').paginate(page=page, per_page=page_size, error_out=False)
    pagedata = paginate.items  # 当前页数的记录列表
    total = paginate.total
    pageNum = paginate.page
    pageInfo['pageNum'] = pageNum
    pageInfo['total'] = total
    pageInfo['pageSize'] = page_size
    pageInfo['pages'] = paginate.pages
    # pagination = Pagination(page=page, total=total, per_page=page_size, query=None, items= None)

    resultStr['data'] = InfoData.query_set_to_list(pagedata)
    resultStr['paging'] = pageInfo
    # result = db.session.query(InfoData.NewsInfo).filter(InfoData.NewsInfo.id == id)
    # resultStr['data'] = InfoData.query_set_to_list(result)
    return json.dumps(resultStr, ensure_ascii=False)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
