# 로그 담당 클래스
from pathlib import Path

class Logger:
    
    def __init__(self, dir_name: str):
        self._directory = dir_name
        self._encoding_list: list[str] = ['utf-8','cp949','utf-16']
        self._log_path = Path(dir_name)
    
    def get_log(self, filename: Path):
        for encoder in self._encoding_list:
            try:
                with open(filename, "rt", encoding=encoder) as file:
                    for line in file:
                        yield line
                break
            except UnicodeDecodeError:
                continue
    
    async def print_log(self, filename: Path):
        log_generator = self.get_log(filename)
        while True:
            try:
                item = next(log_generator)
                print(item)
            except StopIteration:
                print("로그는 여기까지입니다.")
                break
    
    async def print_every_log(self):
        for file in self._log_path.iterdir():
            try:
                await self.print_log(file)
            except Exception as e:
                print(f"파일 처리 중 오류 발생 ({file}) : {e}")
