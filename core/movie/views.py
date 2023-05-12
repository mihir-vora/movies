import time
import json
import redis
import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache

# def movie_details(request, movie_id):
#     api_key = '0ba968234e47d96aa0c99613677bccb5'
#     url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'

#     try:
#         response = requests.get(url)
#         data = response.json()
#         return JsonResponse(data)
#     except requests.exceptions.RequestException as e:
#         return JsonResponse({'error': str(e)})



def movie_details(request, movie_id):
	try:
		api_key = '0ba968234e47d96aa0c99613677bccb5'
		url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'

		cache_key = f"movie_details:{movie_id}"

		redis_client = redis.Redis(
			host="localhost", port=6379, db=0
		)
		movie_details = redis_client.get(cache_key)

		if movie_details is None:
			response = requests.get(url)
			movie_details = response.json()
			redis_client.set(cache_key, json.dumps(movie_details), ex=60)  # Set expiration time of 1 minute (60 seconds)

			return JsonResponse(movie_details)
		else:
			new_str = movie_details.decode('utf-8')
			movie_details = json.loads(new_str)  

			return JsonResponse(movie_details)
	except requests.exceptions.RequestException as e:
		return JsonResponse({'error': str(e)})

	