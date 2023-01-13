
collingInfo = {
      'PASSIVE_COOLING' : {'lower':0,'upper':35},
      'HI_ACTIVE_COOLING' : {'lower':0,'upper':45},
      'MED_ACTIVE_COOLING' : {'lower':0,'upper':40}

      }

def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'



def classify_temperature_breach(coolingType, temperatureInC):
  return infer_breach(temperatureInC, collingInfo[coolingType]['lower'], collingInfo[coolingType]['upper'])


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

def send_email(message, recepient = "a.b@c.com",):
    print(f'To: {recepient}')
    print(message)


def getBreachMessage(breachType):
  if breachType == 'TOO_LOW':
    return 'Hi, the temperature is too low'
  elif breachType == 'TOO_HIGH':
    return 'Hi, the temperature is too high'


def prepare_email(breachType):
  breachMessage = getBreachMessage(breachType)
  send_email(breachMessage)
