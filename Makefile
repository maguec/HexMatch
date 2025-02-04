default: help

##@ Utility
help:  ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)


loadschema: ## Load Schema onto Spanner
	@echo "Loading Schema"
	@gcloud spanner databases create hexmatchdb --instance  hexmatch --ddl-file=HexMatchDB.sql

instancecreate: ## Spin up a single node Spanner instance
	@gcloud spanner instances create hexmatch --description="HexMatch Database" --config=regional-us-west1 --edition=ENTERPRISE --processing-units=100 --default-backup-schedule-type=NONE

instancedelete: ## Shutdown the Spanner instance
	@gcloud spanner instances delete hexmatch

dbclean: ## Remove all  table dat
	@gcloud spanner databases execute-sql hexmatchdb  --instance=hexmatch --sql='DELETE from Hex WHERE id < 100000000;'
	@gcloud spanner databases execute-sql hexmatchdb  --instance=hexmatch --sql='DELETE from Provider WHERE id < 100000000;'
	@gcloud spanner databases execute-sql hexmatchdb  --instance=hexmatch --sql='DELETE from Consumer WHERE id < 100000000;'
	@gcloud spanner databases execute-sql hexmatchdb  --instance=hexmatch --sql='DELETE from HasProvider WHERE id < 100000000;'
	@gcloud spanner databases execute-sql hexmatchdb  --instance=hexmatch --sql='DELETE from HasConsumer WHERE id < 100000000;'
	@gcloud spanner databases execute-sql hexmatchdb  --instance=hexmatch --sql='DELETE from HasAdjacent WHERE id < 100000000;'


dbdrop: ## Drop all tables DANGER
	@gcloud spanner databases  delete  hexmatchdb --instance hexmatch
