data = {'mime': [{'By': 'coordinates', 'x': '(969 / 1080)', 'y': '(1884 / 1920)'}], 'login': [{'By': 'id', 'locator': 'cb_privacy_agree', 'move': 'click'}, {'By': 'id', 'locator': 'tv_mobile_login', 'move': 'click'}, {'BY': 'id', 'locator': 'tv_login_tab_second', 'move': 'click'}, {'By': 'id', 'locator': 'et_login_static_account_input', 'move': 'send_keys', 'content': '15518907583'}, {'By': 'id', 'locator': 'et_login_static_password_input', 'move': 'send_keys', 'content': 'ssbai521..'}, {'By': 'id', 'locator': 'btn_login_static_commit', 'move': 'click'}], 'tqy_main': [{'By': 'xpath', 'locator': "//*[@text='借现金']", 'move': 'click'}]}


for i in data["tqy_main"]:
    print(i)
