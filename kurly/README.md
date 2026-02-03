# Kurly Beauty Crawler

컬리 뷰티 카테고리 상품 정보 크롤러

## 파일 설명

### 1. `kurly_beauty_crawler.py`
- **설명**: 정리된 Python 스크립트
- **특징**:
  - 클래스 기반 구조
  - 타입 힌트 적용
  - 에러 핸들링 포함
  - 재사용 가능한 코드

### 2. `kurly_beauty_crawler_clean.ipynb`
- **설명**: 정리된 Jupyter Notebook
- **특징**:
  - 마크다운으로 섹션 구분
  - 단계별 실행 가능
  - 데이터 분석 포함
  - 시각화 가능

## 사용 방법

### Python 스크립트 실행
```bash
python kurly_beauty_crawler.py
```

### Jupyter Notebook 실행
```bash
jupyter notebook kurly_beauty_crawler_clean.ipynb
```

## 주요 기능

### 1. 데이터 수집
- 카테고리별 상품 정보 조회
- 페이지네이션 지원
- 정렬 옵션 설정

### 2. 데이터 파싱
- 상품 기본 정보 추출
- 가격 정보 (정가, 할인가, 할인율)
- 리뷰 정보
- 배송 정보

### 3. 데이터 저장
- JSON 형식 저장
- CSV 형식 저장
- Pandas DataFrame 지원

## API 정보

### 엔드포인트
```
https://api.kurly.com/collection/v2/home/sites/beauty/product-categories/{category_id}/products
```

### 파라미터
- `sort_type`: 정렬 방식 (기본값: 4)
- `page`: 페이지 번호 (기본값: 1)
- `per_page`: 페이지당 상품 수 (기본값: 100)
- `filters`: 필터 옵션

### 카테고리 ID
- 뷰티 카테고리: 167001

## 수집 데이터 필드

| 필드명 | 설명 | 타입 |
|--------|------|------|
| product_no | 상품 번호 | int |
| name | 상품명 | str |
| description | 상품 설명 | str |
| sales_price | 정가 | int |
| discounted_price | 할인가 | int |
| discount_rate | 할인율 (%) | int |
| image_url | 이미지 URL | str |
| review_count | 리뷰 수 | str/int |
| is_sold_out | 품절 여부 | bool |
| delivery_types | 배송 방식 | list |

## 개선 사항

### 원본 노트북 → 정리된 버전

1. **구조화**
   - 라이브러리 임포트 통합
   - 섹션별 마크다운 추가
   - 코드 블록 분리

2. **가독성**
   - 변수명 한글화
   - 주석 추가
   - 출력 형식 개선

3. **기능 추가**
   - DataFrame 변환
   - 통계 분석
   - 데이터 저장

4. **클래스화 (Python 스크립트)**
   - OOP 구조 적용
   - 메서드 분리
   - 재사용성 향상

## 주의사항

1. **API 제한**
   - Rate limiting 적용 가능
   - 적절한 딜레이 권장

2. **네트워크 제한**
   - 일부 환경에서 접근 제한 가능
   - 프록시 설정 필요할 수 있음

3. **데이터 변경**
   - API 응답 구조는 변경될 수 있음
   - 정기적인 검증 필요

## 라이선스

이 코드는 교육 및 학습 목적으로 작성되었습니다.

## 문의

문제가 발생하면 이슈를 등록해 주세요.
