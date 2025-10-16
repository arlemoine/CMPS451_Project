# CMPS 451

## Contents

- [1 General](#1-general)
- [2 Contributor Notes](#2-contributor-notes)
    - [2.1 Adding and Removing Libraries](#21-adding-and-removing-libraries)
- [3 Setup](#3-setup)

## 1 General

Team Name: Team Regular
Members: Alameen Adeku, Adam Rodi, Adriean Lemoine, Nicholas Burgo

## 2 Contributor Notes

#### 2.1 Adding and Removing Libraries

- If the `environment.yml` file is ever adjusted to add new packages or remove them, you can use the following to refresh the list of packages in the environment.

```bash
conda env update --file environment.yml --prune
```

## 3 Setup

1. Clone this repository into the desired directory. Navigate to `/CMPS451_Project/` and use the following command to set up the conda environment. *Note: This sets up a new environment with the bare minimum libraries included in the config file, environment.yml.*

```bash
conda env create -f environment.yml
```

2. Activate the environment with the following. *Note: You can switch freely between environments with `conda activate env_name`. You can also list your local environments with `conda env list`.*

```bash
conda activate cmps451
```
