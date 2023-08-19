import asyncio
import websockets

async def handle_client(websockets, path):
    while True:
        try:
            message = await websocket.recv()
            print(f"Received: {message}")

            await websocket.send("Message Received: " + message)
        
        except websockets.exceptions.ConnectionClosed:
            break

start_server = websockets.serve(handle_client, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

            