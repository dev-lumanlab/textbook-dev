from starlette.types import ASGIApp, Receive, Scope, Send
import time


class ProcessTimeHeaderMiddleware:
    """
    시간 측정을 위한 미들웨어
    """

    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        # 프로세싱 전에 scope에 start_time을 기록
        start_time = time.time()
        scope["start_time"] = start_time

        # send 함수를 래핑하여 응답 헤더에 process_time을 추가
        async def send_wrapper(message):
            if message["type"] == "http.response.start":
                headers = [(key, value) for key, value in message.get("headers", [])]
                process_time = time.time() - start_time
                headers.append((b"x-process-time", str(process_time).encode()))
                message["headers"] = tuple(headers)
            await send(message)

        # 원본 'send' 대신 'send_wrapper'를 사용하여 앱 호출
        await self.app(scope, receive, send_wrapper)
