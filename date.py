from semantic.dates import DateService

service = DateService()
date = service.extractDate("On March 3 at 12:15pm...")
print(date);

