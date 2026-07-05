# go-prometheus-client-lite

[![Tests](https://github.com/aperturerobotics/go-prometheus-client-lite/actions/workflows/tests.yml/badge.svg)](https://github.com/aperturerobotics/go-prometheus-client-lite/actions/workflows/tests.yml)
[![Go Reference](https://pkg.go.dev/badge/github.com/aperturerobotics/go-prometheus-client-lite.svg)](https://pkg.go.dev/github.com/aperturerobotics/go-prometheus-client-lite)

`go-prometheus-client-lite` is a stripped-down fork of
[prometheus/client_golang](https://github.com/prometheus/client_golang)
maintained for Aperture Robotics. It keeps the in-process instrumentation and
registry surface we want for host-bus metrics while dropping the larger
exporter, API-client, and process-scrape surfaces we do not need.

This fork also replaces the upstream `client_model` / protobuf runtime stack
with a local `client_model/go` package generated with
[protobuf-go-lite](https://github.com/aperturerobotics/protobuf-go-lite).
That keeps the retained DTO surface lightweight and avoids the
`google.golang.org/protobuf` dependency tree.

The code generation flow follows the same pattern used in
`repos/bifrost`: `package.json` drives
`github.com/aperturerobotics/common/cmd/aptre`, which runs the embedded WASM
`protoc` pipeline from the shared `common` tooling.

This module is available at
`github.com/aperturerobotics/go-prometheus-client-lite`.

## Retained surface

- `prometheus` counters, gauges, histograms, descriptors, registries, and
  gatherers
- the Go collector
- the build info collector
- const-summary support required by the retained Go collector path

## Removed surface

- Prometheus HTTP API client packages
- `promhttp`, `push`, `graphite`, `promauto`, and `testutil`
- process collector registration and the process collector implementation
- example, tutorial, and experimental package trees
- upstream protobuf/client_model runtime dependencies

## Regenerating the DTOs

The retained DTO package is generated from
[`client_model/go/metrics.proto`](client_model/go/metrics.proto) with the
shared `aptre` flow.

```bash
bun install
bun run gen
```

This uses the shared WASM-based protoc pipeline from `common`, plus the
lightweight protobuf plugins vendored through `.tools/`. There is no native
`protoc` prerequisite for normal generation.

## Scope

This fork is intentionally not a drop-in replacement for the full upstream
Prometheus Go client. It is meant for lightweight in-process collection and
local metric gathering where the removed exporter/client surfaces are not
needed.
