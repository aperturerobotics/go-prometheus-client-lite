package proto

import "reflect"

type equaler interface {
	EqualMessageVT(any) bool
}

// String returns a pointer to v.
func String(v string) *string { return &v }

// Float64 returns a pointer to v.
func Float64(v float64) *float64 { return &v }

// Uint64 returns a pointer to v.
func Uint64(v uint64) *uint64 { return &v }

// Int64 returns a pointer to v.
func Int64(v int64) *int64 { return &v }

// Uint32 returns a pointer to v.
func Uint32(v uint32) *uint32 { return &v }

// Int32 returns a pointer to v.
func Int32(v int32) *int32 { return &v }

// Equal compares protobuf-go-lite messages with generated equality when available.
func Equal(a, b any) bool {
	if a == nil || b == nil {
		return a == b
	}
	if eq, ok := a.(equaler); ok {
		return eq.EqualMessageVT(b)
	}
	return reflect.DeepEqual(a, b)
}
