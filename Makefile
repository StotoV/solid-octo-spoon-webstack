.PHONY: dev e2e clean

DEV_DC = docker-compose
dev:
	$(DEV_DC) up --build

E2E_DC = docker-compose -f docker-compose.yml -f docker-compose.cypress.yml -p e2e
e2e:
	$(E2E_DC) build
	$(E2E_DC) up --exit-code-from cypress

clean:
	$(DEV_DC) stop
	$(DEV_DC) rm -f
	$(E2E_DC) stop
	$(E2E_DC) rm -f
