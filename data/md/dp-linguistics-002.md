# Parallel Needleman-Wunsch on CUDA to measure word similarity based on phonetic transcriptions

## Abstract

We present a method to calculate the similarity between words based on their phonetic transcription (their pronunciation) using the Needleman–Wunsch algorithm. We implement this algorithm in Rust and parallelize it on both CPU and GPU to handle large datasets efficiently. The GPU implementation leverages CUDA and the cudarc Rust library to achieve significant performance improvements. We validate our approach by constructing a fully-connected graph where nodes represent words and edges have weights according to the similarity between the words. This graph is then analyzed using clustering algorithms to identify groups of phonetically similar words. Our results demonstrate the feasibility and effectiveness of the proposed method in analyzing the phonetic structure of languages. It might be easily expanded to other languages.
