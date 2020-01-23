## An Overview of Concurrency
## Case Study:  Live Data Streaming

## Written by: Naeem Khoshnevis

### Introduction 
Application of machine learning, specifically deep learning algorithms in scientific research and solving business problems, has gained substantial interest during the recent years. Sensors for data acquisition are cheaper and more accurate than before. Small research groups or businesses have the possibility of storing a large amount of data, and high-performance computing resources are more accessible than before. As a result, intensive data-driven studies have become a significant part of many research fields and businesses. These studies require handling significantly large datasets, and also, they demand intensive computation. Such studies with different steps in input data, preprocessing, analysis, prediction model training, post-processing, output data, as well as updating models, are good candidates for implementing and studying the concept of concurrency.
A typical data-driven system or practical prediction model can have three main parts: 

- The system requires some data; as a result, there should be one source of incoming data
- It requires to process the incoming data and produce some results or decisions
- The system requires to implement or present the results.

A brief review of the published codes and papers indicates that concurrency is mostly ignored in these studies. One reason is the fact that it is considered an advanced programming feature. As a result, researchers are primarily dependent on the features which are provided with deep learning packages (e.g., see Keras as a high-level neural network API, written in Python and capable of running on top of TensorFlow, CNTK, or Theano [1])

Because modern computers are equipped with multiple CPU cores, as a result, harnessing available computational resources can improve the performance of the data-driven systems and speed up the intensive computational processes. In this study, I present a practical overview of concurrency. First, I present an overview of concurrency in general, then I continue with more technical details on the implementation of concurrency in Python. I develop a live data streaming system with different computational features, and I apply concurrency at different levels. I use the Python programming language as a study platform and different processing packages.
The study shows that concurrency significantly improves the performance of the system, and in many cases, keeps the system responsive for incoming data. It should be considered as one of the crucial steps of developing any data-driven system and product to harness the computational resources in the system effectively.

### Concurrency




<!-- ![Alt text](images/app_flowchart.png?raw=true "Title") -->

### References
1) F. Chollet et al., "Keras," https://keras.io, 2015