
buy_price = float(input("購入価格を入力してください: "))
sell_price = float(input("売却価格を入力してください: "))
quantity = int(input("株数を入力してください: "))

profit = (sell_price - buy_price) * quantity

if profit > 0:
    tax = profit * 0.20315
else:
    tax = 0

after_tax = profit - tax

print("税引き前利益:", round(profit, 2), "円")
print("税金（概算）:", round(tax, 2), "円")
print("税引き後利益:", round(after_tax, 2), "円")
