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
