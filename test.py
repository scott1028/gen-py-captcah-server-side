from io import BytesIO
from captcha.audio import AudioCaptcha
from captcha.image import ImageCaptcha

#audio = AudioCaptcha(voicedir='/path/to/voices')
#image = ImageCaptcha(fonts=['/path/A.ttf', '/path/B.ttf'])

#data = audio.generate('1234')
#assert isinstance(data, bytearray)
#audio.write('1234', 'out.wav')

# data = image.generate('1234')

# assert isinstance(data, BytesIO)
# import pdb; pdb.set_trace()

def testcase01():
	image = ImageCaptcha()
	image.write('1234', '1234.png')

def testcase02():
	image = ImageCaptcha()
	data = image.generate('4567')
	with open('4567.png', 'a') as fd:
		fd.write(data.read())

testcase01()
testcase02()
