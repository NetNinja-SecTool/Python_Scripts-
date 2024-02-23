import psutil

def get_partition_sizes():
    partitions = psutil.disk_partitions()
    partition_sizes = {}

    for partition in partitions:
        partition_name = partition.device
        try:
            partition_info = psutil.disk_usage(partition_name)
            partition_sizes[partition_name] = partition_info.total
        except PermissionError as e:
            print(f"Error getting information for partition {partition_name}: {e}")

    return partition_sizes


def main():
    partition_sizes = get_partition_sizes()

    if partition_sizes:
        print("Partition Sizes:")
        for partition_name, size in partition_sizes.items():
            print(f"{partition_name}: {size / (1024 ** 3):.2f} GB")
    else:
        print("No partitions found.")


if __name__ == "__main__":
    main()
