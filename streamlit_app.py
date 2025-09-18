import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def main():
    st.title("y = nx 그래프 그리기")
    st.write("숫자 n을 입력하면 y = nx 형태의 그래프가 그려집니다.")

    n = st.number_input("n 값을 입력하세요", value=1, step=1)

    x = np.linspace(-10, 10, 200)
    y = n * x

    fig, ax = plt.subplots()
    ax.plot(x, y, label=f"y = {n}x")
    ax.axhline(0, color='gray', linewidth=0.5)
    ax.axvline(0, color='gray', linewidth=0.5)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    st.pyplot(fig)

if __name__ == "__main__":
    main()
st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
