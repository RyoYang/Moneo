
import http.client
import requests
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
from prometheus_client.parser import text_string_to_metric_families
import urllib

metrics_ports = '8000,8001'
metrics_port_list = metrics_ports.split(',')

for port in metrics_port_list:
    metrics_url = f"http://localhost:{port}/metrics"
    print('this is the metrics from port: ' + port)
    response = urllib.request.urlopen(metrics_url)
    content = response.read().decode('utf-8')
    metric_families = text_string_to_metric_families(content)
    metrics_dict = {}
    for metric_family in metric_families:
        for sample in metric_family.samples:
            metric_name = sample.name
            metric_value = sample.value
            metric_labels = sample.labels
            if metric_name not in metrics_dict:
                metrics_dict[metric_name] = {}
            metrics_dict[metric_name][str(metric_labels)] = metric_value
    print(metrics_dict)
