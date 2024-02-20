def urlEncode(text):
  text = text.strip()
  text = text.replace(" ", "%20")

  return text

print(urlEncode("Lighthouse Labs"))
print(urlEncode(" Lighthouse Labs  "))
print(urlEncode("blue is greener than purple for sure"))