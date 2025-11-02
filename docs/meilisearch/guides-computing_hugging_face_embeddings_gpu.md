# Computing Hugging Face embeddings with the GPU

**Source:** https://www.meilisearch.com/docs/guides/computing_hugging_face_embeddings_gpu.md
**Extrait le:** 2025-10-08
**Sujet:** Guides - GPU Configuration

---

# Computing Hugging Face embeddings with the GPU

> This guide for experienced users shows you how to compile a Meilisearch binary that generates Hugging Face embeddings with an Nvidia GPU.

This guide is aimed at experienced users working with a self-hosted Meilisearch instance. It shows you how to compile a Meilisearch binary that generates Hugging Face embeddings with an Nvidia GPU.

## Prerequisites

* A [CUDA-compatible Linux distribution](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#id12)
* An Nvidia GPU with CUDA support
* A modern Rust compiler

## Install CUDA

Follow Nvidia's [CUDA installation instructions](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html).

## Verify your CUDA install

After you have installed CUDA in your machine, run the following command in your command-line terminal:

```sh
nvcc --version | head -1
```

If CUDA is working correctly, you will see the following response:

```
nvcc: NVIDIA (R) Cuda compiler driver
```

## Compile Meilisearch

First, clone Meilisearch:

```sh
git clone https://github.com/meilisearch/meilisearch.git
```

Then, compile the Meilisearch binary with `cuda` enabled:

```sh
cargo build --release --features cuda
```

This might take a few moments. Once the compiler is done, you should have a CUDA-compatible Meilisearch binary.

## Configure the Hugging Face embedder

Run your freshly compiled binary:

```sh
./meilisearch
```

Then add the Hugging Face embedder to your index settings:

```sh
curl \
  -X PATCH 'MEILISEARCH_URL/indexes/INDEX_NAME/settings/embedders' \
  -H 'Content-Type: application/json' \
  --data-binary '{ "default": { "source": "huggingFace" } }'
```

Meilisearch will return a summarized task object and queue your request for processing.
