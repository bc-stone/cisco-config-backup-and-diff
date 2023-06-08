# cisco-config-backup-and-diff
### Automated Cisco router / switch config backup with optional diff

Uses the Netmiko Python library to connect to a device, retrieve the config and save the results to a text file.
The ```config_type``` variable can be changed as necessary (from "running" to "startup", etc.
)

```get_device_config.py``` runs asynchronously with concurrent.futures thread pools.  The number of threads can be adjusted with the ```max_threads``` variable.

```device_list.py``` is provided as a template for externally storing the necessary device connection information as a list of Python dictionaries.  It currently consists of two Cisco always-on sandbox
devices whose usernames and passwords change periodically, so YMMV if using them to test.

```config_diff.py``` creates a side-by-side html diff of two files, color-codes additions, deletions or edits and optionally opens the diff in the default web browser.