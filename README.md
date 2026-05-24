# Linux tuning audit tool

`linux-tuning-audit` is a CLI tool which compares Linux OS tunings with
recommendations from platform providers (for example, Azure, AWS,...).

Examples:

``` shell
$ linux-tuning-audit scrape \
  --profile azure_generic \
  --profile azure_nfs \
  --profile azure_sap_hana_netapp_files
```

``` shell
$ linux-tuning-audit audit \
  --profile azure/sap-hana-scale-out-netapp \
  --evidence supportconfig \
  --path /tmp/scc_host_250524_1200

$ linux-tuning-audit audit \
  --profile azure/network \
  --evidence sosreport \
  --path /tmp/sosreport-host-2026-05-24
```


## Installation

...

## Tools

### Updating profiles

Use the following script to update recommended tunning profiles in `data/profiles`.

``` shell
$ tools/scrape_recommendations.py
```

``` shell
.
├── pyproject.toml
├── README.md
├── data/
│   └── profiles/
│       ├── azure/
│       │   ├── network.yaml
│       │   └── sap-hana-scale-out-netapp.yaml
│       └── aws/
│           └── example.yaml
├── src/
│   └── linux_tuning_audit/
│       ├── __init__.py
│       ├── __main__.py
│       ├── cli.py
│       ├── app.py
│       ├── models.py
│       ├── profiles.py
│       ├── compare.py
│       ├── evidence/
│       │   ├── __init__.py
│       │   ├── base.py
│       │   ├── live.py
│       │   ├── sosreport.py
│       │   ├── supportconfig.py
│       │   ├── sysctl.py
│       │   └── modules.py
│       ├── scrape/
│       │   ├── __init__.py
│       │   ├── fetch.py
│       │   ├── registry.py
│       │   ├── models.py
│       │   └── plugins/
│       │       ├── __init__.py
│       │       ├── azure_network.py
│       │       ├── azure_sap_hana_scale_out_netapp.py
│       │       └── aws_example.py
│       └── output/
│           ├── __init__.py
│           └── report.py
└── tests/
    ├── test_compare.py
    ├── test_profiles.py
    └── test_scrape_plugins.py
```



