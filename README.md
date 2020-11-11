# key-value
simple key-value memory store

# methods

  Put

    Params

    -key (alphanumeric of less than 64 characters in length)

    -value (alphanumeric of less than 128 characters in length) 

    -ttl: (seconds to maintain the value for retrieval

    Return

    -1 if successful

    -KeyError if key is not approved

    -KeyError if value is not approved

  Retrieve

    Params

    -key (alphanumeric of less than 64 characters in length)

    Return

    -value if value has been set and is not expired
    -KeyError if value cannot be found

  Delete

    Params

    -key (alphanumeric of less than 64 characters in length)

    Return

    -1 if successful

    -KeyError if key is not approved

# Examples

    ```

    database = keyvalue.KeyValue()

    await database.put('hello','world'))

    value = await database.retrieve('hello')

    print(value)

    ```

    Expected output:


    `
    world
    `

