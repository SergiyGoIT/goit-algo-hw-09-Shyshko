# Список доступних номіналів монет
COINS = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount):
    """
    Жадібний алгоритм для видачі решти.
    Вибирає найбільші номінали монет, щоб сформувати суму.
    Повертає словник із номіналами та їх кількістю.
    """
    result = {}
    remaining = amount
    
    # Проходимо по всіх номіналах від найбільшого до найменшого
    for coin in COINS:
        # Скільки монет даного номіналу можна взяти
        count = remaining // coin
        if count > 0:
            result[coin] = count
        # Зменшуємо залишкову суму
        remaining -= count * coin
    
    return result

def find_min_coins(amount):
    """
    Алгоритм динамічного програмування для видачі решти.
    Знаходить мінімальну кількість монет для формування суми.
    Повертає словник із номіналами та їх кількістю.
    """
    # Масив для збереження мінімальної кількості монет для кожної суми
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    # Масив для збереження останньої використаної монети
    last_coin = [0] * (amount + 1)
    
    # Заповнюємо dp для всіх сум від 1 до amount
    for i in range(1, amount + 1):
        for coin in COINS:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                last_coin[i] = coin
    
    # Відновлюємо монети, які формують суму
    result = {}
    remaining = amount
    while remaining > 0:
        coin = last_coin[remaining]
        result[coin] = result.get(coin, 0) + 1
        remaining -= coin
    
    return result

# Тестування функцій
if __name__ == "__main__":
    test_amount = 113
    print(f"Жадібний алгоритм для суми {test_amount}: {find_coins_greedy(test_amount)}")
    print(f"Динамічне програмування для суми {test_amount}: {find_min_coins(test_amount)}")
