def convert_minutes(total_minutes):
    days = total_minutes // (24 * 60)
    hours = (total_minutes % (24 * 60)) // 60
    minutes = total_minutes % 60
    return days, hours, minutes

if __name__ == "__main__":
    total_minutes = int(input("Entrez le nombre total de minutes : "))
    days, hours, minutes = convert_minutes(total_minutes)
    print(f"{total_minutes} minutes équivalent à {days} jours, {hours} heures et {minutes} minutes.")