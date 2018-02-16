import requests
import asyncio

def http_call_sync():
    for i in range(3):
        r = requests.get('https://requestb.in/1lb5p931')
        print(r.content.decode(), "Request-"+str(i+1))

async def http_call_async():
    loop = asyncio.get_event_loop()
    req1 = loop.run_in_executor(None, requests.get, "https://requestb.in/1lb5p931")
    req2 = loop.run_in_executor(None, requests.get, "https://requestb.in/1lb5p931")
    req3 = loop.run_in_executor(None, requests.get, "https://requestb.in/1lb5p931")
    ret1 = await req1
    ret2 = await req2
    ret3 = await req3

    print(ret1.content.decode(), "Request-1")
    print(ret2.content.decode(), "Request-2")
    print(ret3.content.decode(), "Request-3")


print("Synchronous Attempt:")
http_call_sync()
print("Asynchronous Attempt:")
loop = asyncio.get_event_loop()
loop.run_until_complete(http_call_async())
