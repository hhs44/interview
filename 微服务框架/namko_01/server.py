from nameko.rpc import rpc


# 创建服务类
class GeetingService:
    # 定义服务名称
    name = "greeting_service"

    @rpc  # 进入接口的标记
    def hello(self, name):
        return f"Hello {name}"
