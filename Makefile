#################################################################################
# GLOBALS                                                                       #
#################################################################################

BUCKET = 
PROJECT_NAME = predicting-flights-conversion

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Clean downloaded data files
clean-all:
	rm -f src/data/**/*

clean:
	rm -f src/data/interim/* src/data/processed/*

explore:
	docker-compose up -d explore

explore-shell:
	docker-compose run --rm -w /home/jovyan/work/scripts explore /bin/bash

data:
	docker-compose run --rm -w /usr/src/app/scripts process python rental_search.py

pipeline:
	docker-compose run --rm -w /usr/src/app/scripts process python run_pipeline.py

shell:
	docker-compose run --rm process /bin/bash
