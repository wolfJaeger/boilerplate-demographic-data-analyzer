import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('./adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df.loc[(df['sex'] == 'Male'), 'age'].mean(), 1)

    # numer of entries
    n_all = df.shape[0]

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(df.loc[(df['education'] == 'Bachelors')].shape[0] / n_all * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`    
    n_higher_educated = df.query('education in ("Bachelors","Masters","Doctorate")').shape[0]
    n_lower_educated = df.query('education not in ("Bachelors","Masters","Doctorate")').shape[0]
    higher_education = round(n_higher_educated / n_all * 100, 1)
    lower_education = round(n_lower_educated / n_all * 100, 1)

    # percentage with salary >50K
    n_higher_educated_rich = df.query('education in ("Bachelors","Masters","Doctorate") and salary == ">50K"').shape[0]
    n_lower_educated_rich = df.query('education not in ("Bachelors","Masters","Doctorate") and salary == ">50K"').shape[0]
    higher_education_rich = round(n_higher_educated_rich / n_higher_educated * 100, 1)
    lower_education_rich = round(n_lower_educated_rich / n_lower_educated * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[(df['hours-per-week'] == min_work_hours)].shape[0]
    num_min_workers_rich = df.loc[((df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K'))].shape[0]


    rich_percentage = round(num_min_workers_rich / num_min_workers * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    salary_frame = pd.DataFrame(df.query('salary == ">50K"')['native-country'].value_counts())
    salary_frame.columns = ['num_high_salary']
    salary_frame['num_low_salary'] = df.query('salary != ">50K"')['native-country'].value_counts()
    salary_frame['pct_high_salary'] = (salary_frame['num_high_salary'] / (salary_frame['num_high_salary'] + salary_frame['num_low_salary'])) * 100
    highest_earning_country = salary_frame.sort_values(by=['pct_high_salary'], ascending=False).iloc[0].name
    highest_earning_country_percentage = round(salary_frame.sort_values(by=['pct_high_salary'], ascending=False).iloc[0]['pct_high_salary'], 1)

    # Identify the most popular occupation for those who earn >50K in India.
    rich_mask = df['salary'] == '>50K'
    india_mask = df['native-country'] == 'India'
    top_IN_occupation = df.loc[(rich_mask & india_mask)]['occupation'].value_counts(normalize=True).to_frame().iloc[0].name

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
