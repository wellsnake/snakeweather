Snake的天气小助手
============

每天定时将中国天气网的天气信息同步发送到绑定的微博上
用法
-----------
1.  访问 [Snake的天气小助手](http://weather.wellsnake.com)
2.  点击登陆
3.  系统会自动跳转到微博授权页面，点击“授权”即可

部署
-----------
1. 去新浪开放平台申请一个新的app，然后获得相应的“APP_KEY”和“APP_SECRET”
2. 修改config.py文件内的“APP_KEY” “APP_SECRET” “CALLBACK_URL”相应的值
3. 将代码部署到Google appengine上就可以啦>_<

Todo List
-----------
1. 将程序部署到Goole appengine上
2. 优化代码
3. 可选择城市
4. 如果微博授权过期，自动延期
5. 可以选择需要@的用户
6. 根据天气内容的不同显示不同的表情
7. 可以自定义输出到微博的文字内容


