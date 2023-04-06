import pandas as pd
import numpy as np


chat_id = 784066571 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return ((x  - np.log(x + 35)) / 10).mean() # Ваш ответ
