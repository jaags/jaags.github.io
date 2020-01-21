---
title: Interview Questions
layout: single
read_time: true
comments: true
share: true
related: true
sidebar:
  nav: MachineLearning
tag:
- NLP
- data science
- similarities measure
date: '2018-08-09'
permalink: "/interview_questions/"
header:
  #teaser: images/IMG-20190710-WA0000.jpg
mathjax: true
toc: true
toc_icon: cog
---

1. ### Differentiate between AI, ML and DP?
2. ### Is Deep learning better than ML?
3. ### Whatt is Perceptron? How does it work?
4. ### What is the role of weights and bias?
5. ### What are activation functions?
6. ### What is the significance of a Cost/Loss function?
7. ### What is gradient descent?
8. ### What are the beenifits of mini-batch gradient descent?
9. ### What are the steps for using a gradient descent algorithm?
10. ### Pseudocode a gradient descent in python?

		params = [wieghts_hidden, weights_output,bias_hidden, bias_output]
		def sgd(cost, params, lr=0.05)
		grads = T.grad(cost=cost, wrt=params)
		for p, g in zip(params, grads)
				updates.append([p, p-g*lr])
		return update
		update = sgd(cost, params) 

11. ### What are the different parts of a multi-layer perceptron?

12. ### What is data normalization and why do we need it?

13. ### Which is better, deep networks or shallow ones? Why?

14. ### Why is wieght initialization import in neural networks?

15. ### Difference between a feed-forward and back propogation neural network?

16. ### What are Hyperparameters? Name a few used in any neural network?

17. ### Explain the different hypparameters related to netowk and training?
  
    * ## Network Hypermaters 
      1. No. of hidden layers
      2. Weight initialization
      3. Actication function
    * ## Training Hyperparameters  
      4. Batch size 
      5. No. of Epoch
      6. Momentum
      7. Learning Rate

18. ### What is a dropout?

    * It's a reqularization technique to avoid overfitting thus increasing the generalizing power.
    * Dropout value 20% - 50% of neurons is a good start
    * A probability too low has minimal effect and too high results in under-learning by the network.

19. ### In training a neural network, the loss does not decrease in the few starting epochs?

    * The learning rate is low
    * Regularization parameter is high
    * Stuck at local-minima


20. ### Name a few deep learning frameworks?

    * Tensorflow
    * Keras
    * PyTorch
    * Chainer
    * Caffe
    * Microsoft CNTK
    * IBM Congition 
    * AmexNet


21. ### What are Tensors?

    * They are multi-dimensional arrays to represent data having higher dimensions, where dimensions refer to different features present in the data set.

22. ### List a few advantages of TensorFlow?

    * Trainable on CPU or GPU
    * Auto differentiation capabilities
    * Advanced support for threads, asynchronous computation
    * Customizable and open source
    * Platform flexibility

23. ### What is computational graph?

    * Series of tensorflow operations arranged as nodes in the graph. Each node takes zero or more tensors as input and produces a tensor as output.

  
24. ### What is a CNN?

    * Convolutional neural network (CNN or ConvNet) is a class of deep neural netorks, most commonly applied to analyzing visual imagery.

    * Unlike neural networks, where the input is a vector, here the input is a multi-channeled image. CNNs use a variation of multilayer perceptrons designed to require minimal pre-processing.


25. ### Explain the different layers of CNN?

    * Input layer
    * Conv + RELU layer
    * Pooling 
    * Conv + RELU layer
    * Pooling layer
    * Flatten 
    * Fully Connected 
    * Softmax

26. ### what are RNN?

    * They are type of neural network designed to recognize patterns in sequence of data, such as text, genomes, handwriting, the spoken words, numerical times series data.
    * RNN use backpropogration algorithm for training because of their internal memory, RNN's are capable of remember important things about the input they received, that enables to be very precise what's coming next.


27. ### What are some issues faced while training a RNN?

    * There are some issues with Back-propagation through time (BTT)
      * Vanishing Gradient
      * Exploading Gradient

28. ### What is Vanishing Gradient decent? How is this harmful?

29. ### What is Exploding Gradient decent?

30. ### Explain the importance of LSTM?

31. ### What are capsules in Capsule Neural Network?

32. ### Explain Autoencoders and it's uses?

33. ### In terms of Dimensionality reduction, How does Autoencoders differ from PCAs?

34. ### Give some real-life examples where autoencoders can be applied?

35. ### What are different layers of Autoencoders?
    
    * Encoder - compresses the input into a latent space representation.

    * Code - represents the compressed part of network, which later fed to decoder.

    * Decoder - As name suggest, this layer decodes the encoded image back to orginal dimension. 
    
36. ### What is a bottlenect in autoencoders and why is it used?


37. ### Is there any variations of Autoencoders?

    * Convolution
    * Sparse
    * Deep
    * Contractive

38. ### What are Deep Autoencoders?

39. ### What is a Restricted Boltzmann Machine?

40. ### How does RBM differ from Autoencoders?

41. ### What are some limitations of deep learning?


42. ### 