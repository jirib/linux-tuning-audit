# Linux tuning audit tool

`linux-tuning-audit` is a CLI tool which compares Linux OS tunings with
recommendations from platform providers (for example, Azure, AWS,...).

Examples:

``` shell
$ linux-audit-tool --help
usage: linux-audit-tool [-h] [-d] -p <profile1,profile2> -s <sysctl-output-file> -m <sysfs modules parameter output>
```

## Installation

...

## Tools

### Updating profiles

Use the following script to update recommended tunning profiles in `data/profiles`.

``` shell
$ tools/scrape_recommendations.py
```