.PHONY: install format lint test clean build run deploy all help

help:  ## Display this help message
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

install:  ## Install required packages
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:  ## Format the code
	black *.py calculate_real_return/*.py

lint:  ## Lint the code
	pylint --disable=R,C,W1203,W0718,W0611 *.py calculate_real_return/*.py

test:  ## Run the tests (uncomment when ready)
	pytest test_calculate_return.py

clean:  ## Clean the workspace
	rm -rf ./__pycache__ ./.pytest_cache

build:  ## Build Docker container
	#docker build -t your_image_name .

run:  ## Run Docker container
	#docker run -p 8501:8501 your_image_name

deploy:  ## Deploy (uncomment when ready)
	# Your deploy commands here

all: install format lint test clean  ## Run all commands (default)
