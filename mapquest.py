import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "1WZGOsaCbV8bduXMJD9NbvhyYzZWQW2L"


while True:
    orig = input("Starting Location: ")
    if orig == "salir" or orig == "s":
        break
    dest = input("Destination: ")
    if dest == "salir" or dest == "s":
        break

    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest, "locale":"es_ES","unit":"K"}) 
    json_data = requests.get(url).json()
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
        print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"]))))
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format(each["distance"])) + " km)")
        print("=============================================\n")
    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Entradas de usuario no válidas para una o ambas ubicaciones.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Falta una entrada para una o ambas ubicaciones.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")