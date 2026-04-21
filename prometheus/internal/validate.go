package internal

import "unicode/utf8"

// SeparatorByte separates hashed label components.
const SeparatorByte byte = 255

// IsValidMetricName reports whether metricName is valid under the default
// UTF-8-based validation used by the stripped client.
func IsValidMetricName(metricName string) bool {
	if len(metricName) == 0 {
		return false
	}
	return utf8.ValidString(metricName)
}

// IsValidLegacyMetricName reports whether metricName uses the legacy Prometheus
// metric-name character set.
func IsValidLegacyMetricName(metricName string) bool {
	if len(metricName) == 0 {
		return false
	}
	for i, b := range metricName {
		if !isValidLegacyMetricRune(b, i) {
			return false
		}
	}
	return true
}

// IsValidLabelName reports whether labelName is valid under the default
// UTF-8-based validation used by the stripped client.
func IsValidLabelName(labelName string) bool {
	if len(labelName) == 0 {
		return false
	}
	return utf8.ValidString(labelName)
}

func isValidLegacyMetricRune(b rune, i int) bool {
	return (b >= 'a' && b <= 'z') ||
		(b >= 'A' && b <= 'Z') ||
		b == '_' ||
		b == ':' ||
		(b >= '0' && b <= '9' && i > 0)
}
