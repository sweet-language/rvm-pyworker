from vastai import Worker, WorkerConfig, HandlerConfig, BenchmarkConfig, LogActionConfig

worker_config = WorkerConfig(
    model_server_url="http://127.0.0.1",
    model_server_port=18000,
    model_log_file="/var/log/model/server.log",
    handlers=[
        HandlerConfig(
            route="/matting",
            allow_parallel_requests=False,
            max_queue_time=600.0,
            workload_calculator=lambda p: 100.0,
            benchmark_config=BenchmarkConfig(
                generator=lambda: {"health": True},
                runs=1,
                concurrency=1,
            ),
        ),
    ],
    log_action_config=LogActionConfig(
        on_load=["Application startup complete."],
        on_error=["Traceback"],
        on_info=["Inference:", "DONE"],
    ),
)

Worker(worker_config).run()
