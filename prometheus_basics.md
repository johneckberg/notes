# Prometheus

Prometheus is a system monitoring and alerting system. It was open sourced by SoundCloud in 2012 and is the second project both to join and to graduate within Cloud Native Computing Foundation after Kubernetes.

The basic components of a Prometheus setup are:

    - Prometheus Server (the server which scrapes and stores the metrics data).
    - Targets to be scraped, for example an instrumented application that exposes its metrics, or an exporter that exposes metrics of another application.
    - Alertmanager to raise alerts based on preset rules.

Prometheus is so ubiquitous in the monitoring space that many tools natively emit metrics in Prometheus format. Prometheus provides a time-series data store you can use for your metrics, in addition to instrumentation clients. I make this note because there is a million forum posts online about "OTel vs prometheus" or "OTel and prometheus".

## OTel vs Prometheus

OTel is primarily focused on the instrumentation part of observability, it doesn’t provide a backend for storing telemetry; you have to forward the data to a backend vendor for storage, alerting, and querying. That being said, OTel also does stuff like tracing and is definitely a more robust instrumentation framework. 

One of the big benefits of OTEL is the OpenTelemetry Protocol (OTLP). It describes the encoding, transport, and delivery mechanism of telemetry data between telemetry sources, intermediate nodes such as collectors and telemetry backends. Prometheus supports OTLP (aka "OpenTelemetry Protocol") ingestion through HTTP, so you can do things like for example; using Prometheus as your OpenTelemetry backend.

That being said, (and I will cover this in detail in the OTel notes), some people hate what OTel has become. [See for example this reddit comment.](https://www.reddit.com/r/sre/comments/1clre50/comment/l2w3y1z/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) 

"OTel has single handedly taken a stinking shit on all the hard work that went into making a common metrics platform out of the Prometheus data model. We were very close to having a viable, used in production, real working code, community driven standard for metrics to replace SNMP. But it's all down the toilet thanks to OTel. The OTel metrics are a shitshow of design-by-committee non-interoperable garbage. I wish they had just stuck to what they knew, Tracing."


## A Quick Note on Cardinality Spikes

When dealing with time series from Prometheus, you will end up in a situation where you have many different time series for a particular metric. We would like to track events individually, so we end up taking the cartesian product of the sets of label values. The cardinality of this cartesian product is the cardinality of the metric; how many individual time series we have.

![cardinality spike grafana](https://grafana.com/static/assets/img/blog/cardinality-spikes-diagram.jpg)

In the example above, the metric has the label status_code has a cardinality of 5, environment has a cardinality of 2, and the overall cardinality of the metric server_responses is 10. Cardinality spikes are expensive because as always, data is a very expensive physical asset. You can 100% generate more data than you need. For example: When you instrument your code and add a new metric, sometimes you attach more context than you need. For example, if you use the label “user_id”, user id will become a label for that metric. Since Prometheus creates one series per label combination, you will end up with a lot of series for a single metric if you have a lot of users. 