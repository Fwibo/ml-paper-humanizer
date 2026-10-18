<!-- section: results; orientation: design; source: arXiv 2412.00088, published text, style reference only -->

where \(\mathcal{L}\) and \(\mathcal{B}\) are known operators, $f(\vb{x})$ and $g(\vb{x})$ are known functions for the residual and boundary/initial conditions, and \(u: \mathbb{R}^{d}\to \mathbb{R}\) is a scalar-valued function, which is the unknown solution to the PDE. The approximated solution \(u_{\theta }(\vb{x})\) $\approx$ \(u(\vb{x})\) is obtained by minimizing the mean squared error (MSE) of the PDE residual $R(\vb{x};\theta)=\mathcal{L} u_{\theta }(\vb{x}) - f(\vb{x})$:

where the residual points \(\{\vb{x}^{(i)}\}_{i=1}^{N_{r}}\) are sampled from the domain \(\Omega\). We use the technique from [cite] that reparameterizes $u_{\theta }$ such that the boundary/initial condition \(\mathcal{B} u(\vb{x}) = g(\vb{x})\) are satisfied exactly for all \(\vb{x}\in \partial\Omega \), so boundary loss is not needed.

PINN training can be amortized by replacing the differential part of the operator $\mathcal{L}$ with a stochastic estimator like SDGD and STDE. For example, for the Allen-Cahn equation, $\mathcal{L}u= \laplacian u+u-u^{3}$, the differential part of $\mathcal{L}$ is the Laplacian $\laplacian$. With amortization, we minimize the following loss
