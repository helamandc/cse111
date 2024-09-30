def cels_from_fahr(fahr):
  """Convert a temperature in Fahrenheit to
  Celsius and return the Celsius temperature.
  """
  cels = (fahr - 32) * 5 / 9
  return cels

def main():
  fahr = 70
  cels = cels_from_fahr(fahr)
  print(f"{cels:.2f}")

if __name__ == "__main__":
  main()