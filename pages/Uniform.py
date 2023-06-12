import streamlit as st
import numpy as np

st.title('Uniform Distribution: Discrete')

def uniform_discrete_distribution(a, b):
    x = np.arange(a, b+1)
    y = np.full_like(x, 1/(b-a+1))
    return x,y

def main():
    a = st.number_input('Enter the lower value (a)', step=1)
    b = st.number_input('Enter the upper value (b)', step=1)

    x,y = uniform_discrete_distribution(a, b)

    st.write('Uniform Distribution Table')
    table = {'Value(x)':x, 'Probability':y}
    st.table(table)

if __name__=='__main__':
    main()