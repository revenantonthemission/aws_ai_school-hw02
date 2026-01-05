# 입력 처리 클래스

from typing import Optional, List

# 사용자 입력을 처리하는 클래스
class InputHandler:
    
    # 게임 선택하기
    @staticmethod
    def get_game_selection() -> int:
        while True:
            try:
                print("\n게임을 선택하세요:")
                print("1. 로또 6/45")
                print("2. 파워볼")
                print("3. 로그 보기")
                print("0. 종료")
                
                choice = int(input("\n선택 (0-3): ").strip())
                
                if 0 <= choice <= 3:
                    return choice
                else:
                    print("[오류] 올바른 번호를 입력하세요 (0-3)")
            except ValueError:
                print("[오류] 숫자를 입력하세요")
    
    # 초기 자금 입력
    @staticmethod
    def get_initial_budget() -> int:
        while True:
            try:
                budget = int(input("\n초기 자금 (원, 기본: 100000): ").strip() or "100000")
                if budget > 0:
                    return budget
                print("[오류] 1 이상의 숫자를 입력하세요")
            except ValueError:
                print("[오류] 올바른 숫자를 입력하세요")

    # 게임 시작/상태 확인/게임 종료 중 하나를 선택
    @staticmethod
    def get_main_menu_action() -> int:
        print("\n" + "="*40)
        print("메인 메뉴")
        print("="*40)
        print("1. 티켓 구매 (게임 시작)")
        print("2. 잔액 및 통계 확인")
        print("0. 게임 종료")
        
        while True:
            try:
                choice = int(input("\n선택 (0-2): ").strip())
                if 0 <= choice <= 2:
                    return choice
                print("[오류] 0-2 사이의 숫자를 입력하세요")
            except ValueError:
                print("[오류] 숫자를 입력하세요")

    # 구매 방식 선택
    @staticmethod
    def get_purchase_type() -> str:
        print("\n구매 방식을 선택하세요:")
        print("1. 자동 (랜덤 생성)")
        print("2. 수동 (번호 직접 입력)")
        
        while True:
            try:
                choice = int(input("\n선택 (1-2): ").strip())
                if choice == 1:
                    return 'auto'
                elif choice == 2:
                    return 'manual'
                print("[오류] 1 또는 2를 입력하세요")
            except ValueError:
                print("[오류] 숫자를 입력하세요")
    
    # 티켓 구매 개수 입력하기
    @staticmethod
    def get_ticket_count() -> int:
        while True:
            try:
                count = int(input("구매할 티켓 수: ").strip())
                if count > 0:
                    return count
                print("[오류] 1 이상의 숫자를 입력하세요")
            except ValueError:
                print("[오류] 올바른 숫자를 입력하세요")
    
    # 수동으로 번호 입력하기
    @staticmethod
    def get_numbers(count: int, min_num: int, max_num: int, 
                   manual: bool = False, prompt_msg: Optional[str] = None) -> Optional[List[int]]:
        if not manual:
            return None
        
        if prompt_msg:
            print(f"\n{prompt_msg}:")
        else:
            print(f"\n{count}개의 번호를 입력하세요 ({min_num}-{max_num}):")
        
        print(f"예: {' '.join(str(min_num + i) for i in range(count))}")
        
        while True:
            try:
                input_str = input("> ").strip()
                numbers = [int(x) for x in input_str.split()]
                
                if len(numbers) != count:
                    print(f"[오류] 정확히 {count}개의 번호를 입력하세요")
                    continue
                
                if len(set(numbers)) != count:
                    print("[오류] 중복된 번호가 있습니다")
                    continue
                
                if not all(min_num <= num <= max_num for num in numbers):
                    print(f"[오류] 모든 번호는 {min_num}~{max_num} 범위여야 합니다")
                    continue
                
                return numbers
            except ValueError:
                print("[오류] 올바른 숫자를 입력하세요")
    
    # 사용자가 올바르게 선택을 했는지 확인하기
    @staticmethod
    def confirm_action(message: str) -> bool:
        while True:
            response = input(f"{message} (y/n): ").strip().lower()
            if response in ['y', 'yes', '예']:
                return True
            elif response in ['n', 'no', '아니오']:
                return False
            print("[오류] 'y' 또는 'n'을 입력하세요")
    
    # 사용자의 입력이 유효한지 검증하기
    @staticmethod
    def validate_input(input_value: str, input_type: str) -> bool:
        if input_type == 'int':
            try:
                int(input_value)
                return True
            except ValueError:
                return False
        elif input_type == 'positive_int':
            try:
                return int(input_value) > 0
            except ValueError:
                return False
        return False
    
    # 엔터키가 들어올 때까지 대기
    @staticmethod
    def wait_for_enter():
        input("\n계속하려면 Enter를 누르세요...")
