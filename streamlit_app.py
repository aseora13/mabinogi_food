import matplotlib.pyplot as plt
import streamlit as st

def main() -> None:
    attack = st.number_input(label='기본 공격력',min_value=1000, max_value=20000)
    members = st.select_slider(label='파티원 수', options=range(2, 9))
    runes = st.columns([1, 1])
    with runes[0]:
        weapons = {
            '기타':0,
            '천 자루 검': .24,
            '무수한 담금질': .08,
            '격노+': .36
        }
        
        selected_weapon = st.selectbox('사용 중인 무기 룬', weapons.keys())
        result1 = weapons[selected_weapon]
    with runes[1]:
        armor = {
            '깨달음': .1,
            '안정+': .11,
            '마나 격류': .14,
            '비열한 일격': .24,
            '바위 거인': .24
        }
        
        selected_armor = st.multiselect('사용 중인 방어 룬', armor.keys())
        result2 = 0
        for i in selected_armor:
            result2 += armor[i]
    st.text('총 공격력 증가량(룬): {:.1f}%'.format((result1 + result2)*100))
    st.text('고등어 연어 스테이크 섭취 시 공격력: {:.1f}'.format(attack*(1 + result1 + result2 + members*0.01)))
    st.text('농어 매운탕 섭취 시 공격력: {:.1f}'.format((attack+120*members)*(1 + result1 + result2)))

if __name__ == "__main__":
    main()
