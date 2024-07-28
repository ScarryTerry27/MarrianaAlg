import streamlit as st
from utils.common import change_page, change_other, calculate
from utils.router import gipo, giper

if "page" not in st.session_state:
    st.session_state["page"] = 1
    st.session_state["other"] = False


def show_sidebar():
    with st.sidebar:
        st.button("🚑 Главная страница", on_click=change_page, kwargs={"page": 1})
        st.button("🎈 Вторая страница", on_click=change_page, kwargs={"page": 2})
        st.button("🌡 Третья страница", on_click=change_page, kwargs={"page": 3})
        st.button("📟 Алгоритм", on_click=change_page, kwargs={"page": 4})


def page_1():
    st.title("Написать тут что то")
    with open("texts/page1.txt", encoding='utf-8', mode='r') as file:
        text = file.read()

    st.markdown(text, unsafe_allow_html=True)
    col1, col2 = st.columns([3, 1])

    with col2:
        st.caption("В.А.Таболин, 1986 г.", unsafe_allow_html=True)

    st.button("Далее 💊", on_click=change_page, kwargs={"page": 2})


def page_2():
    st.title("Тут какой то текст")
    with open("texts/page2.txt", encoding='utf-8', mode='r') as file:
        text = file.read()

    st.markdown(text)
    col1, col2 = st.columns([1, 29])

    with col2:
        st.caption('''De Rose D.U.et al.Neonatal
    hypoglycemia and neurodevelopmental outcomes: Yesterday, today, tomorrow // European
    Journal of Pediatrics.– 2024. – Т.183. – №.3. – С.1113-1119''', unsafe_allow_html=True)

    st.subheader("Какие возможны риски, связанные с дисгликемией…")
    col1, col2 = st.columns([7, 3])
    col1.button("Гипогликемия", on_click=change_other, kwargs={"what": 1})
    col2.button("Гиперликемия", on_click=change_other, kwargs={"what": 2})

    st.button("Далее 💊", on_click=change_page, kwargs={"page": 3})


def page_3():
    st.title("По результатам нашего клинического рандомизированного исследования сделаны выводы")
    with open("texts/page5.txt", encoding='utf-8', mode='r') as file:
        text = file.read()

    st.write(text)

    st.button("Далее 💊", on_click=change_page, kwargs={"page": 4})


def page_4():
    st.title("Разработанный алгоритм")

    dicti = {"Доношенные и поздние недоношенные свыше 34 нед. гестации: 2,3 мг/кг/мин": (1.15, 1.15),
             "Недоношенные менее 34 нед. гестации": (1.15, 2.3),
             "Все новорожденные, имеющие факторы риска гипогликемии (транзиторный гиперинсулинизм, диабетическая фетопатия, асфиксия при рождении, длительное парентеральное питание)": (2.3, 2.3)}
    number1 = st.radio(label="Выберите из списка(текст поменять)", options=dicti.keys(), index=0, key="R1")
    number2 = st.number_input("Введите вес, кг", min_value=0, max_value=10)
    number3 = st.number_input("Введите дозу", value=dicti[number1][0])
    gl = st.radio("Введите процент глюкозы", options=[5, 10, 20])
    if number3 > dicti[number1][1] or number3 < dicti[number1][0]:
        st.error(f"Значения должны быть в пределах от {dicti[number1][0]}, до {dicti[number1][1]}")
        if number3 > dicti[number1][1]:
            number3 = dicti[number1][1]
            st.info(f"Значения дозы приведено к максимальной: {dicti[number1][1]}")
        if number3 < dicti[number1][0]:
            number3 = dicti[number1][0]
            st.info(f"Значения дозы приведено к минимальной: {dicti[number1][0]}")
    st.button('🚀 Рассчитать', on_click=calculate, kwargs={"ves": number2, "doza": number3, "gl": gl})

    st.button("🔄 На главную", on_click=change_page, kwargs={"page": 1})


router = {1: page_1, 2: page_2, 3: page_3, 4: page_4}
show_sidebar()
if not st.session_state["other"]:
    router[st.session_state['page']]()
else:
    [gipo, giper][st.session_state["other"]-1]()
