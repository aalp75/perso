############# ENIGMA #############
### Model M3 - German Army WW2 ###
######### Author: aalp75 #########


Contents
I   - M3 Machine
II  - Code
III - How to run
IV  - Examples

I - M3 Machine ##############################

  M3 Machine is composed of
  1 reflector to chose among 2
  3 rotors to chose among 5
  1 plugboard to chose for reverse 10 letters at maximum

  Plugboard; ex (‘AV’,’DE’,’HO’,’JK’,’LS’,’XQ’)
  Rotors used and their oder ; ex (‘I’,’VI’,’II’)
  Initial position of rotors ; ex (25, 6, 4)
  reflector used ; ex ‘RefB’

II  - Code ##############################

  Implement in Python 3 with Jupyter Notebook as an objects
  Plugboard, rotors and reflector are implemented as list of numero and each list correspond to the permutation associated.
  For example if Plugboard[1] = 5 that mean the letters B(2) is coded as F(5).

III - How to run ##############################

  Create ur Enigma Machine with : Enigma()

  Setup your settings with :

    new_plug = ['AW','HX','CO','JP','EK','FR']
    new_rotorpos = ['M','R','Z']
    new_rotsetup = [5,2,3]
    new_refsetup = 1

    enigma.setup(new_plug,new_rotorpos,new_rotsetup,new_refsetup)

  Write ur message you want to crypt in message_clean.txt

  Run enigma.encrypt_file('message_clean.txt','message_encrypt.txt')

  Your message encrypted is now in message_encrypt.txt

IV - Examples ##############################

  Clean message : I WANT TO MEET YOU AT MIDNIGHT TOMORROW
  Encrypt message : Y NGUM DS ZSHB BJI SH LCHFXXXD ZDISLPGU

  Clean message : I REALLY DON T LIKE YOUR NEW FRIEND
  Encrypt message : Y SXCWSP YHL B PEMG SGHZ FJU LKMRXI
