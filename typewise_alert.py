
def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'


def assignLimits(coolingType):
  if coolingType == 'PASSIVE_COOLING':
      return 0,35
  elif coolingType == 'HI_ACTIVE_COOLING':
      return 0,45
  elif coolingType == 'MED_ACTIVE_COOLING':
      return 0,40
  return 0,0


def classify_temperature_breach(coolingType, temperatureInC):
  lowerLimit,upperLimit = assignLimits(coolingType)
  return infer_breach(temperatureInC, lowerLimit, upperLimit)


def alertAction(alertTarget,breachType):
  if alertTarget == 'TO_CONTROLLER':
    send_to_controller(breachType)
  elif alertTarget == 'TO_EMAIL':
    prepare_email(breachType)


def check_and_alert(alertTarget, batteryChar, temperatureInC):
  breachType = classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
  alertAction(alertTarget,breachType)



def send_to_controller(breachType):
  header = 0xfeed
  print(f'{header}, {breachType}')

def send_email(recepient,message):
    print(f'To: {recepient}')
    print(message)

def prepare_email(breachType):
  recepient = "a.b@c.com"
  if breachType == 'TOO_LOW':
    send_email(recepient,'Hi, the temperature is too low')
  elif breachType == 'TOO_HIGH':
    send_email(recepient,'Hi, the temperature is too high')