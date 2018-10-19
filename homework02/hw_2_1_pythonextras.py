import datetime

# exercise:
# 1)
# Calculate random persons 10 000th day

# 2)
# When will they be 1.000.000.000 seconds old?


if __name__ == '__main__':
    now = datetime.datetime.now()

    since_birth = now - datetime.datetime(1988, 2, 3, 6, 35)
    print "Dominik has wandered this earth for " + str(since_birth)
    print
    print "Dominik has been alive for " + str(since_birth.total_seconds()) + " seconds."
    print

    day_of_birth = datetime.datetime(1988, 2, 3, 6, 35)
    after_10000_days = day_of_birth + datetime.timedelta(days=10000)
    after_1000000000_seconds = day_of_birth + datetime.timedelta(seconds=1000000000)
    print "Dominik's 10.000th day will be on: " + str(after_10000_days)
    print
    print "Dominik will be 1 billion seconds old on: " + str(after_1000000000_seconds)
