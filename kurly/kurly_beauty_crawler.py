"""
Kurly Beauty Category Product Crawler
컬리 뷰티 카테고리 상품 정보 수집 스크립트
"""

import requests
import json
from typing import Dict, List, Optional


class KurlyBeautyCrawler:
    """컬리 뷰티 카테고리 상품 크롤러"""
    
    BASE_URL = "https://api.kurly.com/collection/v2/home/sites/beauty/product-categories"
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def fetch_products(
        self, 
        category_id: int = 167001, 
        sort_type: int = 4, 
        page: int = 1, 
        per_page: int = 100
    ) -> Optional[Dict]:
        """
        상품 목록 조회
        
        Args:
            category_id: 카테고리 ID (기본값: 167001)
            sort_type: 정렬 타입 (기본값: 4)
            page: 페이지 번호 (기본값: 1)
            per_page: 페이지당 상품 수 (기본값: 100)
            
        Returns:
            API 응답 데이터 (딕셔너리) 또는 None
        """
        url = f"{self.BASE_URL}/{category_id}/products"
        params = {
            'sort_type': sort_type,
            'page': page,
            'per_page': per_page,
            'filters': ''
        }
        
        try:
            response = self.session.get(url, params=params, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"요청 실패: {e}")
            return None
    
    def parse_products(self, api_response: Dict) -> List[Dict]:
        """
        API 응답에서 상품 정보 추출
        
        Args:
            api_response: API 응답 데이터
            
        Returns:
            상품 정보 리스트
        """
        if not api_response or api_response.get('code') != '0000':
            print("유효하지 않은 응답")
            return []
        
        products = api_response.get('data', [])
        parsed_products = []
        
        for product in products:
            parsed = {
                'product_no': product.get('no'),
                'name': product.get('name'),
                'description': product.get('short_description'),
                'sales_price': product.get('sales_price'),
                'discounted_price': product.get('discounted_price'),
                'discount_rate': product.get('discount_rate'),
                'image_url': product.get('list_image_url'),
                'review_count': product.get('review_count'),
                'is_sold_out': product.get('is_sold_out'),
                'delivery_types': [d.get('type') for d in product.get('delivery_type_infos', [])]
            }
            parsed_products.append(parsed)
        
        return parsed_products
    
    def get_pagination_info(self, api_response: Dict) -> Dict:
        """
        페이지네이션 정보 추출
        
        Args:
            api_response: API 응답 데이터
            
        Returns:
            페이지네이션 정보 딕셔너리
        """
        meta = api_response.get('meta', {})
        pagination = meta.get('pagination', {})
        
        return {
            'total_items': pagination.get('total', 0),
            'current_page': pagination.get('current_page', 1),
            'total_pages': pagination.get('total_pages', 1),
            'items_per_page': pagination.get('per_page', 100)
        }


def main():
    """메인 실행 함수"""
    crawler = KurlyBeautyCrawler()
    
    # 첫 페이지 데이터 가져오기
    print("컬리 뷰티 상품 정보 수집 중...")
    response = crawler.fetch_products(page=1, per_page=100)
    
    if response:
        # 상품 정보 파싱
        products = crawler.parse_products(response)
        print(f"\n수집된 상품 수: {len(products)}개")
        
        # 페이지네이션 정보
        pagination = crawler.get_pagination_info(response)
        print(f"전체 상품 수: {pagination['total_items']}개")
        print(f"전체 페이지: {pagination['total_pages']}페이지")
        
        # 샘플 출력 (첫 3개 상품)
        print("\n=== 샘플 상품 정보 ===")
        for i, product in enumerate(products[:3], 1):
            print(f"\n{i}. {product['name']}")
            print(f"   가격: {product['sales_price']:,}원 → {product['discounted_price']:,}원 ({product['discount_rate']}% 할인)")
            print(f"   리뷰: {product['review_count']}개")
            print(f"   품절: {'예' if product['is_sold_out'] else '아니오'}")
        
        # JSON 저장
        output_file = '/home/claude/kurly_beauty_products.json'
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(products, f, ensure_ascii=False, indent=2)
        print(f"\n전체 데이터 저장 완료: {output_file}")
    else:
        print("데이터 수집 실패")


if __name__ == "__main__":
    main()
