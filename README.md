predicting-flights-conversion
==============================

A project to gather housing data for price and location analysis. Currently this works against RightMove website only.

## Getting Started

Clone this repo, then execute the following command to build your container environment.  

```bash
$ docker-compose build
```

Then copy the credentials template, and complete the sections.

```bash
$ cp src/credentials.txt.template src/credentials.txt
```

Now you can fetch the underlying data, then build up the estimates.

```bash
$ docker-compose run --rm -w /usr/src/app/scripts process python rental_search.py
$ docker-compose run --rm -w /usr/src/app/scripts process python parse_rental_results.py
```

Or, if it is easier, use the Makefile (POSIX systems):

```bash
$ make data
$ make pipeline
```

**Getting a shell**

For this you need the _process_ docker image, which you can get with `docker-compose build process`.

You can start a temporary container with a shell in the working directory by typing `make shell`. When you exit out of this shell the container will be destroyed, but any files you create in the working directory will remain as they are a mapped volume to your host _./src_ directory.

**Jupyter Notebook server**

    1. Run `docker-compose build explore` to build the exploratory analysis image
    2. Run `docker-compose up explore` to start the Jupyter server

This will build the image, and start a container running Jupyter notebook, returning the link to access the notebook.

To run a specific Python script inside the running container: `docker-compose exec explore COMMAND [ARGS...]`.  
Alternatively you can just open a shell session up on the running container: `docker-compose exec explore /bin/bash`.  
To run one off command using that service image (in this case a shell): `docker-compose run --rm -w /home/jovyan/work/scripts explore /bin/bash`. 

## Project Organisation

    ├── README.md                    <- The top-level README for data scientists using this project.
    │
    ├── docker-compose.yml           <- The compose file to configure the containers and set up interactions between each other
    │
    ├── docker                       <- Each directory stores the required content to build a Docker image
    │   ├── explore                  <- Docker image to perform exploratory analysis and develop solutions
    │   │    ├── custom.css          <- Stylesheet to customise Jupyter notebook UI
    │   │    ├── explore.dockerfile  <- Docker image build instructions
    │   │    └── requirements.txt    <- The requirements file for reproducing the analysis environment
    │   │
    │   └── process                  <- Docker image to run adhoc Python scripts
    │       ├── process.dockerfile   <- Docker image build instructions
    │       └── requirements.txt     <- The requirements file for reproducing the scripts environment
    │
    │── Makefile                     <- Makefile with commands like `make data`, `make shell`
    │
    ├── references                   <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports                      <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures                  <- Generated graphics and figures to be used in reporting
    │
    ├── src                          <- Source code for use in this project.
    │   ├── data
    │   │   ├── external             <- Data from third party sources.
    │   │   ├── interim              <- Intermediate data that has been transformed.
    │   │   ├── processed            <- The final, canonical data sets for modeling.
    │   │   └── raw                  <- The original, immutable data dump.
    │   │
    │   │
    │   │── models                   <- Trained and serialized models, model predictions, or model summaries
    │   │
    │   │── notebooks                <- Jupyter notebooks. Naming convention is a number (for ordering),
    │   │                               the creator's initials, and a short `-` delimited description, e.g.
    │   │                               `1.0-jqp-initial-data-exploration`.
    │   │
    │   │── config.yaml              <- Holds project configuration
    │   │
    │   │── credentials.txt          <- Contains your personal credentials for access to data stores
    │   │
    │   └── scripts                  <- Scripts to download or generate data
    │       ├── helpers              <- Helper libraries to navigate the project, query data stores, get credentials etc
    │       └── __init__.py          <- Makes src a Python module

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
