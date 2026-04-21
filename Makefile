SHELL:=bash

PROTOC ?= protoc
PROTOC_GEN_GO_LITE ?= $(HOME)/company/bin/protoc-gen-go-lite

all:

.PHONY: build
build:
	go build ./...

.PHONY: vendor
vendor:
	go mod vendor

.PHONY: test
test:
	go test ./...

.PHONY: lint
lint:
	GOFLAGS=-mod=mod go run github.com/golangci/golangci-lint/v2/cmd/golangci-lint run --timeout=10m

.PHONY: fix
fix:
	GOFLAGS=-mod=mod go run github.com/golangci/golangci-lint/v2/cmd/golangci-lint run --fix --timeout=10m

.PHONY: format
format:
	gofmt -w ./

.PHONY: gengo
gengo:
	PATH="$$(dirname $(PROTOC_GEN_GO_LITE)):$$PATH" \
	$(PROTOC) \
		--plugin=protoc-gen-go-lite="$(PROTOC_GEN_GO_LITE)" \
		--go-lite_out=. \
		--go-lite_opt=paths=source_relative \
		--go-lite_opt=features=equal \
		--go-lite_opt=Mgoogle/protobuf/timestamp.proto=github.com/aperturerobotics/protobuf-go-lite/types/known/timestamppb \
		client_model/go/metrics.proto
	gofmt -w client_model/go/metrics.pb.go
