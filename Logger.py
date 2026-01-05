# 로그 담당 클래스
from pathlib import Path

class Logger:
    
    def __init__(self, dir_name: str):
        self._directory = dir_name
        self._encoding_list: list[str] = ['utf-8','cp949','utf-16']
        self._log_path = Path(dir_name)
    
    def get_log(self, filename: Path):
        for i in range(len(self._encoding_list)):
            with open(filename, "rt", encoding=self._encoding_list[i]) as file:
                try:
                    for line in file:
                        yield line
                except Exception as e:
                    print(f"There was an error while reading the game log: {e}")
                    pass
    
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
        dir_iter = self._log_path.iterdir()
        try:    
            for file in dir_iter:
                await self.print_log(file)
        except Exception as e:
            print(f"There is something wrong: {e}")
