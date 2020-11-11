import asyncio
import time
from cacheout import Cache

KEY_LENGTH = 64
VALUE_LENGTH = 128
DEFAULT_TIME = 0 #0 for keep until deleted
MAX_SIZE = 10000000

class KeyValue:
    #define two stores a dictionary for indeterminate storage and a ttl cache for expiring data
    def __init__(self):
        self.cache = {};
        self.cache_ttl = Cache(maxsize=MAX_SIZE, ttl=0, timer = time.time, default=None)
    
    #add data to cache if no ttl. add to cache_ttl if time limit provided
    async def put(self, key, value, expire_time=DEFAULT_TIME):
        if(not self._checkKey(key)):
            raise KeyError;
        if(not self._checkValue(value)):
            raise KeyError;

        if expire_time != 0:                                        #if data has expire time set to ttl cache and delete if exists in indeterminate cache
            self.cache_ttl.set(key, value, ttl=expire_time)
            await self._delete_cache(key)
        else:
            self.cache[key] = value                         
        return 1

    #retrieve data if avialable
    async def retrieve(self, key):
        if(not self._checkKey(key)):
            raise KeyError;
        result = await self._retrieve_cache(key)
        result_ttl = await self._retrieve_cache_ttl(key)
        if(result == False and result_ttl == False):
            raise KeyError
        elif result:
            return result
        else:
            return result_ttl

    async def delete(self, key):
        if(not self._checkKey(key)):
            raise KeyError
        await self._delete_cache(key)
        await self._delete_cache_ttl(key)
        return 1;

    #retrieval for cache and ttl cache
    async def _retrieve_cache(self, key):
        if(not await self._contains_cache(key)):
            return False;
        return self.cache[key];
    async def _retrieve_cache_ttl(self, key):
        if(not await self._contains_cache_ttl(key)):
            return False
        return self.cache_ttl.get(key);
    
    #deletion for cache and ttl cache
    async def _delete_cache(self, key):
        if(not await self._contains_cache(key)):
            return 1
        del self.cache[key]
        return 1
    async def _delete_cache_ttl(self, key):
        if(not await self._contains_cache_ttl(key)):
            return 1
        del self.cache_ttl[key]
        return 1
    
    #check key and value being alpha numberic strings of approriate length
    def _checkKey(self, key):
        if(isinstance(key, str) and key.isalnum() and len(key) <= KEY_LENGTH):
            return True
        else:
            return False
    def _checkValue(self, value):
        if(isinstance(value, str) and value.isalnum() and len(value) <= VALUE_LENGTH):
            return True
        else:
            return False
    #check each data store for key values
    async def _contains_cache(self, key):
        return key in self.cache.keys()
    async def _contains_cache_ttl(self, key):
        return self.cache_ttl.has(key)




