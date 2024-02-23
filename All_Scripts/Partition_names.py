import psutil

def get_partition_names():
    partitions = psutil.disk_partitions()
    return [partition.device for partition in partitions]


def main():
    partition_names = get_partition_names()

    if partition_names:
        print("Partition Names:")
        for name in partition_names:
            print(name)
    else:
        print("No partitions found.")


if __name__ == "__main__":
    main()
