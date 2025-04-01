import requests

def download_mars_photos(sol, camera, api_key):
    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
    params = {
        'sol' : sol,
        'camera' : camera,
        'api_key' : api_key
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print("HTTP request error:", e)
        return
    except ValueError:
        print("Error: response is not valid JSON.")
        return
    
    photos = data.get('photos', [])

    if not photos:
        print("No photo found")
        return
    
    photo = photos[0]
    image_url = photo.get('img_src')
    if not image_url:
        print("Photo does not have a valid URL.")
        return

    print(f"Downloading photo: {image_url}")

    try:
        image_response = requests.get(image_url)
        image_response.raise_for_status()
        filename = "mars_photo1.jpg"
        with open(filename, 'wb') as file:
            file.write(image_response.content)
        print(f"Photo saved as {filename}")
    except requests.exceptions.RequestException as e:
        print("Error while downloading the image:", e)
        return

if __name__ == "__main__":
    download_mars_photos(1000, 'fhaz', 'DEMO_KEY')
