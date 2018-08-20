路书云 TOS
=========

```shell
gunicorn config.wsgi:application -k egg:meinheld#gunicorn_worker -w 4 -b 0.0.0.0:5000

gunicorn config.wsgi:application -k gevent -w 4 -b 0.0.0.0:5000


dropdb project
createuser project -P
createdb project -O project -E UTF8 -e
psql -U project -d project -h 127.0.0.1

```


[-] 支付模块 (payment, wechat, alipay)
[x] 队列服务 (celery)
[x] 搜索模块 (haystack)
[x] 分布存储 (minio, qiniu, aliyun_oss2)
[x] 缩量图片 (thumbor)
[x] 社会登录 (socials)
[x] 开放接口 (openapi)
[x] 登录接口 (rest_auth, jwt_auth)
[x] 微信接口 (wechat_mps, wechat_app)

```
# 读取中行外币汇率 1-9页
df = pd.read_html('http://www.boc.cn/sourcedb/whpj/index_1.html', header=1)
```






