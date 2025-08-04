# Exporters & Clients

note: Prometheus metrics and label names are written in snake_case.

This will cover the basics of instrumenting your own system, instrumentation on third party systems, and  how to export the data to prometheus.

## Metric Types

| Metric Type | Description |
| :--- | :--- |
| **Counter** | A cumulative metric that only increases. It's used for things like request counts or errors. |
| **Gauge** | A metric that can be set to any value. It's used for things that can go up and down, like CPU usage or memory consumption. |
| **Histogram** | Samples observations and buckets them. It's used for things like request durations and response sizes. |
| **Summary** | Similar to a Histogram, but calculates configurable quantiles over a sliding time window. |

## Prometheus instrumentation Client opinions/guidelines

Before you can monitor your own services, you need to add instrumentation to their code via one of the Prometheus client libraries. Once an application is instrumented, the client library automatically manages the exposure of these collected metrics. This is typically done via a standard HTTP /metrics endpoint on the application instance itself. The Prometheus server is then configured to periodically scrape this endpoint, pulling the current state of all tracked metrics into its time-series database.

For monitoring purposes, services can generally be broken down into three types: online-serving, offline-processing, and batch jobs. There is overlap between them, but every service tends to fit well into one of these categories.

### Online-serving

An online-serving system is one where a human or another system is expecting an immediate response. For example, most database and HTTP requests fall into this category.

The key metrics in such a system are the number of performed queries, errors, and latency. The number of in-progress requests can also be useful.

### Offline-processing

For offline processing, no one is actively waiting for a response, and batching of work is common. There may also be multiple stages of processing.

For each stage, track the items coming in, how many are in progress, the last time you processed something, and how many items were sent out. If batching, you should also track batches going in and out.

Knowing the last time that a system processed something is useful for detecting if it has stalled, but it is very localised information. A better approach is to send a heartbeat through the system: some dummy item that gets passed all the way through and includes the timestamp when it was inserted. Each stage can export the most recent heartbeat timestamp it has seen, letting you know how long items are taking to propagate through the system.

### Batch jobs

There is a fuzzy line between offline-processing and batch jobs, as offline processing may be done in batch jobs. Batch jobs are distinguished by the fact that they do not run continuously, which makes scraping them difficult.

The key metric of a batch job is the last time it succeeded. It is also useful to track how long each major stage of the job took, the overall runtime and the last time the job completed (successful or failed).

## Writing Exporters

So what about third party services?

When taking metrics from another monitoring or instrumentation system, things tend not to be so black and white. 
An exporter is a separate program that runs alongside the system you want to monitor (e.g., a database, a web server like Nginx, or the Linux OS itself). The exporter's job is to connect to the third-party system, collect its existing metrics, and then expose those metrics in the Prometheus format on its own HTTP endpoint. The key here is that exporters use the native interfaces of the service; such as APIs, logs, system calls, JMX (Java Management Extensions), or SNMP (Simple Network Management Protocol) to gather relevant data. Once collected, the exporter transforms this data into Prometheus's standardized multi-dimensional metric format. After conversion, thats when the metrics are exposed by the exporter (via a standard HTTP).

To quote the prometheus website, "The main decision you need to make when writing an exporter is how much work you’re willing to put in to get perfect metrics out of it."
