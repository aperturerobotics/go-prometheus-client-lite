//go:build js && !wasm
// +build js,!wasm

package prometheus

// getRuntimeNumThreads returns the number of open OS threads.
func getRuntimeNumThreads() float64 {
	return 1
}
