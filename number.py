from semantic.numbers import NumberService

service = NumberService()

print service.parse("Two hundred and six")

print service.parse("Five point one five")


print service.parse("Eleven and two thirds")


print service.parseMagnitude("7e-05")

