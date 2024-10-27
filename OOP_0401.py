# 1) Item 클래스 구현
class Item:
    def __init__(self, name, vendor, category, price, cost, weight):
        self.name = name
        self.vendor = vendor
        self.category = category
        self.price = price
        self.cost = cost
        self.weight = weight

    def increase_cost(self, increase_percentage):
        self.cost *= (1 + increase_percentage/100)

    def profit(self):
        return self.price - self.cost


# 2) 제품 객체 생성, Item 리스트에 저장
items = [
    Item("포테이토칩", "농심", "과자류", 1800, 1300, 300),
    Item("액츠파워젤", "피죤", "세탁세제류", 20770, 13500, 4.2),
    Item("대천김 도시락김 5g(54봉)", "케이앤비컴퍼니", "식품류", 18300, 10000, 300)
]

# items 리스트에 저장된 제품들의 정보 출력
for item in items:
    print("Name:", item.name)
    print("Vendor:", item.vendor)
    print("Category:", item.category)
    print("Price:", item.price)
    print("Cost:", item.cost)
    print("Weight:", item.weight)
    print()  # 공백 라인 추가


# 3) 대천김의 생산단가가 15% 인상되었을때 이를 반영하는 명령문
for item in items:
    if item.name == "대천김 도시락김 5g(54봉)":
        # 생산단가 15% 인상
        item.increase_cost(15)
        break

# 인상된 생산단가 출력
print("대천김의 인상된 생산단가:", items[2].cost)



# 4) 고객이 1개씩 구매했다고 가정
total_profit = 0
for item in items:
    total_profit += item.profit()

# 총 판매이익금 출력
print("총 판매이익금:", total_profit)
