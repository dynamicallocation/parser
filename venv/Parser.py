


class Parser: 
    def __init__(self,archive,fullText,Max_Rows,queryType,is_licensed,tformat,type_license,cid):
            self.archive = archive 
            self.fullText = fullText
            self.Max_Rows = Max_Rows 
            self.queryType = queryType 
            self.tformat = tformat
            self.is_licensed = is_licensed
            self.type_license = type_license
            self.cid = cid
            self.data = []
            self.url = ""


    def getURL(): 
        return url


            
    
    def queryData():
        data['archive'] = archive
        data['fullText'] = fullText
        data['Max_Rows'] = Max_Rows 
        data['queryType'] = queryType
        data['licensed'] = is_licensed 
        data['tformat'] = tformat
        data['cid'] = cid
        buildURL['archive']()

   
        buildURL = {
            'law': buildLaw
            'arciv': buildArciv
            'crossref': buildRef
        }


    def buildLaw():
        url = 'https://api.case.law/v1/cases/435800/?full_case='+ data['fulltext']+'&format='+ data['tformat']
    
    def buildArciv():
        url = 'http://export.arxiv.org/api/query?search_query=all:'+data['queryType']+'&start=0&max_results='+data['Max_Rows']
    
    def buildRef():
        url = "http://api.crossref.org/members/98/works?filter=has-license:"+data['licensed']+",has-full-text:"+data['fullText']+"&query="+data['queryType']+"&rows="+data['Max_Rows']
  





    

            