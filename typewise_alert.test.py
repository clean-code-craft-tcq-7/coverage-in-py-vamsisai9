import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
    self.assertTrue(typewise_alert.infer_breach(120, 50, 100) == 'TOO_HIGH')
    self.assertTrue(typewise_alert.infer_breach(60, 50, 100) == 'NORMAL')

  def test_temparature_breach_classification_high(self):
    self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING',36) == 'TOO_HIGH')
    self.assertTrue(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING',46) == 'TOO_HIGH')
    self.assertTrue(typewise_alert.classify_temperature_breach('MED_ACTIVE_COOLING',100) == 'TOO_HIGH')

  def test_temparature_breach_classification_low(self):
    self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING',-45) == 'TOO_LOW')
    self.assertTrue(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING',-45) == 'TOO_LOW')
    self.assertTrue(typewise_alert.classify_temperature_breach('MED_ACTIVE_COOLING',-45) == 'TOO_LOW')

  def test_temparature_breach_classification_normal(self):
    self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING',33) == 'NORMAL')
    self.assertTrue(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING',41) == 'NORMAL')
    self.assertTrue(typewise_alert.classify_temperature_breach('MED_ACTIVE_COOLING',39) == 'NORMAL')


if __name__ == '__main__':
  unittest.main()
