import json
import websockets

async def inject_popup(winner_name):
    """Injects a popup displaying the winner's name."""
    websocket_url = "ws://localhost:9222/devtools/page/YOUR_PAGE_ID"
    async with websockets.connect(websocket_url) as websocket:
        command = {
            "id": 1,
            "method": "Runtime.evaluate",
            "params": {
                "expression": f"""(() => {{
                    alert('Congratulations {winner_name}!');
                }})();"""
            }
        }
        await websocket.send(json.dumps(command))
        response = await websocket.recv()
        print("Popup Response:", response)
