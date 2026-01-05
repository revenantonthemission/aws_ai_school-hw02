# 로그 담당 클래스

class Logger:
    
    def __init__(self, filename: str):
        self._filename: str = filename
        self._encoding_list: list[str] = ['utf-8','cp949','utf-16']
    
    def get_log(self):
        for i in range(len(self._encoding_list)):
            with open(self._filename, "rt", encoding=self._encoding_list[i]) as file:
                try:
                    for line in file:
                        yield line
                except Exception as e:
                    print(f"There was an error while reading the game log: {e}")
                    pass
    
    def print_log(self):
        log_generator = self.get_log()
        while True:
            try:
                item = next(log_generator)
                print(item)
            except StopIteration:
                print("로그는 여기까지입니다.")
                break