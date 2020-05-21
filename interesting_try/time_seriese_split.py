# Initialization
time_series = [x for x in range(1,37)]

# Set up parameters
history_size = 12
future_size = 10

# resize the data
def time_series_data_split(time_series_data, history_size, future_size):
    data = []
    labels = []

    # Check Intializations
    print("The Original Data: ", time_series)
    print("History Size: ", history_size)
    print("Future Size: ", future_size)

    for i in range(len(time_series_data) - history_size - future_size + 1):
        data.append(time_series[i:history_size+i])
        labels.append(time_series[i + history_size + future_size-1])
        print(data[i], labels[i])

# Check the interesting function
def printing(flag = 0):
    print("No setting flag") if flag == 0 else print("The flag is set up.")

if __name__ == "__main__":
    printing(1)

