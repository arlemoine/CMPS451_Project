## Setup

1. Clone this repository into the desired directory. Navigate to `/CMPS451_Project/AA_Batteries/` and use the following command to set up the conda environment. *Note: This sets up a new environment with the bare minimum libraries included in the config file, environment.yml.*

```bash
conda env create -f environment.yml
```

2. Activate the environment with the following. *Note: You can switch freely between environments with `conda activate env_name`. You can also list your local environments with `conda env list`.*

```bash
conda activate cmps451
```

3. If the `environment.yml` file is ever adjusted to add new packages or remove them, you can use the following to refresh the list of packages in the environment.

```bash
conda env update --file environment.yml --prune
```

## Help

## Starting Anaconda Navigator more readily

If you can't get `anaconda-navigator` to work without being in the base environment, refer to [this](https://stackoverflow.com/questions/43030871/anaconda-navigator-ubuntu16-04) help article.
