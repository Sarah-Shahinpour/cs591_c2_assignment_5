# Assumptions: 
# 1) url will always contain protocol and domain separated by "://" while path is optional. 
# 2) domain and path will be separated by "/"
# 3) protocol, domain, path will not contain "/" as part of their string 

# Resource: https://stackoverflow.com/questions/33657463/python-test-to-check-instance-type/33657828 

class Problem1():
    def __init__(self): 
        pass

    def urlSplit(self, url):
        protocol, lastHalf = url.split("://")
        domain, path = lastHalf.split("/")
        return [protocol, domain, path]