import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

st.title('Poisson Distribution')

def poisson_distribution(k, lambd):
    return poisson.pmf(k, lambd)

def main():
    k = st.number_input('Enter the number of event (k)', min_value=0, step=1)
    lambd = st.number_input('Enter the lamda value', min_value=0.01, step=0.01)

    x = np.arange(0, k+1)
    y = [poisson_distribution(i, lambd) for i in x]

    fig, ax = plt.subplots()
    ax.bar(x,y)
    ax.set_xlabel('Event (k)')
    ax.set_ylabel('Probability')
    ax.set_title('Poisson Distribution')
    st.pyplot(fig)

    st.write('Poisson Distribution Table')
    table = {'Event (k)':x, 'Probability':y}
    st.table(table)

if __name__ == '__main__':
    main()