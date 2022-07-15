def convertNewsInfoList(newsList):
    newsListData = []
    if newsList is not None and newsList:
        for newsData in newsList:
            newsDict = {'id': newsData.id, 'title': newsData.title, 'timeStr': newsData.time_str,
                        'info': newsData.info, 'content': newsData.content, 'imgPath': newsData.img_path}

            newsListData.append(newsDict)
    return newsListData


def convertProImgList(proImgList):
    proImgListData = []
    if proImgList is not None and proImgList:
        for proImgData in proImgList:
            proImgDict = {'id': proImgData.id, 'proId': proImgData.pro_id, 'imgPath': proImgData.img_path,
                          'sort': proImgData.sort, 'delFlag': proImgData.del_flag}
            proImgListData.append(proImgDict)
    return proImgListData


def convertProInfoList(proList):
    proListData = []
    if proList is not None and proList:
        for proData in proList:
            proDict = {'id': proData.id, 'proName': proData.pro_name, 'deptName': proData.dept_name,
                       'proLabels': proData.pro_labels,
                       'proPrin': proData.pro_prin, 'contant': proData.contant, 'proDes': proData.pro_des,
                       'proFunc': proData.pro_func,
                       'proCase': proData.pro_case, 'proInfo': proData.pro_info, 'proVedio': proData.pro_vedio,
                       'proClass': proData.pro_class, 'proImg': proData.pro_img, 'sort': proData.sort}
            proListData.append(proDict)
    return proListData


def convertNewsInfo(newsData):
    newsInfoData = {}
    if newsData is not None:
        newsInfoData = {'id': newsData.id, 'title': newsData.title, 'timeStr': newsData.time_str,
                    'info': newsData.info, 'content': newsData.content, 'imgPath': newsData.img_path}
    return newsInfoData