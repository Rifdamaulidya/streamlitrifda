import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title('Binomial Distribution')

def binomial_distribution(n,p,k):
    q = 1-p
    koef = np.math.comb(n,k)
    return koef*(p**k)*(q**(n-k))

def main():
    n = st.number_input('Enter the number of trial (n)', min_value=1,step=1)
    p = st.slider('Enter the probability of success (p)', min_value=0.0, max_value=1.0, step=0.01)
    k = st.number_input('Enter the number of success (x)', min_value=0, max_value=n, step=1)

    x = np.arange(0,n+1)
    y = [binomial_distribution(n,p,i) for i in x]

    fig, ax = plt.subplots()
    ax.bar(x,y)
    ax.set_xlabel('Number of Success (x)')
    ax.set_ylabel('Probability')
    ax.set_title('Binomial Distribution')
    st.pyplot(fig)

    st.write('Binomial Distribution Table')
    table = {'Number of Success (x)':x, 'Probability':y}
    st.table(table)

if __name__=='__main__':
    main()