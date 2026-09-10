def state_tracking():

    previous = 0
    running_sum = 0

    for current in range(0, 10):
        running_sum += current
        print(f"Current {current} Previous {previous} Sum {running_sum}")
        previous = current

def main():

    state_tracking()

main()