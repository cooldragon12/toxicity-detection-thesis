from channels.generic.websocket import AsyncJsonWebsocketConsumer

class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add(
            self.scope['user'].username,
            self.channel_name
        )
    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.scope['user'].username,
            self.channel_name
        )
    
    async def receive_json(self, content):
        await self.channel_layer.group_send(
            self.scope['user'].username,
            {
                'type': 'chat_message',
                'message': content['message']
            }
        )
    
    async def chat_message(self, event):
        await self.send_json({
            'message': event['message']
        })