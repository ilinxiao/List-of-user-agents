import requests as req
from bs4 import BeautifulSoup
import time
import os

from user_agents import parse
from check_ua import check_ua


def save(br, ua, file):
    with open(file,'a') as f:
        f.write(ua+'\n')
        
def save_list(list, file):
    with open(file, 'wt') as f:
        f.write('\r'.join(list))
    
def getUa(br):

    url = 'http://www.useragentstring.com/pages/useragentstring.php?name='+br
    r = req.get(url)
    user_agent_list = []
    
    if r.status_code == 200:
        soup = BeautifulSoup(r.content,'html.parser')
    else:
        soup = False

    if soup:
        div = soup.find('div',{'id':'liste'})
        lnk = div.findAll('a')

        for i in lnk:
            try:
                if check_ua(i.text):
                    user_agent_list.append(i.text)
                else:
                    pass
                    print('%s' % i.text)
            except Exception as e:
                print('no ua, %s' % e)
    else:
        print('No soup for '+br)
    return user_agent_list


if __name__ == '__main__':
    # lst = ['Firefox','Internet+Explorer','Opera','Safari','Chrome','Edge','Android+Webkit+Browser']
    lst = ['Firefox', 'Chrome', 'Safari']

    user_agent_list = []
    for i in range(0, len(lst)):
        user_agent_list.extend(getUa(lst[i]))
        if i<len(lst)-1:
            time.sleep(20)
        
        
    file = 'user_agent.txt'
    try:
        if os.path.exists(file):
            os.remove(file)
        save_list(user_agent_list, file)
    except:
        pass
        