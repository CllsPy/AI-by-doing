import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title('Monte Carlo Approximation For Pi')
def pi_estimator(radius=1, num_iter=int(1e4)):

    X = np.random.uniform(-radius, +radius, num_iter)
    Y = np.random.uniform(-radius, +radius, num_iter)

    R2 = X**2 + Y**2
    inside = R2 < radius ** 2
    outside = ~inside

    samples = (2*radius) * (2*radius) * inside

    I_hat = np.mean(samples)
    pi_hat = I_hat/radius ** 2
    pi_hat_se = np.std(samples)/np.sqrt(num_iter)

 
    fig, ax = plt.subplots()
    ax.scatter(X[inside], Y[inside], c='b', alpha=0.5)
    ax.scatter(X[outside], Y[outside], c='r', alpha=0.5)
    st.pyplot(fig)


pi_estimator()
