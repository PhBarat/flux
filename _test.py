# b45ab922-e413-45dc-800c-b9622042574c

from flux.api import ImageRequest

# this will create an api request directly but not block until the generation is finished
# request = ImageRequest("A beautiful beach", name="flux.1.1-pro")
request = ImageRequest("A beautiful beach", name="flux.1.1-pro", api_key="b45ab922-e413-45dc-800c-b9622042574c")

# any of the following will block until the generation is finished
request.url
# -> https:<...>/sample.jpg
request.bytes
# -> b"..." bytes for the generated image
request.save("outputs/api.jpg")
# saves the sample to local storage
request.image
# -> a PIL image

