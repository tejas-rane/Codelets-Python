import urllib2
import json
def getMovieTitles(substr):
    url="https://jsonmock.hackerrank.com/api/movies/search/?Title="+substr
    pageno=1
    moreResuls = "https://jsonmock.hackerrank.com/api/movies/search/?Title="+substr+"&page="
    #+str(pageno)
    out=[]
    response = urllib2.urlopen(moreResuls+str(pageno))
    resData = response.read()
    json_data = json.loads(resData)
    print json_data

    for i in json_data['data']:
        out.append(i['Title'])

    total_pages = json_data['total_pages']
    while pageno<total_pages:
        pageno += 1
        response = urllib2.urlopen(moreResuls + str(pageno))
        resData = response.read()
        json_data = json.loads(resData)
        print json_data

        for i in json_data['data']:
            out.append(i['Title'])

    print out

getMovieTitles("spiderman")