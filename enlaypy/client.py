"""
Enlay.io python client

Made by Artucuno
"""
import sys, os
import json
import requests
import asyncio
import httpx
from .errors import *

class EnlayClient:
    def __init__(self, key):
        self.key = key

    def send_request(self, endpoint: str, post: bool = False, jsondata: bool = True, retasjson: bool = True, hasresponse: bool = True, data: dict = {}):
        """Send request function
        ```
        Args:
        endpoint: str - The API endpoint
        post: bool (False) - Specifies get/post request
        jsondata: bool (True) - Data is posted as json
        retasjson: bool (True) - Return response as json or text
        hasresponse: bool (True) - Specifies if the request should recieve a response
        data: dict ({}) - Data to send
        ```
        """
        headers = {
        'Authorization': self.key
        }
        if post:
            if data != {}:
                if jsondata:
                    x = requests.post('https://api.enlay.io/'+endpoint, json=data, headers=headers)
                else:
                    x = requests.post('https://api.enlay.io/'+endpoint, data=data, headers=headers)
            else:
                x = requests.post('https://api.enlay.io/'+endpoint, headers=headers)
            if hasresponse:
                if type(x.json()) != list:
                    if 'code' in x.json().keys():
                        print(x.json()['code'])
                        if x.json()['code'] == 'not authorized':
                            raise NotAuthorized(x.json()['message'])
                        elif x.json()['code'] == 'not found':
                            raise NotFound(x.json()['message'])
                        else:
                            raise OtherError(x.json()['message'])
                if retasjson:
                    return x.json()
                else:
                    return x.text
            else:
                return True
        else:
            x = requests.get('https://api.enlay.io/'+endpoint, headers=headers)
            if hasresponse:
                if type(x.json()) != list:
                    if 'code' in x.json().keys():
                        print(x.json()['code'])
                        if x.json()['code'] == 'not authorized':
                            raise NotAuthorized(x.json()['message'])
                        elif x.json()['code'] == 'not found':
                            raise NotFound(x.json()['message'])
                        else:
                            raise OtherError(x.json()['message'])
                if retasjson:
                    return x.json()
                else:
                    return x.text
            else:
                return True

    def get_advertisers(self, limit: int = 20):
        """Get a list of advertisers
        ```
        Args:
        limit: int (20) - Limit of advertisers to return
        ```
        """
        return self.send_request(f'advertisers?limit={limit}')

    def create_placements(self, id: str, unique: bool = True, max: int = 3):
        """Get a list of placements for a slot
        ```
        Args:
        id: str - Slot ID
        unique: bool (True) - Specifies if placements are unique
        max: int (3) - Max placements
        ```
        """
        return self.send_request(f'slots/{id}/placements', post=True, data={"max": max, "unique": unique})

    def click_placement(self, id: str, redirect_url: str = None):
        """Add a click to a placement
        ```
        Args:
        id: str - Placement ID
        redirect_url: str (None) - Link redirect url
        ```
        """
        s = f'p/{id}/c'
        if redirect_url:
            s += f'?redirect_url={redirect_url}'
        return self.send_request(s, hasresponse=False)

    def view_placement(self, placements: list):
        """Add an impression to a placement
        ```
        Args:
        placements: list - List of placement IDs ([{'id': '6987923797392924672'}, ...])
        ```
        """
        return self.send_request('p/v', post=True, data=placements, hasresponse=False)


class EnlayClientAsync:
    def __init__(self, key):
        self.key = key

    async def send_request(self, endpoint: str, post: bool = False, jsondata: bool = True, retasjson: bool = True, hasresponse: bool = True, data: dict = {}):
        """Send request function
        ```
        Args:
        endpoint: str - The API endpoint
        post: bool (False) - Specifies get/post request
        jsondata: bool (True) - Data is posted as json
        retasjson: bool (True) - Return response as json or text
        hasresponse: bool (True) - Specifies if the request should recieve a response
        data: dict ({}) - Data to send
        ```
        """
        headers = {
        'Authorization': self.key
        }
        client = httpx.AsyncClient()
        if post:
            if data != {}:
                if jsondata:
                    x = await client.post('https://api.enlay.io/'+endpoint, json=data, headers=headers)
                else:
                    x = await client.post('https://api.enlay.io/'+endpoint, data=data, headers=headers)
            else:
                x = await client.post('https://api.enlay.io/'+endpoint, headers=headers)
            x.raise_for_status()
            if hasresponse:
                if type(x.json()) != list:
                    if 'code' in x.json().keys():
                        print(x.json()['code'])
                        await client.aclose()
                        if x.json()['code'] == 'not authorized':
                            raise NotAuthorized(x.json()['message'])
                        elif x.json()['code'] == 'not found':
                            raise NotFound(x.json()['message'])
                        else:
                            raise OtherError(x.json()['message'])
                if retasjson:
                    await client.aclose()
                    return x.json()
                else:
                    await client.aclose()
                    return x.text
            else:
                await client.aclose()
                return True
        else:
            x = await client.get('https://api.enlay.io/'+endpoint, headers=headers)
            x.raise_for_status()
            if hasresponse:
                if type(x.json()) != list:
                    if 'code' in x.json().keys():
                        await client.aclose()
                        print(x.json()['code'])
                        if x.json()['code'] == 'not authorized':
                            raise NotAuthorized(x.json()['message'])
                        elif x.json()['code'] == 'not found':
                            raise NotFound(x.json()['message'])
                        else:
                            raise OtherError(x.json()['message'])
                if retasjson:
                    await client.aclose()
                    return x.json()
                else:
                    await client.aclose()
                    return x.text
            else:
                await client.aclose()
                return True

    async def get_advertisers(self, limit: int = 20):
        """Get a list of advertisers
        ```
        Args:
        limit: int (20) - Limit of advertisers to return
        ```
        """
        return await self.send_request(f'advertisers?limit={limit}')

    async def create_placements(self, id: str, unique: bool = True, max: int = 3):
        """Get a list of placements for a slot
        ```
        Args:
        id: str - Slot ID
        unique: bool (True) - Specifies if placements are unique
        max: int (3) - Max placements
        ```
        """
        return await self.send_request(f'slots/{id}/placements', post=True, jsondata=False, data={"max": max, "unique": unique})

    async def click_placement(self, id: str, redirect_url: str = None):
        """Add a click to a placement
        ```
        Args:
        id: str - Placement ID
        redirect_url: str (None) - Link redirect url
        ```
        """
        s = f'p/{id}/c'
        if redirect_url:
            s += f'?redirect_url={redirect_url}'
        return await self.send_request(s, hasresponse=False)

    async def view_placement(self, placements: list):
        """Add an impression to a placement
        ```
        Args:
        placements: list - List of placement IDs ([{'id': '6987923797392924672'}, ...])
        ```
        """
        return await self.send_request('p/v', post=True, data=placements, hasresponse=False)
