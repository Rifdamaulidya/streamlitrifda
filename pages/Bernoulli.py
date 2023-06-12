import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title('Bernoulli Distribution')

def bernoulli_distribution(p, k):
    q = 1-p
    prob = [p if i==1 else q for i in k]
    return prob

def main():
    p = st.slider('Enter the probability of success (p)', value=0.5, min_value=0.0, max_value=1.0, step=0.01)
    k = np.array([0,1])

    prob = bernoulli_distribution(p,k)

    fig, ax = plt.subplots()
    ax.bar(k, prob)
    ax.set_xticks(k)
    ax.set_xticklabels(['Failure(0)', 'Success(1)'])
    ax.set_xlabel('Possible Outcomes')
    ax.set_ylabel('Probability')
    ax.set_title('Bernoulli Distribution')
    st.pyplot(fig)

    st.write('Bernoulli Distribution Table')
    table = {'Possible Outcomes':k, 'Probability':prob}
    st.table(table)

if __name__ == '__main__':
    main()