# key-value
simple key-value memory store

methods

  Put
    Params
    -key ()
    -value () 
    -ttl: (seconds to maintain the value for retrieval
    Return
    -1 if successful
    -KeyError if key is not approved
  Retrieve
    Params
    -key()
    Return
  Delete
    Params
    -key()
    Return
    -1 if successful
    -KeyError if key is not approved
Examples
    ```
    database = keyvalue.KeyValue()
    await database.put('hello','world'))
    value = await database.retrieve('hello')
    print(value)
    ````
    Expected output:

    ```
    world
    ```

