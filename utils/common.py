import streamlit as st


def calculate(ves, doza, gl):
    num = doza * ves
    # мл = мг / 1000.
    dicti = {5: 50, 10: 100, 20: 200}
    ml = (num / dicti[gl]) * 60
    st.success(f"Скорость введения в мг: {round(num, 2)} мг/мин")
    st.success(f"Скорость введения {gl} процентной глюкозы: {ml} мл/час")


def change_page(page):
    st.session_state["other"] = 0
    st.session_state['page'] = page


def change_other(what):
    st.session_state["other"] = what