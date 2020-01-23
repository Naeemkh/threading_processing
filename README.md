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

Concurrency is defined as the ability to conduct several computations at the same time or the ability to run different parts of code out of order in an overlapping period instead of executing in sequential order. In practice, concurrency is managing the available shared resources (CPU and Memory) among different programs [2]. In many cases, concurrency is confused with parallelism. Parallelism is utilizing different CPU cores and using mostly the same code on different data. Parallelism is the ability to split the tasks into subtasks that can be processed at the same time.

Concurrency can be implemented in different levels. Reference [3] defiened concurrency in three levels:
- Low-Level Concurrency: This level of concurrency makes explicit use of atomic operations. Atomic op- erations are program operations that run completely independently of any other processes. This level of concurrency is for library writers.
- Mid-Level Concurrency: This is concurrency that does not use any explicit atomic operations but uses explicit locks. Most programming languages support this kind of concurrency.
- High-level Concurrency: In this level of concurrency there is no explicit atomic operations and no explicit lock.

In this study, I am interested in implementing concurrency in developing applications; as a result, low-level concurrency is beyond the scope of this project. Implementing mid-level concurrency is practical in many applications; however, it is very error-prone. Problems that are hard to track down and occurring without any discernible pattern can happen in this level of concurrency. High-level concurrency reduces the possibility of these errors; it is easy to implement; however, it provides limited choices in implementation and level of user control [3].

Regardless of the level of concurrency, a concurrent program or system should be correct. The application should start from the initial state and correctly stop at the final state. In other words, it should provide the same correct answer as a sequential program.

To better understand concurrency in practice, we need to be familiar with processes and threads. A program under execution is called a process and is created by the operating system. Each process has its own dedicated memory and is not allowed to have access to other processes’ memory. Independent lightweight processes within a process are called threads. A thread, which is also known as a basic unit of CPU utilization, executes its own piece of code independently from other threads [2].

Multithreading (or threading for simplicity) is the ability of the central processing unit (CPU) to provide multiple threads of execution. This operation should be implemented in a way to make sure that the result of the multithreaded program is the same as the case when it is run sequentially. It is recommended that the nonconcurrent program be written first, if possible. If it is correct, then look for possible locations that can be run concurrently without loss of performance and correctness [3].

Sharing data is the most critical challenge in concurrent programming. The programmer, or concurrency modules, should make sure that the shared data is accessible and modifiable only through one thread at a time. Different approaches to sharing resources are the main difference between threading and multiprocessing. Execution through threading allows multiple threads exist and execute independently but share their process resources within the context of a process. Each process is isolated from other processes on the same machine. Different threads within one process have access to shared memory. However, communication between processes is implemented mostly by Inter-Process Communications (IPC). Fig. 1 shows an example of processes with single and multi-thread. In each process, threads share data and code; however, each thread has its dedicated stack, counter, and register (for more details about threads components see [2])


<figure class="image">
  <img src="images/app_flowchart.png" alt="Schematic representation of two processes." style="width: 500px;">
  <figcaption>Fig 1. Schematic representation of two processes. a) A process with a single thread. b) A process with three threads. The components of each thread are represented. In each process, threads share data and code.</figcaption>
</figure>


![Alt text](images/app_flowchart.png?raw=true "Title")

### References
1) F. Chollet et al., "Keras," https://keras.io, 2015
2) A. S. Tanenbaum and M. Van Steen, Distributed systems: principles and paradigms. Prentice-Hall, 2007. 
3) M. Summerfield, Python in practice: create better programs using concurrency, libraries, and patterns. Addison-Wesley, 2013.