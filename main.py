# project 2
import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    global city
    city = ""
    while (city != 'chicago' and city != 'new york city' and city != 'washington'):
        city = input("Please enter city (chicago, new york city, washington): ")
        city = city.lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    month = ""
    while (
            month != 'all' and month != 'january' and month != 'february' and month != 'march' and month != 'april' and month != 'may' and month != 'june'):
        month = input("Please enter month (all, january, february, ... , june): ")
        month = month.lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ""
    while (
            day != 'all' and day != 'monday' and day != 'tuesday' and day != 'wednesday' and day != 'thursday' and day != 'friday' and day != 'saturday' and day != 'sunday'):
        day = input("Please enter the day of the week (all, monday, tuesday, ... sunday): ")
        day = day.lower()

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    # i took this method from my solution to problem 3
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is ")
    print((df['Start Time'].dt.month).mode()[0])

    # TO DO: display the most common day of week
    print("The most common day of week is ")
    print((df['Start Time'].dt.day).mode()[0])

    # TO DO: display the most common start hour
    print("The most common start hour is ")
    print((df['Start Time'].dt.hour).mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station is ")
    print(df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("The most commonly used end station is ")
    print(df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print("The most frequent combination of start station and end station trip is ")
    print((df['End Station'] + " " + (df['Start Station'])).mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time is ")
    print(df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("The mean travel time is ")
    print(df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("The counts of user types is ")
    print(df['User Type'].value_counts())

    if city == 'chicago' or city == 'new york city':
        # TO DO: Display counts of gender
        print("The counts of gender is ")
        print(df['Gender'].value_counts())

        # TO DO: Display earliest, most recent, and most common year of birth
        print("The earliest year of birth is ")
        print(df['Birth Year'].min())
        print("The most recent year of birth is ")
        print(df['Birth Year'].max())
        print("The most common year of birth is ")
        print(df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_data(df):
    view = input('Would you like to view 5 rows of raw data? Please enter yes or no : ').lower()
    loc = 0
    while (view == 'yes'):
        print(df.iloc[loc:loc + 5])
        loc += 5
        view = input("Would you like to see 5 more rows? ").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() == 'no':
            break
        elif restart.lower() != 'yes':
            print("incorrect input")
            break


if __name__ == "__main__":
    main()

