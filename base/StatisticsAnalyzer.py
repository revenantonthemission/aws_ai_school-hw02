# 통계 분석기 클래스

from typing import List, Dict
from RoundResult import RoundResult

# 시뮬레이션 통계 분석
class StatisticsAnalyzer:
    
    def __init__(self):
        self.total_spent = 0
        self.total_won = 0
        self.winning_frequency: Dict[int, int] = {}  # {등급: 횟수}
        self.round_results: List[RoundResult] = []
    
    # 라운드 결과 기록
    def record_round(self, round_result: RoundResult):
        self.round_results.append(round_result)
        self.total_spent += round_result.total_spent
        self.total_won += round_result.total_won
        
        # 등급별 당첨 빈도 업데이트
        for rank, count in round_result.get_winning_count_by_rank().items():
            self.winning_frequency[rank] = self.winning_frequency.get(rank, 0) + count
        
    # 당첨 통계 반환
    def get_winning_statistics(self) -> Dict:
        total_tickets = sum(r.tickets_purchased for r in self.round_results)
        total_winning_tickets = sum(len(r.winning_tickets) for r in self.round_results)
        
        return {
            'total_rounds': len(self.round_results),
            'total_tickets': total_tickets,
            'total_winning_tickets': total_winning_tickets,
            'winning_rate': (total_winning_tickets / total_tickets * 100) if total_tickets > 0 else 0,
            'winning_by_rank': self.winning_frequency,
            'total_spent': self.total_spent,
            'total_won': self.total_won,
            'net_profit': self.total_won - self.total_spent
        }
    
    # 등급별 상세 분석
    def get_frequency_analysis(self) -> Dict[int, Dict]:
        analysis = {} 
        for rank, count in self.winning_frequency.items():
            total_rounds = len(self.round_results)
            analysis[rank] = {
                'count': count,
                'frequency': (count / total_rounds) if total_rounds > 0 else 0,
                'percentage': (count / total_rounds * 100) if total_rounds > 0 else 0
            }
        return analysis
    
    # 요약 레포트 생성
    def generate_summary_report(self) -> str:
        stats = self.get_winning_statistics()
        freq_analysis = self.get_frequency_analysis()
        
        report = f"""
{'='*60}
시뮬레이션 결과 요약
{'='*60}

기본 통계:
  - 총 라운드: {stats['total_rounds']:,}회
  - 구매 티켓: {stats['total_tickets']:,}장
  - 당첨 티켓: {stats['total_winning_tickets']:,}장
  - 당첨 확률: {stats['winning_rate']:.2f}%

수익 분석:
  - 총 투자액: {stats['total_spent']:,}원
  - 총 당첨금: {stats['total_won']:,}원
  - 순손익: {stats['net_profit']:+,}원

등급별 당첨 현황:
"""
        
        for rank in sorted(freq_analysis.keys()):
            info = freq_analysis[rank]
            report += f"  - {rank}등: {info['count']:,}회 ({info['percentage']:.2f}%)\n"
        
        report += f"\n{'='*60}\n"
        
        return report
    
    def reset(self):
        """통계 초기화"""
        self.total_spent = 0
        self.total_won = 0
        self.winning_frequency = {}
        self.round_results = []
