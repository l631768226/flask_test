from model import InfoData
from utils import CommonMethod
import json


def newsDetail(id):
    resData = {'code': 1, 'msg': '', 'data': None, 'paging': None}
    NewsInfo = InfoData.NewsInfo
    newsData = NewsInfo.query.filter(NewsInfo.id == id).all()
    if newsData:
        resultData = CommonMethod.convertNewsInfo(newsData[0])
        resData['data'] = resultData
    else:
        resData['code'] = -1
        resData['msg'] = '传入数据有误'
    return json.dumps(resData, ensure_ascii=False)