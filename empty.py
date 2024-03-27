atom all_checks.py
#!/usr/binenv python3
(...)
## feature2 1234 local
def check_disk_full(disk, min_gb, min_percent):
    """Returns True if there isn't enough disk space, False otherwise."""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_gb:
        return True
    return False
## added this comment 1353
# comment 1403 remote
# feature-br comment added remotely 1523
def main(): 
    if check_reboot():
        print("Pending Reboot.")
        sys_exit(1)
    if check_disk_full(disk="/", min_gb=2, min_percent=10):
        print("Disk full.")
        sys.exit(1)
    
    print("Everything ok")
    sys.exit(0)
## added this comment 1349
# feature2-br local 1224

main()
