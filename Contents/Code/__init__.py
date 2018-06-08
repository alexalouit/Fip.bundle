####################################################################################################
def Start():

	ObjectContainer.art = R('art-default.jpg')
	ObjectContainer.title1 = 'FIP'
	TrackObject.thumb = R('icon-default.png')

####################################################################################################
@handler('/music/fip', 'FIP', thumb='icon-fip.png', art='art-default.jpg')
def MainMenu():

	oc = ObjectContainer()
	oc.add(CreateTrackObject(url='https://direct.fipradio.fr/live/fip-midfi.mp3', title='FIP'))
	oc.add(CreateTrackObject(url='https://direct.fipradio.fr/live/fip-webradio1.mp3', title='FIP Rock'))
	oc.add(CreateTrackObject(url='https://direct.fipradio.fr/live/fip-webradio2.mp3', title='FIP Jazz'))
	oc.add(CreateTrackObject(url='https://direct.fipradio.fr/live/fip-webradio3.mp3', title='FIP Groove'))
	oc.add(CreateTrackObject(url='https://direct.fipradio.fr/live/fip-webradio4.mp3', title='FIP World'))
	oc.add(CreateTrackObject(url='https://direct.fipradio.fr/live/fip-webradio5.mp3', title='FIP New'))
	oc.add(CreateTrackObject(url='https://direct.fipradio.fr/live/fip-webradio6.mp3', title='FIP Reggae'))

	return oc

####################################################################################################
def CreateTrackObject(url, title, include_container=False, offset=0, **kwargs):

	track_object = TrackObject(
		key = Callback(CreateTrackObject, url=url, title=title, include_container=True),
		rating_key = url,
		title = title,
		source_title = title,
		thumb = R('icon-' + title.lower().replace(' ', '-') + '.png'),
		art = R('art-default.jpg'),
		items = [
			MediaObject(
				parts = [
					PartObject(key=Callback(PlayAudio, url=url, ext='mp3'))
				],
				container = Container.MP3,
				bitrate = 128,
				audio_codec = AudioCodec.MP3,
				audio_channels = 2
			)
		]
	)

	if include_container:
		return ObjectContainer(objects=[track_object])
	else:
		return track_object

####################################################################################################
def PlayAudio(url):

	return Redirect(url)
