import sys
import pytest
import asyncio
import time
sys.path.insert(1, '../key-value');
import keyvalue
#single put and retrieve
def test_put_get():
    database = keyvalue.KeyValue()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(database.put('hello','world'))
    value = loop.run_until_complete(database.retrieve('hello'))
    assert value == 'world';

#retrieve value should raise exceptions
def test_get_empty_exception():
    database = keyvalue.KeyValue()
    loop = asyncio.get_event_loop()
    with pytest.raises(KeyError):
        value = loop.run_until_complete(database.retrieve('hello'))

#put followed by delete should cause retrieve to throw exception
def test_put_delete():
    database = keyvalue.KeyValue()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(database.put('hello','world'))
    loop.run_until_complete(database.delete('hello'))
    with pytest.raises(KeyError):
        value = loop.run_until_complete(database.retrieve('hello'))

#delete empty should cause exception
def test_delete_empty():
    database = keyvalue.KeyValue()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(database.put('hello','world'))
    loop.run_until_complete(database.delete('hello'))
    with pytest.raises(KeyError):
        value = loop.run_until_complete(database.retrieve('hello'))

#put with timelimit should return if queried quickly. 
def test_put_time():
    database = keyvalue.KeyValue()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(database.put('hello','world', 30))
    value = loop.run_until_complete(database.retrieve('hello'))
    assert value == 'world';

#put with timelimit then wait should throw exception after ttl expired
def test_put_time_expire():
    database = keyvalue.KeyValue()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(database.put('hello','world', 2))
    time.sleep(15);
    with pytest.raises(KeyError):
        value = loop.run_until_complete(database.retrieve('hello'))
