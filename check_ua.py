from user_agents import parse

def check_ua(ua):
    user_agent = parse(ua)
    # print(user_agent.browser)
    # print(user_agent.os)
    # print(user_agent.device)
    if validate_browser(user_agent.browser) or validate_os(user_agent.os) or validate_device(user_agent.device):
        return True
    return False
    
def is_other(obj):
    if obj.family == 'Other':
        return True
    return False
    
def validate_browser(browser):
    if not is_other(browser) or browser.version or browser.version_string != '':
        return True
    return False
    
def validate_os(os):
    return validate_browser(os)

def validate_device(device):
    if not is_other(device) or device.brand or device.model:
        return True
    return False
    
if __name__ == '__main__':
    for ua in open('user_agent.txt', 'r'):
        ua = ua.strip()
        if ua:
            # print(ua)
            if not check_ua(ua):
                print('not validate:%s' % ua)