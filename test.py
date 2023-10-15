from python_billiard_bot import *
import pytest

#проверяем, что уже зарегистрированного пользователя бот перекинет в меню
def test_start():
    res = start(user_id=315398445, vk=vk)
    assert res == CONTEXT_MENU 

#проверяем, что ФИО нового пользователя заносится в таблицу
def test_add_new_user():
    add_new_user(user_id=243443254, text='ФИО: Jeff Beck')
    res = df['name'].loc[len(df.index)-1]
    assert res == 'Jeff Beck'

#проверяем, что вопрос генирируется
def test_question_generator():
    res = generate_question(vk, 243443254)
    assert res

#проверяем, что в случае правильного ответа кол-во удачных попыток увеличивается на единицу
def test_right_answer():
    old_val = df['right_tries'].loc[df['id'] == 315398445]
    answer_is_right(vk, 315398445) 
    new_val = df['right_tries'].loc[df['id'] == 315398445]
    assert new_val[0] == old_val[0] + 1

#проверяем, что после окончания тестирования индекс выставляется в ноль
def test_end_of_test():
    is_last_question(vk, 243443254)
    assert indx == 0

#проверяем, что статистика отправляется 
def test_statistics():
    res = send_stats(vk, 243443254)
    assert res

#проверяем, что пользователь переходит в режим редактрования
def test_change_info():
    res = change_info(243443254, vk)
    assert res == CONTEXT_CHANGE_INFO

#проверяем, что при нажатии кнопки "Другое" пользователю возвращается заглушка
def test_other():
    res = other(243443254, vk)
    assert res == CONTEXT_OTHER