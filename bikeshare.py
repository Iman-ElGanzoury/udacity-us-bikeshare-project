import time
import pandas as pd

city_data = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'nyc': 'new_york_city.csv',
             'ny': 'new_york_city.csv',
             'new york': 'new_york_city.csv',
             'newyork': 'new_york_city.csv',
             'newyorkcity': 'new_york_city.csv',
             'newyork city': 'new_york_city.csv',
             'new yorkcity': 'new_york_city.csv',
             'washington': 'washington.csv'}

keyboardinterrupt = '\nNo input taken. Please try again.'
invalid_answer = '\nPlease enter a valid answer.'
loading = '\nJUST A MOMENT........CALCULATING '
answer = ['y','n']


def filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    while True:
        try:
            city = str(input('\nWhich city do you want the data from? Chicago, New York City, or Washington?').lower())

            if city not in ['chicago', 'new york city', 'nyc', 'ny', 'new york', 'newyork', 'newyorkcity', 'newyork city', 'new yorkcity', 'washington']:
                print('\nPlease enter only the name of one of the 3 specified cities.')
                continue
            else:
                break

        except KeyboardInterrupt:
            print(keyboardinterrupt)
            continue
        else:
            break

    while True:
        try:
            month = str(input('\nEnter the name of the month: January, February, March, April, May, or June.\nReply with "none" for no month filter:').lower())

            if month not in ['january', 'february', 'march', 'april', 'may', 'june','none']:
                print('\nPlease enter only the name of a month from the first six months of the year.')
                continue
            else:
                break

        except KeyboardInterrupt:
            print(keyboardinterrupt)
            continue
        else:
            break

    while True:
        try:
            day = str(input('\nEnter the name of a day of the week.\nReply with "none" for no day filter:').lower())

            if day not in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'none']:
                print('\nThat is not a day of the week. Please try again.')
                continue
            else:
                break

        except KeyboardInterrupt:
            print(keyboardinterrupt)
            continue
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(city_data[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['Month'] = df['Start Time'].dt.month_name()
    df['Weekday'] = df['Start Time'].dt.day_name()

    if month != 'none':
        df = df[df['Month']==month.title()]
    if day != 'none':
        df = df[df['Weekday']==day.title()]

    return df


def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print(loading,'TIME STATS >>>>>>>')
    start_time = time.time()

    if month == 'none':
        most_common_month = df['Month'].mode()[0]
        print('\nThe most common month is:  ',most_common_month)
    if day == 'none':
        most_common_day = df['Weekday'].mode()[0]
        print('The most common day is:  ',most_common_day)

    df['Hour'] = df['Start Time'].dt.hour
    most_common_sh = df['Hour'].mode()[0]
    print('The most common start hour is:  ',most_common_sh)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print(loading,'STATION STATS >>>>>>>')
    start_time = time.time()

    most_common_start = df['Start Station'].mode()[0]
    most_common_end = df['End Station'].mode()[0]

    df['Trip'] = df['Start Station'] + '--' + df['End Station']
    most_common_trip = df['Trip'].mode()[0]

    print('\nThe most common start station is:   ', most_common_start)
    print('The most common end station is:   ', most_common_end)
    print('The most common trip is:   ', most_common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print(loading,'TRIP DURATION STATS >>>>>>>')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    average_travel_time = df['Trip Duration'].mean()

    print('\nThe total travel time is:   {:,} seconds.'.format(total_travel_time))
    print('The average travel time is:   {:,} seconds.'.format(average_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print(loading,'USER STATS >>>>>>>')
    start_time = time.time()

    each_type = df['User Type'].value_counts().to_string()
    print('\nThe number of users of either type are as follows:   \n{}'.format(each_type))

    if 'Birth Year' and 'Gender' in df:
        df['Gender'] = df['Gender'].fillna('Unknown')
        each_gender = df['Gender'].value_counts().to_string()

        df.dropna(inplace = True)
        df['Birth Year'] = df['Birth Year'].astype(int)
        earliest = df['Birth Year'].min()
        latest = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]

        print('\nThe number of users of either gender are as follows:   \n{}'.format(each_gender))
        print('\nThe oldest users were born in:   \n{}'.format(earliest))
        print('\nThe youngest users were born in:   \n{}'.format(latest))
        print('\nMost users were born in:   \n{}'.format(most_common_year))
    else:
        print('\nThis dataframe does not include data on Birth Year - Gender.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def restart():
    """asks for user input on if they would like to explore more."""

    while True:
        try:
            restart_input = input('\nWould you like to explore some more data? Enter "y" or "n":').lower()

            if restart_input not in answer:
                print(invalid_answer)
                continue
            if restart_input == 'n':
                print('\nAlright. Thanks for using my interactive program!')
                break

        except KeyboardInterrupt:
            print(keyboardinterrupt)
            continue
        else:
            break

    return restart_input


def main():
    print('\nHello! Welcome to this interactive 2017 US Bikeshare data project.\nNow Let\'s do some data exploration!')

    while True:
        while True:
            try:
                raw_input_question = input('\nWould you like to see 5 lines of raw data from one of the cities?\nEnter "y" or "n":').lower()

                if raw_input_question not in answer:
                    print(invalid_answer)
                    continue
                else:
                    break

            except KeyboardInterrupt:
                print(keyboardinterrupt)
                continue
            else:
                break

        x = 5
        y = 10

        if raw_input_question == 'y':
            city, month, day = filters()

            print('\nJUST A MOMENT........DISPLAYING RAW DATA >>>>>>>\n')
            start_time = time.time()

            df = load_data(city, month, day)
            print(df.head().to_string())

            print("\nThis took %s seconds." % (time.time() - start_time))
            print('-'*40)

            while True:
                try:
                    raw_input_2 = input('\nMore lines? Enter "y" or "n":').lower()

                    if raw_input_2 not in answer:
                        print(invalid_answer)
                        continue
                    elif raw_input_2 == 'y':
                        print('\n',df.iloc[x:y].to_string())
                        print('-'*40)
                        x += 5
                        y += 5
                        continue
                    else:
                        print('\nAlright!\n')

                except KeyboardInterrupt:
                    print(keyboardinterrupt)
                    continue
                else:
                    break

        else:
            city, month, day = filters()
            df = load_data(city, month, day)
            time_stats(df, month, day)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)

        if restart() == 'y':
            continue
        else:
            break


if __name__ == '__main__':
    main()
