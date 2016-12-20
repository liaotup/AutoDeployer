#! /bin/bash
# -*- coding: utf-8 -*
import urlparse
import os
import comm_log
import tornado.ioloop
import tornado.web
import tornado.options
from tornado.options import define, options

# 监听端口
define("port", default=8978, help="run on the given port", type=int)
# 日志输出
define("log", default=comm_log.get_logging('gohook'))

token = '888v8d6d66d7f8f87d6df78f9f9f9d8f'
script = '/home/AutoDeployer/'

def pull(projectName, isNeedReploy):
    print 'AutoDeployer: Pull Project:'+projectName
    os.system('sh '+script+'gitPull.sh ' + projectName)
    if isNeedReploy == "true":
        os.system('sh '+script+'tomcatDeloyer.sh ' + projectName)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        result = urlparse.urlparse(self.request.uri)
        params = urlparse.parse_qs(result.query, True)
        print 'AutoDeployer: Token name:' + params.get('token')[0]
        print 'AutoDeployer: Project name:' + params.get('projectName')[0]
        print 'AutoDeployer: isNeedReploy:' + params.get('isNeedReploy')[0]
        if params.get('token')[0] == token:
            pull(params.get('projectName')[0], params.get('isNeedReploy')[0])
            self.write('Service has sense of it:'+params.get('projectName')[0] + " isNeedToRedeploy:" + params.get('isNeedReploy')[0])
        else:
            print 'AutoDeployer: request Error'
            self.write('Request Error!')


application = tornado.web.Application([
    (r"/gohook", MainHandler),
])

if __name__ == "__main__":
    print 'AutoDeployer: System Inited!'
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
