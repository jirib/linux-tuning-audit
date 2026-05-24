# Linux tuning audit tool

`linux-tuning-audit` is a CLI tool which compares Linux OS tunings with
recommendations from platform providers (for example, Azure, AWS,...).

Examples:

``` shell
$ linux-tuning-audit audit \
  --profile azure-network \
  --profile azure-sap-hana-scale-out-netapp \
  --evidence supportconfig \
  --path /tmp/scc_host_250524_1200

$ linux-tuning-audit audit \
  --profile azure-network \
  --evidence sosreport \
  --path /tmp/sosreport-host-2026-05-24
```


## Installation

...

## Scraping recommendations

``` shell
$ uv run python tools/scrape_profiles/scrape.py \
  --profile azure_network \
  --output /tmp/azure_network.generated.yaml

$ diff -u data/profiles/azure_network.yaml /tmp/azure_network.generated.yaml
```
