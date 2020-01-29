<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 17:33:00 2020

@author: OKORNOE
"""

import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_dic = {1:"January", 2:"february", 3:"March", 4:"April", 5:"May", 6:"June",-1:"all"}

days_dic = {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday",
            6:"Saturday", 7:"Sunday",-1:"all"}


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

    city_input = input("\nEnter the city you which to analyse\n")
    city = city_input.lower()
	while city := input("Please enter city among chicago, new york city, washington :").lower() not in city_list:
        continue
  

    # TO DO: get user input for month (all, january, february, ... , june)
    print("Enter -1 to apply no month filter to the data")
    print("Please enter 1 for January and 6 for June in that order")
    month_input = input("Enter the month you want to filter\n")
    month = int(month_input)
    while month not in month_dic:
        month_input = input("\nInvalid input; Enter the month you want to filter again\n")
        month = int(month_input)
    month = month_dic[month].lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print("Enter -1 to apply no month filter to the data")
    print("Please enter 1 for monday and 7 for sunday in that order\n")
    day_input = input("\nEnter the day you want to filter\n")
    day = int(day_input)
    while day not in days_dic:
        day_input = input("\nEnter the day you want to filter again\n")
        day = int(day_input)
    day = days_dic[day]

    print('-' * 40)
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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common hour
    df['hour'] = df['Start Time'].dt.hour
    # find the most popular hour
    common_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', common_hour)

    df['month'] = df['Start Time'].dt.month
    # find the most popular hour
    common_month = df['month'].mode()[0]
    print('Most Popular month:', month_dic[common_month])

    df['day'] = df['Start Time'].dt.weekday
    # find the most popular hour
    common_day = df['day'].mode()[0]
    print('Most Popular day:', days_dic[common_day+1])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The common use start station is: " , common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most common end station is: ", common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['start_end_station'] = df['Start Station'] + ' to ' + df['End Station']
    print(df.start_end_station.mode().loc[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total time travel is: ", total_travel)

    mean = df['Trip Duration'].mean()
    print("mean of trip duration is ", mean)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print("User type count is ", user_type_count)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print("User type count is ", gender)
    else:
        print("This data has no Gender column")
        

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        most_recent_birth_year = df['Birth Year'].max()
        most_earliest_birth_year = df['Birth Year'].min()
        most_common_birth_year = df['Birth Year'].mode()[0]
        print("Most recent birth year is {}".format(most_recent_birth_year))
        print("Most earliest birth year is {}".format(most_earliest_birth_year))
        print("Most common birth year is {}".format(most_common_birth_year))
    else:
        print("This dataset has no birth year")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def view_raw_data(df):
    
	""" Asks users whether they want to view raw data of the file and
	prints the first five rows of the data using a dictinary """
    input_list = ["yes", "no"]
    n =5
    
    while True:
        user_input = input("\nDo you want to see (more) raw data; Enter yes or no\n")
        if user_input not in input_list:
            user_input = input("\nInvalid input, try again\n")
        elif user_input == input_list[0]:
            new_list = df.head(n).to_dict(orient='records')
            for item in new_list:
                print(item,'\n\n\n')
            n+=10
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()

