from model import InfoData
from utils import CommonMethod
import json


def proDetail(id):
    resData = {'code': 1, 'msg': '', 'data': None, 'paging': None}
    resultData = {'proDetail': {}, 'proImgList': []}

    if id is None:
        resData['code'] = -1
        resData['msg'] = '传入参数有误'
        return json.dumps(resData, ensure_ascii=False)

    ProInfo = InfoData.ProInfo
    proList = ProInfo.query.filter(ProInfo.id == id).all()
    proListData = CommonMethod.convertProInfoList(proList)
    proData = None
    if proListData:
        proData = proListData[0]
    else:
        resData['code'] = -1
        resData['msg'] = '数据不存在'
        return json.dumps(resData, ensure_ascii=False)
    resultData['proDetail'] = proData

    ProImg = InfoData.ProImg
    proImgList = ProImg.query.filter(ProImg.pro_id == id).all()
    proImgListData = CommonMethod.convertProImgList(proImgList)
    proImgData = []
    if proImgListData:
        proImgData = proImgListData
    resultData['proImgList'] = proImgData
    resData['data'] = resultData
    return json.dumps(resData, ensure_ascii=False)


def proList(proClass, page, pageSize):

    resData = {'code': 1, 'msg': '', 'data': [], 'paging': None}
    pageInfo = {'pageNum': 1, 'pageSize': 1, 'size': 1, 'total': 1, 'pages': 1}
    ProInfo = InfoData.ProInfo
    proList = None
    if proClass is None or proClass == '':
        print("all")
        proList = ProInfo.query.order_by(ProInfo.sort.asc())
    else:
        proList = ProInfo.query.filter_by(ProInfo.pro_class == proClass).order_by(ProInfo.sort.asc())
    if proList:
        if page == 0 or pageSize == 0:
            resData['data'] = InfoData.query_set_to_list(proList)
        else:
            paginate = proList.paginate(page=page, per_page=pageSize, error_out=False)
            pagedata = paginate.items  # 当前页数的记录列表
            total = paginate.total
            pageNum = paginate.page
            pageInfo['pageNum'] = pageNum
            pageInfo['total'] = total
            pageInfo['pageSize'] = pageSize
            pageInfo['pages'] = paginate.pages
            resData['data'] = InfoData.query_set_to_list(pagedata)
            resData['paging'] = pageInfo
    else:
        resData['code'] = -1
        resData['msg'] = '数据不存在'
    return json.dumps(resData, ensure_ascii=False)