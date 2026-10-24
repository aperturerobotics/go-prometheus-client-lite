import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MetricType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COUNTER: _ClassVar[MetricType]
    GAUGE: _ClassVar[MetricType]
    SUMMARY: _ClassVar[MetricType]
    UNTYPED: _ClassVar[MetricType]
    HISTOGRAM: _ClassVar[MetricType]
    GAUGE_HISTOGRAM: _ClassVar[MetricType]
COUNTER: MetricType
GAUGE: MetricType
SUMMARY: MetricType
UNTYPED: MetricType
HISTOGRAM: MetricType
GAUGE_HISTOGRAM: MetricType

class LabelPair(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class Gauge(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: float
    def __init__(self, value: _Optional[float] = ...) -> None: ...

class Counter(_message.Message):
    __slots__ = ("value", "exemplar", "created_timestamp")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EXEMPLAR_FIELD_NUMBER: _ClassVar[int]
    CREATED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    value: float
    exemplar: Exemplar
    created_timestamp: _timestamp_pb2.Timestamp
    def __init__(self, value: _Optional[float] = ..., exemplar: _Optional[_Union[Exemplar, _Mapping]] = ..., created_timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Quantile(_message.Message):
    __slots__ = ("quantile", "value")
    QUANTILE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    quantile: float
    value: float
    def __init__(self, quantile: _Optional[float] = ..., value: _Optional[float] = ...) -> None: ...

class Summary(_message.Message):
    __slots__ = ("sample_count", "sample_sum", "quantile", "created_timestamp")
    SAMPLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_SUM_FIELD_NUMBER: _ClassVar[int]
    QUANTILE_FIELD_NUMBER: _ClassVar[int]
    CREATED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    sample_count: int
    sample_sum: float
    quantile: _containers.RepeatedCompositeFieldContainer[Quantile]
    created_timestamp: _timestamp_pb2.Timestamp
    def __init__(self, sample_count: _Optional[int] = ..., sample_sum: _Optional[float] = ..., quantile: _Optional[_Iterable[_Union[Quantile, _Mapping]]] = ..., created_timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Untyped(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: float
    def __init__(self, value: _Optional[float] = ...) -> None: ...

class Histogram(_message.Message):
    __slots__ = ("sample_count", "sample_count_float", "sample_sum", "bucket", "created_timestamp", "schema", "zero_threshold", "zero_count", "zero_count_float", "negative_span", "negative_delta", "negative_count", "positive_span", "positive_delta", "positive_count", "exemplars")
    SAMPLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_COUNT_FLOAT_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_SUM_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    CREATED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    ZERO_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    ZERO_COUNT_FIELD_NUMBER: _ClassVar[int]
    ZERO_COUNT_FLOAT_FIELD_NUMBER: _ClassVar[int]
    NEGATIVE_SPAN_FIELD_NUMBER: _ClassVar[int]
    NEGATIVE_DELTA_FIELD_NUMBER: _ClassVar[int]
    NEGATIVE_COUNT_FIELD_NUMBER: _ClassVar[int]
    POSITIVE_SPAN_FIELD_NUMBER: _ClassVar[int]
    POSITIVE_DELTA_FIELD_NUMBER: _ClassVar[int]
    POSITIVE_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXEMPLARS_FIELD_NUMBER: _ClassVar[int]
    sample_count: int
    sample_count_float: float
    sample_sum: float
    bucket: _containers.RepeatedCompositeFieldContainer[Bucket]
    created_timestamp: _timestamp_pb2.Timestamp
    schema: int
    zero_threshold: float
    zero_count: int
    zero_count_float: float
    negative_span: _containers.RepeatedCompositeFieldContainer[BucketSpan]
    negative_delta: _containers.RepeatedScalarFieldContainer[int]
    negative_count: _containers.RepeatedScalarFieldContainer[float]
    positive_span: _containers.RepeatedCompositeFieldContainer[BucketSpan]
    positive_delta: _containers.RepeatedScalarFieldContainer[int]
    positive_count: _containers.RepeatedScalarFieldContainer[float]
    exemplars: _containers.RepeatedCompositeFieldContainer[Exemplar]
    def __init__(self, sample_count: _Optional[int] = ..., sample_count_float: _Optional[float] = ..., sample_sum: _Optional[float] = ..., bucket: _Optional[_Iterable[_Union[Bucket, _Mapping]]] = ..., created_timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., schema: _Optional[int] = ..., zero_threshold: _Optional[float] = ..., zero_count: _Optional[int] = ..., zero_count_float: _Optional[float] = ..., negative_span: _Optional[_Iterable[_Union[BucketSpan, _Mapping]]] = ..., negative_delta: _Optional[_Iterable[int]] = ..., negative_count: _Optional[_Iterable[float]] = ..., positive_span: _Optional[_Iterable[_Union[BucketSpan, _Mapping]]] = ..., positive_delta: _Optional[_Iterable[int]] = ..., positive_count: _Optional[_Iterable[float]] = ..., exemplars: _Optional[_Iterable[_Union[Exemplar, _Mapping]]] = ...) -> None: ...

class Bucket(_message.Message):
    __slots__ = ("cumulative_count", "cumulative_count_float", "upper_bound", "exemplar")
    CUMULATIVE_COUNT_FIELD_NUMBER: _ClassVar[int]
    CUMULATIVE_COUNT_FLOAT_FIELD_NUMBER: _ClassVar[int]
    UPPER_BOUND_FIELD_NUMBER: _ClassVar[int]
    EXEMPLAR_FIELD_NUMBER: _ClassVar[int]
    cumulative_count: int
    cumulative_count_float: float
    upper_bound: float
    exemplar: Exemplar
    def __init__(self, cumulative_count: _Optional[int] = ..., cumulative_count_float: _Optional[float] = ..., upper_bound: _Optional[float] = ..., exemplar: _Optional[_Union[Exemplar, _Mapping]] = ...) -> None: ...

class BucketSpan(_message.Message):
    __slots__ = ("offset", "length")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    offset: int
    length: int
    def __init__(self, offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class Exemplar(_message.Message):
    __slots__ = ("label", "value", "timestamp")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    label: _containers.RepeatedCompositeFieldContainer[LabelPair]
    value: float
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, label: _Optional[_Iterable[_Union[LabelPair, _Mapping]]] = ..., value: _Optional[float] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Metric(_message.Message):
    __slots__ = ("label", "gauge", "counter", "summary", "untyped", "histogram", "timestamp_ms")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    GAUGE_FIELD_NUMBER: _ClassVar[int]
    COUNTER_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    UNTYPED_FIELD_NUMBER: _ClassVar[int]
    HISTOGRAM_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_MS_FIELD_NUMBER: _ClassVar[int]
    label: _containers.RepeatedCompositeFieldContainer[LabelPair]
    gauge: Gauge
    counter: Counter
    summary: Summary
    untyped: Untyped
    histogram: Histogram
    timestamp_ms: int
    def __init__(self, label: _Optional[_Iterable[_Union[LabelPair, _Mapping]]] = ..., gauge: _Optional[_Union[Gauge, _Mapping]] = ..., counter: _Optional[_Union[Counter, _Mapping]] = ..., summary: _Optional[_Union[Summary, _Mapping]] = ..., untyped: _Optional[_Union[Untyped, _Mapping]] = ..., histogram: _Optional[_Union[Histogram, _Mapping]] = ..., timestamp_ms: _Optional[int] = ...) -> None: ...

class MetricFamily(_message.Message):
    __slots__ = ("name", "help", "type", "metric", "unit")
    NAME_FIELD_NUMBER: _ClassVar[int]
    HELP_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    METRIC_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    name: str
    help: str
    type: MetricType
    metric: _containers.RepeatedCompositeFieldContainer[Metric]
    unit: str
    def __init__(self, name: _Optional[str] = ..., help: _Optional[str] = ..., type: _Optional[_Union[MetricType, str]] = ..., metric: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., unit: _Optional[str] = ...) -> None: ...
