from model import InfoData
from utils import CommonMethod
import json


def indexInfo():
    resData = {'code': 1, 'msg': '', 'data': None, 'paging': None}
    # pageInfo = {'pageNum': 1, 'pageSize': 1, 'size': 1, 'total': 1, 'pages': 1}
    qIndexListRst = {'newsList': [], 'proList': []}
    newsList = InfoData.NewsInfo.query.limit(3).all()
    newsListData = CommonMethod.convertNewsInfoList(newsList)

    proList = InfoData.ProInfo.query.limit(3).all()
    proListData = CommonMethod.convertProInfoList(proList)

    qIndexListRst['newsList'] = newsListData
    qIndexListRst['proList'] = proListData
    resData['data'] = qIndexListRst
    return json.dumps(resData, ensure_ascii=False)
