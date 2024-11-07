# Galaxy clustering model selection based on $f\sigma_8$ data

![License Badge](https://img.shields.io/badge/license-MIT-brightgreen.svg)

## Table of Contents

- [Overview](#overview)
- [Description](#Description)
- [Installation](#installation)
- [Usage](#usage)
- [Acknowledgements](#acknowledgements)

---

## Overview


This repo contains the codes used for the ML analysis in arXiv:2411.04058. The aim is to perform model selection between ΛCDM and a Coupled Dark Energy (CDE) model (see arXiv:2211.13588) with the growth rate $f\sigma_8$ data. This folder contains:
1. The $f\sigma_8$ data creation file within the context of the modified version of \texttt{CLASS} for this CDE model: https://github.com/LisaGoh/CDE (python)
2. The Neural Network for model classification CDE and ΛCDM, for the $\beta_1$ activation case. (jupyter notebook)
3. The Neural Network for the multi-class case $\beta_1$ and $\beta_2 + \beta_3$. (jupyter notebook)

## Installation

### Prerequisites

- Required software: `python`
- Dependencies: `numpy`, `matplotlib`, `tensorflow`, `class`

### How to get started

```bash
# Example to get it running
pip install numpy matplotlib tensorflow
git clone https://github.com/IndiraOcampo/Growth_LSS_model_selection.git
```

## Usage

If you are using the content provided in this repository to do your own analysis, please cite this repository and the manuscript:

```bash
@misc{[Growth_LSS_model_selection_Coupled_Dark_Energy,
  authors = {Ocampo I, Goh L},
  title = {Growth LSS model selection},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/IndiraOcampo/Growth_LSS_model_selection_Coupled_Dark_Energy.git}},
}
```

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/IndiraOcampo/Growth_LSS_model_selection_CDE/blob/main/LICENSE) file for details.
