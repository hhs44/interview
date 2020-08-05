import logging
# 拦截ip，并写入log
from django.http import HttpResponseForbidden

from simpledemo import settings

logging.basicConfig(
    format='%(asctime)s - %(pathname)s[%(lineno)d] - %(levelname)s: %(message)s',
    level=logging.INFO)


# ip拦截中间件实现
class SimpleMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response
        self.apiLogger = logging.getLogger('web.log')

    def __call__(self, request):
        # 拦截黑名单里的IP并纪录进日志
        if request.META['REMOTE_ADDR'] in getattr(settings, "BLACKLIST", []):
            # 以info级别存储信息
            self.apiLogger.info(f"{request.META['REMOTE_ADDR']} in BLACKLIST")
            return HttpResponseForbidden(request)
        response = self.get_response(request)

        return response
