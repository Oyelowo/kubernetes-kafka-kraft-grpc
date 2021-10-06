Use kafka for connections cos it is event-based/driven service and there can be a lot of connections from even fewer users. So, Kafka might help provide some buffer


First, put location into it's own service as it has no dependence, although, connection service depends on location model/ data. We can as well say it depends on location service.
