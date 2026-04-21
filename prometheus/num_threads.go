//go:build !js || wasm

package prometheus

import "runtime"

// getRuntimeNumThreads returns the number of open OS threads.
func getRuntimeNumThreads() float64 {
	n, _ := runtime.ThreadCreateProfile(nil)
	return float64(n)
}
