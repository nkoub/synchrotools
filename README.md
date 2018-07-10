==synchrotools==

**synchrotools** is a python package providing a collection of indices that characterize 
 + synchronization 
 + chimera states
 + metastable states

Data are handled with numpy ndarrays and dictionaries


+ Kuramoto order Parameter
 - Global order parameter: 
\begin{equation}
\rho = \frac{1}{N}\sum_{j=1}^N e^{\mathbf{i}\theta_j(t)} 
\end{equation}

 - Local order parameter: 
\begin{equation} \rho_i = \frac{1}{2\delta}\sum_{j=i-\delta}^{i+\delta} e^{\mathbf{i}\theta_j(t)} \end{equation}

+ Mean correlation

+ Mean phase velocity
\begin{equation}
\Omega_i = \frac{2 \pi K_i}{\Delta T}\,,
\end{equation}
where \(K_i\) is the number of periods of the $i$-th oscillator during a time interval \(\Delta T\).  

+ Metastabilite index \(\lambda\):

\begin{equation} \lambda = {\langle \sigma_{\textbf{met}} \rangle}_{C_m}\end{equation}
where
\begin{equation} \sigma_{\textbf{met}}(m)=\frac{1}{T-1}\sum_{t=1}^T(\rho_m(t)-{\langle \rho_m \rangle}_T)^2\end{equation}

+ Chimera-like index \( \chi \)
\begin{equation} \chi={\langle \sigma_{\textbf{chi}} \rangle}_T, \end{equation}
where
\begin{equation} \sigma_{\textbf{chi}}(t)=\frac{1}{M-1}\sum_{m=1}^M(\rho_m(t)-{\langle \rho(t) \rangle}_M)^2 \end{equation}

+ Local curvature
 - Local curvature:
\begin{equation} \hat{D}\theta_i(t) := \sum_{j=i-\delta}^{j=i+\delta} \!\left[\theta_j(t) - \theta_i(t)\right]\, \end{equation}
 
 - Spatial coherence:

The norm of the operator \(\hat{D}\) in the coherent clusters is zero (or sufficiently small) \( \|\hat{D}\{\theta_{i_\text{coh}}(t)\}\|\approx 0 \), while in the incoherent clusters \( \|\hat{D}\{\theta_{i_\text{incoh}}(t)\}\| \) is finite and has pronounced fluctuations. The maximum value \( D_m \) of \( \|\hat{D}\theta_i(t)\| \) corresponds to the local curvature of nodes whose neighbors. 
