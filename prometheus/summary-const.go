package prometheus

import (
	"sort"
	"time"

	dto "github.com/aperturerobotics/go-prometheus-client-lite/client_model/go"
	"github.com/aperturerobotics/go-prometheus-client-lite/proto"
	"github.com/aperturerobotics/protobuf-go-lite/types/known/timestamppb"
)

// quantileLabel is used for the label that defines the quantile in summaries.
const quantileLabel = "quantile"

type constSummary struct {
	desc       *Desc
	count      uint64
	sum        float64
	quantiles  map[float64]float64
	labelPairs []*dto.LabelPair
	createdTs  *timestamppb.Timestamp
}

func (s *constSummary) Desc() *Desc {
	return s.desc
}

func (s *constSummary) Write(out *dto.Metric) error {
	sum := &dto.Summary{
		SampleCount:      proto.Uint64(s.count),
		SampleSum:        proto.Float64(s.sum),
		CreatedTimestamp: s.createdTs,
	}

	qs := make([]*dto.Quantile, 0, len(s.quantiles))
	for rank, q := range s.quantiles {
		qs = append(qs, &dto.Quantile{
			Quantile: proto.Float64(rank),
			Value:    proto.Float64(q),
		})
	}
	sort.Sort(quantSort(qs))
	sum.Quantile = qs

	out.Label = s.labelPairs
	out.Summary = sum
	return nil
}

// NewConstSummary returns a summary metric with fixed values.
func NewConstSummary(
	desc *Desc,
	count uint64,
	sum float64,
	quantiles map[float64]float64,
	labelValues ...string,
) (Metric, error) {
	if desc.err != nil {
		return nil, desc.err
	}
	if err := validateLabelValues(labelValues, len(desc.variableLabels.names)); err != nil {
		return nil, err
	}
	if quantiles == nil {
		quantiles = map[float64]float64{}
	}

	return &constSummary{
		desc:       desc,
		count:      count,
		sum:        sum,
		quantiles:  quantiles,
		labelPairs: MakeLabelPairs(desc, labelValues),
	}, nil
}

// MustNewConstSummary panics where NewConstSummary would have returned an error.
func MustNewConstSummary(
	desc *Desc,
	count uint64,
	sum float64,
	quantiles map[float64]float64,
	labelValues ...string,
) Metric {
	m, err := NewConstSummary(desc, count, sum, quantiles, labelValues...)
	if err != nil {
		panic(err)
	}
	return m
}

// NewConstSummaryWithCreatedTimestamp returns a summary metric with fixed
// values and created timestamp.
func NewConstSummaryWithCreatedTimestamp(
	desc *Desc,
	count uint64,
	sum float64,
	quantiles map[float64]float64,
	ct time.Time,
	labelValues ...string,
) (Metric, error) {
	m, err := NewConstSummary(desc, count, sum, quantiles, labelValues...)
	if err != nil {
		return nil, err
	}
	cs := m.(*constSummary)
	cs.createdTs = timestamppb.New(ct)
	return cs, nil
}

// MustNewConstSummaryWithCreatedTimestamp panics where
// NewConstSummaryWithCreatedTimestamp would have returned an error.
func MustNewConstSummaryWithCreatedTimestamp(
	desc *Desc,
	count uint64,
	sum float64,
	quantiles map[float64]float64,
	ct time.Time,
	labelValues ...string,
) Metric {
	m, err := NewConstSummaryWithCreatedTimestamp(desc, count, sum, quantiles, ct, labelValues...)
	if err != nil {
		panic(err)
	}
	return m
}

type quantSort []*dto.Quantile

func (s quantSort) Len() int {
	return len(s)
}

func (s quantSort) Less(i, j int) bool {
	return s[i].GetQuantile() < s[j].GetQuantile()
}

func (s quantSort) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}
