# kmsbackEnd

## 使用

```bash
docker-compose up -d
```

flask服务端口映射在宿主机的2333

## 接口

### 主页

- [GET] /status

  获取kms服务状态

- [GET] /content/\<name\>

  获取各个板块内容

  - intro
  - usage
  - key
  - ed2k

### 登录

- [POST] /login

### 管理[login_required]

- [POST] /content/\<name\>

  设置各个板块的内容

  - intro
  - usage
  - key
  - ed2k
  - password

- <del>[POST] /control</del>del>

  控制kms服务的开关

- [GET] /logs

  获取kms日志