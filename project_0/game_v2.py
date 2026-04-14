"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    m = 101
    n = 1
    while True:
        count += 1
        predict_number = np.random.randint(n, m) # предполагаемое число
        
        if predict_number > number:
            m = predict_number
        elif predict_number < number:
            n = predict_number
            
        elif number == predict_number:
            break # выход из цикла, если угадали
    return(count)
    
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов 
    угадывает наш алгоритм

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_ls = [] # список дял сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспризводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls)) # находим среднее количество попыток
    
    print(f'Ваш алгоритм угадывает в среднем за {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)

        