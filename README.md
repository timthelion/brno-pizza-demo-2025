Example project setting up EMQX to use Websockets secured with JWT tokens
---------------------------------------------------------------------------------------

This is an example project demonstrating how to setup MQTT using EMQX for the purpose of sending live messages to web clients.

You can launch emqx with:

```
sh launch-emqx.sh
```

You can generate jwt tokens using:

```
python3 generate-jwt.py --username tim
```

You can generate an admin jwt token using:

```
python3 generate-jwt.py --username admin --admin
```

You can send a message to a user as admin using:

```
mqttui --username admin --password $token --broker  ws://localhost:8085/mqtt  publish /users/<tim>/foo bas
```

You can watch for messages as a user using:

```
mqttui --username tim --password $token --broker ws://localhost:8085/mqtt foo
```
