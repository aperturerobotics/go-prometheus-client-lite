//go:build deps_only

package goprometheusclientlite

import (
	// _ imports common with the tools like protoc.
	_ "github.com/aperturerobotics/common"
	// _ imports common aptre cli.
	_ "github.com/aperturerobotics/common/cmd/aptre"
)
