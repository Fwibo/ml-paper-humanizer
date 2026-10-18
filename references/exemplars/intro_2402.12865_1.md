<!-- section: intro; orientation: design; source: arXiv 2402.12865, published text, style reference only -->

Deep learning models consist of layers, which are parameterized by matrices that are trained using a method known as backpropagation. This process involves the creation of gradient matrices that are used to update the models' layers. Backpropagation has been playing a major role in interpreting deep learning models and multiple lines of study aggregate the gradients to provide explainability [cite].

Recent interpretability works have introduced methods to project the weights and intermediate activations of Transformer-based LMs [cite] into the vocabulary space. The seminal ``Logit Lens'' method [cite] has paved the way to explaining LMs' behavior

during inference [cite], including directly interpreting individual neurons [cite]. Our work is the first, as far as we can ascertain, to project LM \emph{gradients} to the vocabulary space. Furthermore, modern LMs contain thousands of neurons in each layer, while certain features are likely distributed across multiple neurons [cite]. These issues are handled in our examination of the gradient matrices by performing a decomposition of provably low-rank matrices.
