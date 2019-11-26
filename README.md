# kmsbackEnd

## 使用

```bash
cd kmsBackend
docker-compose up -d
```

flask服务端口映射在宿主机的5000

## 接口

### 主页

- [GET] /status

  | Response        |
  | --------------- |
  | {"status":true} |

  获取kms服务状态

- [GET] /content/\<name\>

  获取各个板块内容

  | 参数 | Value                         | Response                          |
  | ---- | ----------------------------- | --------------------------------- |
  | name | intro \| usage \| key \| ed2k | {"status":true,"content":"xxxxx"} |

### 登录

- [POST] /login

  | 参数     | Request         |
  | -------- | --------------- |
  | password | password=xxxxxx |

### 管理[login_required]

- [POST] /content/\<name\>

  设置各个板块的内容

  | 参数 | Value                         | Response            |
  | ---- | ----------------------------- | ------------------- |
  | name | intro \| usage \| key \| ed2k | {"content":"xxxxx"} |

  

- [POST] /control

  控制kms服务的开关

  ```
  Request规范
  content-type:applicatin/json
  data:{"action"："start"}
  ```

  | 参数   | Value                    | Response        |
  | ------ | ------------------------ | --------------- |
  | action | start \| stop \| restart | {"status":true} |

  

- [GET] /logs

  | Response                                                     |
  | ------------------------------------------------------------ |
  | [<br />{"time": "2019-11-26 05:02:24", <br />"ip": "172.22.0.3:56698",<br /> "request": "Protocol version                : 6.0\nClient is a virtual machine     : No\nLicensing status                : 2 (OOB grace)\nRemaining time (0 = forever)    : 43200 minutes\nApplication ID                  : 55c92734-d682-4d71-983e-d6ec3f16059f (Unknown)\nSKU ID (aka Activation ID)      : 8de8eb62-bbe0-40ac-ac17-f75595071ea3 (Unknown)\nKMS ID (aka KMS counted ID)     : 8449b1fb-f0ea-497a-99ab-66ca96e9a0f5 (Unknown)\nClient machine ID               : 0d2dd5f1-6b08-4ae3-821d-534cf1f183c9\nPrevious client machine ID      : 00000000-0000-0000-0000-000000000000\nClient request timestamp (UTC)  : 2019-11-26 05:02:24\nWorkstation name                : mail.microsoft.es\nN count policy (minimum clients): 5\n>>> Sending response, ePID source = randomized at program start\nProtocol version                : 6.0\nKMS host extended PID           : 03612-00206-554-689679-03-2110-17763.0000-0132019\nKMS host Hardware ID            : 3A1C049600B60076\nClient machine ID               : 0d2dd5f1-6b08-4ae3-821d-534cf1f183c9\nClient request timestamp (UTC)  : 2019-11-26 05:02:24\nKMS host current active clients : 50\nRenewal interval policy         : 10080\nActivation interval policy      : 120\n\n"},<br />{xxxx},<br />...<br />] |
  
  获取kms日志